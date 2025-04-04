import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass 

API_key = '10b20d494de92c5f001630a24ff98007'

def get_weather_data(city_name, state_code, country_code, API_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{state_code},{country_code}&appid={API_key}&units=imperial'
    response = requests.get(url)
    data = response.json()

    main = data.get('main')
    weather = data.get('weather')
    wind = data.get('wind')
    timezone = data.get('timezone')
    sys = data.get('sys')

    return {
        'main' : weather[0].get('main'),
        'description' : weather[0].get('description'),
        'temp' : main.get('temp'),
        'feels_like' : main.get('feels_like'),
        'humidity' : weather[0].get('humidity'),
        'temp_min' : main.get('temp_min'),
        'temp_max' : main.get('temp_max'),
        'speed' : wind.get('speed'),
        'name' : timezone,
        'country' : sys.get('country')
    }

print(get_weather_data('nashville', 'TN', 'US', API_key))

    

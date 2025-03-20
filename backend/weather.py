import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass 

API_key = '10b20d494de92c5f001630a24ff98007'

def get_weather_data(city_name, state_code, country_code, API_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{state_code},{country_code}&appid={API_key}&units=imperial'
    response = requests.get(url)
    data = response.json()
    weather = data.get('weather')
    return weather
print(get_weather_data('nashville', 'TN', 'US', API_key))

    

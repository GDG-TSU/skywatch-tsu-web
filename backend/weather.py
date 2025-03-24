import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass 

load_dotenv()
api_key = os.getenv('API_KEY')

@dataclass
class WeatherData:
    main: str

def get_weather_data(city_name, state_code, country_code, API_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{state_code},{country_code}&appid={API_key}&units=imperial'
    response = requests.get(url)
    data = response.json()

    main = data.get('main')
    weather = data.get('weather')
    wind = data.get('wind')
    sys = data.get('sys')

    return {
        'main' : weather[0].get('main'),
        'description' : weather[0].get('description'),
        'temp' : main.get('temp'),
        'feels_like' : main.get('feels_like'),
        'humidity' : main.get('humidity'),
        'temp_min' : main.get('temp_min'),
        'temp_max' : main.get('temp_max'),
        'speed' : wind.get('speed'),
        'name' : data.get('name'),
        'country' : sys.get('country')
    }
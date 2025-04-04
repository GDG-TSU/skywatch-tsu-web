import requests
from dotenv import load_dotenv
import os 
from dataclasses import dataclass
API_key = '10b20d494de92c5f001630a24ff98007'
def different_weather(city_name, state_code, country_code, API_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{state_code},{country_code}&appid={API_key}&units=imperial'
    response = requests.get(url)
    data = response.json()
    return data

@dataclass
class WeatherData:
    main: str
    description: str
    temperature: float
    feels_like: float
    temp_min: float
    temp_max: float
    humidity: int
    wind_speed: float
    city_name: str
    country_code: str
    state_code: str
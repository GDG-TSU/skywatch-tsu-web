import requests

API_key = '7eff5dbb6f6d6f32af78be9196c2f179'

def get_weatherData(city_name,state_code,country_code, API_key):

    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?'
                            f'q={city_name},{state_code},{country_code}&appid={API_key}')

    weatherData = response.json()



    
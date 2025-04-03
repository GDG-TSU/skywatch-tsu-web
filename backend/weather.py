import requests
import pprint

def getweather(city, state, country, apikey):
    
    response = pip._vendor.requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&appid={apikey}')
    return response.json()

<<<<<<< HEAD
pprint.pprint(getweather('Nashville', 'TN', 'US', '7883ad61ed21bb9a011bfb77a06feae1'))



class WeatherData:
    def __init__(city_name, state_code, country_code, api_key):
        weather_data = getweather(city_name, state_code, country_code, api_key)
        weather = weather_data['weather'][0]
        main = weather['main']
        description = weather['description']
        temp = weather_data['main']['temp']
        icon = weather['icon']
        return weather_data(main, description, temp, icon)


    
=======
pprint.pprint(getweather('Nashville', 'TN', 'US', '[APIKEY]'))
>>>>>>> 393eb119ea9824c44578994479f6217e4246f813

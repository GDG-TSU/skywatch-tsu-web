import pip._vendor.requests
import pprint

def getweather(city, state, country, apikey):
    
    response = pip._vendor.requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&appid={apikey}')
    return response.json()

pprint.pprint(getweather('Nashville', 'TN', 'US', '7883ad61ed21bb9a011bfb77a06feae1'))
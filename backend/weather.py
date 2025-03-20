import pip._vendor.requests
import pprint

def getweather(city, state, country, apikey):
    
    response = pip._vendor.requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&appid={apikey}')
    return response.json()

pprint.pprint(getweather('Nashville', 'TN', 'US', '[APIKEY]'))

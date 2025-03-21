import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

def WeatherCity(City):
    A = "http://api.openweathermap.org/geo/1.0/direct?q=" + City + "&limit=5&appid=f51ea00159e3b0ea63353b97120d6c2b"
    data = requests.get(A).json()
    Coords = []
    Coords.append(data[0]['lon'])
    Coords.append(data[0]['lat'])
    LONG = Coords[0]
    LAT = Coords[1]
    Weathera = Weather(LONG, LAT)
    return Weathera
    
def Weather(Long, Lati):
    Website = "https://api.openweathermap.org/data/3.0/onecall?"

    API_KEY = "&appid=dc9b91e41a1ec09655f6fb56ef16855d"

    LONGI = str(Lati)
    LATI = str(Long)

    importing = Website + "lat=" + LONGI + "&lon=" + LATI + API_KEY + "&units=imperial"

    response = requests.get(importing).json()

    stuff = []
    stuff.append(response['current']['temp'])
    stuff.append(response['current']['feels_like'])
    stuff.append(response['current']['weather'][0]['main'])
    return stuff



print(WeatherCity("Nashville"))
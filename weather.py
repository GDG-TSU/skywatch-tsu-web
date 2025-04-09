import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

# Load environment variables
load_dotenv()
api_key = os.getenv('API_KEY')
if not api_key:
    print("WARNING: API_KEY not found in environment variables!")

@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temp: float
    feels_like: float
    humidity: int
    temp_min: float
    temp_max: float
    wind_speed: float
    location: str
    country: str
    background_image: str  # Added for dynamic background image
    icon_image: str  # Added for dynamic weather icon

def get_weather_background(main_condition, description):
    """
    Determine the appropriate background image based on weather conditions
    Using only: sunny.jpg, rainy.jpg, cloudy.jpg, snowy.jpg, foggy.jpg
    """
    main_condition = main_condition.lower() if main_condition else ""
    description = description.lower() if description else ""
    
    # Map weather conditions to available background images
    if 'thunderstorm' in main_condition or 'rain' in main_condition or 'drizzle' in main_condition:
        return 'rainy.jpg'
    elif 'snow' in main_condition or 'ice' in main_condition or 'sleet' in main_condition:
        return 'snowy.jpg'
    elif 'clear' in main_condition:
        return 'sunny.jpg'
    elif 'clouds' in main_condition:
        return 'cloudy.jpg'
    elif 'mist' in main_condition or 'fog' in main_condition or 'haze' in main_condition:
        return 'foggy.jpg'
    else:
        # Default background for any other conditions
        return 'cloudy.jpg'

def get_weather_icon(icon_code):
    """
    Map OpenWeatherMap icon codes to available icons:
    clear_day.png, clear_night.png, clouds.png, rain_day.png
    """
    # Basic mapping focusing on day/night and main weather type
    if icon_code.startswith('01'):  # Clear sky
        return 'clear_day.png' if icon_code.endswith('d') else 'clear_night.png'
    elif icon_code.startswith(('09', '10')):  # Rain
        return 'rain_day.png'
    else:  # All other conditions
        return 'clouds.png'

def get_weather_data(city_name, state_code, country_code, API_key):
    # Build the URL with the provided parameters
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{state_code},{country_code}&appid={API_key}&units=imperial'
    
    # Make the API request and handle potential errors
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        
        # Check if the API returned an error
        if 'cod' in data and str(data['cod']) != '200':
            print(f"API Error: {data.get('message', 'Unknown error')}")
            return None
            
        # Safely get nested data with error handling
        main = data.get('main', {})
        weather = data.get('weather', [])
        wind = data.get('wind', {})
        sys = data.get('sys', {})
        
        # Check if weather data is available
        if not weather:
            print("No weather data available")
            return None
        
        # Get weather condition for determining background
        main_condition = weather[0].get('main', '')
        description = weather[0].get('description', '')
        icon_code = weather[0].get('icon', '01d')
        
        # Determine appropriate background and icon images
        background_image = get_weather_background(main_condition, description)
        icon_image = get_weather_icon(icon_code)
            
        return WeatherData(
            main=weather[0].get('main', ''),
            description=weather[0].get('description', ''),
            icon=weather[0].get('icon', ''),
            temp=main.get('temp', 0.0),
            feels_like=main.get('feels_like', 0.0),
            humidity=main.get('humidity', 0),
            temp_min=main.get('temp_min', 0.0),
            temp_max=main.get('temp_max', 0.0),
            wind_speed=wind.get('speed', 0.0),
            location=data.get('name', city_name),
            country=sys.get('country', country_code),
            background_image=background_image,
            icon_image=icon_image
        )
        
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return None
    except Exception as e:
        print(f"Error processing weather data: {e}")
        return None

def main(city_name, state_code, country_code):
    weather_data = get_weather_data(city_name, state_code, country_code, api_key)
    return weather_data
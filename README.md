# SkyWatch TSU

A dynamic weather application built for Tennessee State University that provides real-time weather information based on user location input.

<img width="1271" alt="Screenshot 2025-04-09 at 4 57 12 PM" src="https://github.com/user-attachments/assets/48ef30f1-a879-48c6-9cf2-c3a31078f2b2" />


## Features

- **Real-time Weather Data**: Fetches current weather conditions from the OpenWeatherMap API
- **Dynamic Weather Visuals**: Background images and icons change based on current weather conditions
- **Location-Based Weather**: Users can enter any city, state, and country to get localized weather information
- **Responsive Design**: Clean interface that works across desktop and mobile devices
- **Comprehensive Data**: Displays temperature, feels-like temperature, humidity, wind speed, and more

## Weather Information Displayed

- Current temperature
- Location name and country
- Weather description
- "Feels like" temperature
- Humidity percentage
- Minimum and maximum temperature
- Wind speed

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **APIs**: OpenWeatherMap API

## Project Structure

```
skywatch-tsu/
├── app.py                  # Main Flask application
├── weather.py              # Weather data processing module
├── static/
│   ├── index.css           # CSS styles
│   └── assets/
│       ├── weather.png     # Application logo
│       ├── Icons/          # UI icons
│       └── weatherIcons/   # Weather condition images
├── templates/
│   └── index.html          # Main HTML template
├── .env                    # Environment variables (API key)
└── requirements.txt        # Python dependencies
```

## Getting an OpenWeatherMap API Key

1. Sign up for a free account at [OpenWeatherMap](https://openweathermap.org/)
2. Navigate to your account's "API Keys" section
3. Generate a new API key
4. Copy the key into your `.env` file


## Acknowledgments

- Built by the GDG team at Tennessee State University
- Weather data provided by [OpenWeatherMap](https://openweathermap.org/)
- Icons and images curated for various weather conditions

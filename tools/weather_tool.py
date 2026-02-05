import requests


GEOCODING_API_URL = "https://geocoding-api.open-meteo.com/v1/search"


WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"


def get_weather(city: str):
    

    geo_params = {
        "name": city,
        "count": 1
    }

    geo_response = requests.get(GEOCODING_API_URL, params=geo_params)
    geo_response.raise_for_status()

    geo_data = geo_response.json()
    results = geo_data.get("results")

    if not results:
        raise ValueError(f"City '{city}' not found")

    latitude = results[0].get("latitude")
    longitude = results[0].get("longitude")

    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }

    weather_response = requests.get(WEATHER_API_URL, params=weather_params)
    weather_response.raise_for_status()

    weather_data = weather_response.json()
    current_weather = weather_data.get("current_weather", {})


    weather_info = {
        "city": city,
        "temperature_celsius": current_weather.get("temperature"),
        "windspeed_kmh": current_weather.get("windspeed"),
        "weather_code": current_weather.get("weathercode")
    }

    return weather_info

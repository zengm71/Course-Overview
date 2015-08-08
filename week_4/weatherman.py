# weatherman.py
# 
# Provides the current forecast for the weather in Berkeley, California

from urllib.request import urlopen
import json

def get_report():
    """
    Returns the current forecast of Berkeley right now
    """
    response = urlopen(
        'http://api.openweathermap.org/data/2.5/weather?q=Berkeley,ca')
    rawWeatherData = response.read().decode("utf-8")
    weatherData = json.loads(rawWeatherData)

    forecast = "Berkeley, CA Forecast: " + weatherData["weather"][0]["main"]
    return forecast
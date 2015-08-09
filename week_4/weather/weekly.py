# weekly.py
# 
# Provides the weather for Berkeley, CA for the week

from urllib.request import urlopen
import json

def forecast():
    """
    Returns the daily weather for Berkeley, CA
    """
    response = urlopen('http://api.openweathermap.org/data/2.5/forecast/daily?q=Berkeley&mode=json&units=Imperial&cnt=7')
    rawWeatherData = response.read().decode("utf-8")
    weatherData = json.loads(rawWeatherData)

    forecastStr = ""
    for i in range(7):
        forecastStr += _daily_forecast(weatherData, i) + "\n\n"

    forecastStr = forecastStr[:-2] # Remove the two newlines at the end 
    return forecastStr


def _daily_forecast(weatherData,index):
    """
    Helper function that prints a single day's forecast
    """

    forecastStr = "Forecast for Berkeley, CA: " + weatherData["list"][index]["weather"][0]["main"] + "\n" \
    "Current Temp: " + str(weatherData["list"][index]["temp"]["day"]) + " degrees \n"  \
    "High Temp: " + str(weatherData["list"][index]["temp"]["max"]) + " degrees \n" \
    "Low Temp: " + str(weatherData["list"][index]["temp"]["min"]) + " degrees"

    return forecastStr
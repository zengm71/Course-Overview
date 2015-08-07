from urllib.request import urlopen
import json

def get_report():
    response = urlopen('http://api.openweathermap.org/data/2.5/weather?q=Berkeley,ca')
    rawWeatherData = response.read().decode("utf-8")
    weatherData = json.loads(rawWeatherData)
    return weatherData["weather"][0]["main"]
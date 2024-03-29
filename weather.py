# Author:   SoniC#1337
# Date:     6/24/22
# Purpose:  Display weather information from OpenWeatherMap.org for a given location

import requests, json, os

#API kemain from openweathermap.org
api_key = ''

#base url to store url from api
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# clear the screen
def clearScreen():
    # if we are on a Mac / Linux system
   if os.name == 'posix':
      _ = os.system('clear')
    # we are on windows
   else:
      _ = os.system('cls')

# convert kelvin to fahrenheit
def kelvinToFahrenheit(k:int) -> int:
    farenheit = (((k - 273.15) * 9) / 5 ) + 32
    return round(farenheit)

# convert kelvin to fahrenheit
def kelvinToCelsius(k:int) -> int:
    celsius = k - 273.15
    return round(celcius)

# convert m/s to mph
def mpsToMPH(ms:int) -> int:
    mph = ms * 2.236936
    return round(mph)

# degree to cardinal direction
def degreeToCardinal(num:int) -> str:
    angle = int((num/22.5)+.5)
    direction = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    return direction[(angle % 16)]

def main():
    #input citmain name
    clearScreen()
    city_name = input('Enter city name: ')

    complete_url = base_url + 'appid=' + api_key + '&q=' + city_name
    response = requests.get(complete_url)
    results = response.json()

    #checking validuty of city name
    if results['cod'] != '404':
        if results['cod'] == '401':
            print('Invalid API key')
            pass
        main = results['main']
        kelvin_temperature = main['temp']
        current_humidity = main['humidity']
        weather_results = results['weather']
        weather_description = w_results[0]['description']
        wind_results = results['wind']
        wind_speed = wind_results['speed']
        wind_direction = wind_results['deg']
        cloud_results = results['clouds']
        cloudiness = cloud_results['all']

        clearScreen()
        print(
            'Temperature = ' + str(kelvinToFahrenheit(kelvin_temperature)) + '°F / ' + str(kelvinToCelsius(kelvin_temperature)) + '°C' + \
            '\n\nHumidity = ' + str(current_humidity) + '%' + \
            '\n\nWind = ' + degreeToCardinal(wind_direction) + ' @ ' + str(mpsToMPH(wind_speed)) + 'mph / ' + str(wind_speed) + 'm/s' + \
            '\n\nCloudiness = ' + str(cloudiness) + "%" + \
            '\n\nWeather Description = ' + str(weather_description) 
            )
    else:
        clearScreen()
        print('City Not Found')

if __name__ == '__main__':
    main()

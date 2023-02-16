import requests

#Allows Fetched Data to be readable and "pretty" in format
from pprint import pprint

API_Key = 'Insert your API Key here' #Go to OpenWeather's Website to access the free API's that they provide! Go to the README file for the link to OpenWeather's Website.

City = input("Enter any city: ")

url = "https://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" + City

weather_data = requests.get(url).json()

pprint(weather_data)

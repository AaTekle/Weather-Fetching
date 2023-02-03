import requests

#Allows Fetched Data to be readable and "pretty" in format
from pprint import pprint

API_Key = '905cff5fdb5814434f5e47644cfd5476'

City = input("Enter any city: ")

URL = "https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={API key}" + API_Key + "&q=" + City

weather_data = requests.get(URL).json()

pprint(weather_data)

import requests

#Allows Fetched Data to be readable and "pretty" in format
from pprint import pprint

API_Key = '905cff5fdb5814434f5e47644cfd5476'

City = input("Enter any city: ")

url = "https://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" + City

weather_data = requests.get(url).json()

pprint(weather_data)

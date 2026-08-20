import requests
from dotenv import load_dotenv
import os

load_dotenv()
APPID = os.environ.get("APPID")

weather_parameters = {
    "appid": APPID,
    "lat": 54.896870,
    "lon": 23.892429,
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=weather_parameters)
response.raise_for_status()

weather_data = response.json()
for weather in weather_data["list"]:
    if weather["weather"][0]["id"] < 700:
        print("Bring an umbrella!")
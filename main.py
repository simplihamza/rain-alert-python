import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
APPID = os.environ.get("APPID")
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
trial_number = os.environ.get("TWILIO_TRIAL_NUMBER")
receiver_number = os.environ.get("RECEIVER_NUMBER")

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
    condition_code = weather["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

client = Client(account_sid, auth_token)

if will_rain:
    message = client.messages.create(
        to=receiver_number,
        from_=trial_number,
        body="️sms_event_notifications",
    )

print(message.status)
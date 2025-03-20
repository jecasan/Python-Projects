import requests
import os
from twilio.rest import Client

account_sid = "AC9f7f453fb25207dee42d88274cbab8b1"
auth_token = os.environ.get("AUTH_TOKEN")


api_key = os.environ.get("OWM_API_KEY")
endpoint = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat" : 14.602400,
    "lon" : 121.013489,
    "appid" : api_key,
    "cnt" : 4,
}

response = requests.get(url=endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)
will_rain = False
for _ in range(0,4):
    if weather_data["list"][_]["weather"][0]["id"] < 700:
        will_rain = True
        
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="+19036665293",
        body="It's going to rain today. Bring an umbrella.",
        to=os.environ.get("MOBILE_NUMBER")
    )
    print(message.status)



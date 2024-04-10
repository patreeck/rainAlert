import os
import requests
from twilio.rest import Client

DUBLIN_LAT = 53.349804
DUBLIN_LONG = -6.260310

# RAINING_LAT = 34.327690
# RAINING_LONG = 47.077766

api_key = os.environ.get("OWN_API_KEY")  # set_env variable
# twilio.com
account_sid = "ACb8a52d107c596f2d3b7b4780c250025a"
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)
param = {
    "lat": DUBLIN_LAT,
    "lon": DUBLIN_LONG,
    "appid": api_key,
    "cnt": 4
}

res = requests.get(url='https://api.openweathermap.org/data/2.5/forecast', params=param)
res.raise_for_status()

weather_data = res.json()
print(weather_data)


def check_if_its_raining():
    for weather_details in weather_data['list']:
        if int(weather_details["weather"][0]["id"]) < 700:
            return True
        else:
            return False


if check_if_its_raining():
    message = client.messages \
        .create(
        body="It is going to Rain🌧️ please bring Umbrella ☂️, Thank you. Pratik Gadkar 😊",
        from_='+12513201209',
        to='+353892030026')
    # print(message.status)
else:
    print("Its not going to Rain, have fun !")

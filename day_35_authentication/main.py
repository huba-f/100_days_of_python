import requests
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

api_key = "7654fbe02a9bf55f07a710dda42e5fe4"
twilio_account_sid = "ACaabfffdbce4d6cb8426d1988720c0b88"
twilio_auth_token = "caaec60861d85ab8ec07e7bd99c848f2"

client = Client(twilio_account_sid, twilio_auth_token)

weather_params = {
    "lat": 46.744740,
    "lon": 25.534439,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}

data = requests.get(OWM_ENDPOINT, params=weather_params)
data.raise_for_status()
weather_data = data.json()["hourly"]
will_snow = False
will_rain = False

for x in weather_data[0:13]:
    if 700 > int(x["weather"][0]["id"]) > 599:
        will_snow = True
    elif int(x["weather"][0]["id"]) < 700:
        will_rain = True

if will_snow:
    message = client.messages \
        .create(
        body="Today there will be snow!",
        from_='+12674891940',
        to='+0757797751'
    )
    print(message.status)
elif will_rain:
    message = client.messages \
        .create(
        body="Today there will be rain!",
        from_='+12674891940',
        to='+400757797751'
    )
    print(message.status)

import requests
from twilio.rest import Client

account_sid = 'AC04e80cbe6c70bc3159620ffed92419b6'
auth_token = 'b9bcfbd8e82becfe54fecace9ba29c5f'
API_KEY = "a6a2e1bb38ff85972009c1160f951797"
LAT = 30.73
LON = 76.77
LAT1 = 53.45
LON1 = 33.29

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
}
response = requests.get("https://api.openweathermap.org/data/2.5/weather", parameters).json()
weather_data = response['weather'][0]['main']

if weather_data == 'Rain':
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='+14132484122',
    body='Bring an umbrella ☂️',
    to='+918146806068'
    )

    print(message.sid)



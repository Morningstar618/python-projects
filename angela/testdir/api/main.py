import requests
from datetime import datetime


##################### ISS SPACE STATION API ###############################

# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# data = response.json()

# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
# iss_position = (latitude, longitude)

# print(iss_position)


############################ SUNRISE-SUNSET API #############################

MY_LAT = 30.733315
MY_LONG = 76.779419

parameters = {     # Required parameters for Sunrise-Sunset API 
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset_hour = sunset.split("T")[1].split(":")[0]
print(sunrise_hour)
print(sunset_hour)

time_now_hour = datetime.now().hour
print(time_now_hour)

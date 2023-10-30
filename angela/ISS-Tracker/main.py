import requests
from datetime import datetime
import smtplib
from time import sleep

MY_LAT = 30.733315 # Your latitude
MY_LONG = 76.779419 # Your longitude

EMAIL = "yellow618light@gmail.com"
PASSWORD = "dgeavqxnocssktqr"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now_hour = datetime.utcnow().hour

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

lat_diff = MY_LAT - iss_latitude
lon_diff = MY_LONG - iss_longitude

iss_sky = False

if ((-5<lat_diff<5) and (-5<lon_diff<5)) and (time_now_hour<sunrise or time_now_hour>sunset):
    iss_sky = True

while iss_sky:
    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=EMAIL, password=PASSWORD)
        conn.sendmail(from_addr=EMAIL, to_addrs="ayush618officer@gmail.com", msg="Subject:Look at the Sky!\n\nISS is going through your location.")
    if (-5<lat_diff<5) and (-5<lon_diff<5):
        sleep(60)
    else:
        iss_sky = False



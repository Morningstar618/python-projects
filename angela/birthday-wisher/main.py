import datetime as dt
import pandas
import random
import smtplib

EMAIL = "yellow618light@gmail.com"
PASSWORD = "dgeavqxnocssktqr"

birthdays = pandas.read_csv('birthdays.csv').to_dict(orient='records')
is_birthday = [birthday for birthday in birthdays if birthday['day'] == dt.datetime.now().day if birthday['month'] == dt.datetime.now().month]


for birthday in is_birthday:
    with open("letter_templates/letter_{}.txt".format(random.randint(1, 3))) as data:
        letter = data.read().replace("[NAME]", birthday['name'])
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user=EMAIL, password=PASSWORD)
            conn.sendmail(from_addr=EMAIL, to_addrs=birthday['email'], msg="Subject:Happy Birthday {}!\n\n{}".format(birthday['name'], letter))






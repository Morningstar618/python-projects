import smtplib
import datetime as dt
import random


my_email = "yellow618light@gmail.com"
password = "dgeavqxnocssktqr"

day_of_week = dt.datetime.now().weekday()

if day_of_week == 6:
    with open('quotes.txt') as data:
        quotes = data.readlines()
        quote = random.choice(quotes)
                
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)

            connection.sendmail(from_addr=my_email, to_addrs="ayush618officer@gmail.com", msg="Subject:Motivational quotes\n\n{}".format(quote))

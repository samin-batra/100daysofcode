import smtplib
from datetime import datetime as dt
import random

my_email = "doejohnny160@gmail.com"
password = ""

with open("quotes.txt","r") as f:
    quotes = f.readlines()

quote_of_the_day = random.choice(quotes)
curr_date = dt.now()
curr_day = curr_date.weekday()
print(curr_day)
if curr_day == 0:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user = my_email, password = password)
    connection.sendmail(from_addr=my_email, to_addrs="samin_rooney@yahoo.co.in", msg = f"Subject:Quote of the day \n\n  {quote_of_the_day}")
    connection.close()
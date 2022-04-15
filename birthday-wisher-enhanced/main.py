##################### Extra Hard Starting Project ######################

import pandas as pd
import smtplib
from datetime import datetime
import random

FROM_ADDRESS = "doejohnny160@gmail.com"
FROM_PASS = "Hello@123"

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
bdays = pd.read_csv("birthdays.csv")
# birthdays_as_dict = bdays.to_dict(orient="records")
print(bdays)
today = datetime.now()
date_today = today.day
month_today = today.month
# print(date_today)
# print(month_today)
# print(bdays['month']==month_today)
birthdays_today = bdays[(bdays['month'] == month_today) & (bdays['day'] == date_today)]
print(birthdays_today)
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
for index, row in birthdays_today.iterrows():
    print(row['email'])
    print(row['name'])
    letter = random.randint(1, 3)
    try:
        with open(f"letter_templates/letter_{letter}.txt", "r") as f:
            contents = f.read()
            contents = contents.replace("[NAME]", row['name'])
        connection = smtplib.SMTP(host="smtp.gmail.com")
        connection.starttls()
        connection.login(user=FROM_ADDRESS, password=FROM_PASS)
        connection.sendmail(from_addr=FROM_ADDRESS, to_addrs=row['email'],
                            msg=f"Subject: Happy Birthday! \n\n {contents}")
    except:
        print("File doesn't exist")
# 4. Send the letter generated in step 3 to that person's email address.

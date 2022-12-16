import pandas as pd
from datetime import datetime 
import random
import smtplib

my_email = "@gmail.com"
password = ""

now = datetime.now()
today = (now.month, now.day)

df = pd.read_csv('birthdays.csv')
birthdays_dict = {
    (data_row['month'], data_row['day']) : data_row
      for (index, data_row) in df.iterrows() }

if today in birthdays_dict:
    name = birthdays_dict[today]['name']
    email = birthdays_dict[today]['email']
    
    number = random.randint(1,3)
    
    with open(f'letter_templates/letter_{number}.txt', 'r') as f:
        content = f.read()
        content = content.replace('[NAME]', name)
        print(content)

   
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user = my_email, password = password )
        connection.sendmail(
            from_addr = my_email,         
            to_addrs = email,
            msg = f"Subject:Happy Birthday\n\n{content}")








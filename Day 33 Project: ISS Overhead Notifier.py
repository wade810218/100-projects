import requests
from datetime import datetime
import time
import smtplib

My_EMAIL = ""
My_PASSWORD = ""

MY_LAT = 22.620550 
MY_LONG = 120.312050 

def iss_overhead_check():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    lat = abs(MY_LAT - iss_latitude) <= 5
    long = abs(MY_LONG - iss_longitude) <= 5
    
    return lat & long
   
def dark_check():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    
    response = requests.get("https://api.sunrise-sunset.org/json",     
                            params=parameters)
    response.raise_for_status()
    data = response.json()
    
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    
    time_now = datetime.now()

    sunrise_local = (sunrise + 8) % 24
    sunset_local = (sunset + 8) % 24
    hour_now = time_now.hour
    
    return not (sunrise_local <= hour_now <= sunset_local)
    

while True:
    time.sleep(60)
    
    if iss_overhead_check() & dark_check():
        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user = My_EMAIL, password = My_PASSWORD )
            connection.sendmail(
                from_addr = My_EMAIL,         
                to_addrs = My_EMAIL,
                msg = f"Subject:ISS Overhead Notifier\n\nJust look up")
    



import requests
import smtplib
import time
from datetime import datetime

MY_LAT = 14.599512
MY_LONG = 120.984222
MY_EMAIL = [your_email]
PASSWORD = [your_app_password]
"""
To test code use TEST parameters:
    Change loc[0] with TEST_LAT and loc[1] with TEST_LONG
    Change hour_now with TEST_HOUR
"""
TEST_LAT = 14
TEST_LONG = 120
TEST_HOUR = 24

def main():
    loc = get_loc()
    close = is_close(loc[0], loc[1])
    dark = get_time()
    while True:
        time.sleep(60)
        if dark is True and close is True:
            send_email()
    
def get_loc():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()

    data = iss_response.json()
    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])
    return latitude, longitude

def is_close(latitude, longitude):
    if  latitude - 5 < MY_LAT < latitude + 5 and longitude - 5 < MY_LONG < longitude + 5:
        return True
    else:
        return False

def get_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0, 
    }

    sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    sun_response.raise_for_status()
    sun_data = sun_response.json()
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])
    
    time_now = datetime.now()
    hour_now = time_now.hour
    
    return is_dark(sunrise, sunset, hour_now)

def is_dark(sunrise, sunset, hour_now): 
    if hour_now > sunset or hour_now < sunrise:
        return True
    else:
        return False
       
def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, 
                            to_addrs=MY_EMAIL, 
                            msg=f"Subject:Look Up!\n\nLook Up! The ISS is above you in the sky.".encode("windows-1252")
        )
    
if __name__ == "__main__":
    main()

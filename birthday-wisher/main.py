import pandas as pd
import datetime as dt
import smtplib
import random as rd

MY_EMAIL = "jerickpython@gmail.com"
PASSWORD = #yourpassword

def main():
    month, day = get_date()
    bday_dict = birthday_data()
    check_day(month, day, bday_dict)
#------------Get Date------------#
def get_date():
    now = dt.datetime.now()
    return now.month, now.day
#------------Read CSV------------#
def birthday_data():
    data = pd.read_csv("birthdays.csv")
    bday_dict = data.to_dict(orient="records")
    return bday_dict
#------------Pick Letter------------#
def pick_template(name):
    rand_num = rd.randint(1, 10)
    with open(f"letter_templates/letter_{rand_num}.txt") as file:
        letter = file.read()
        message = letter.replace("[NAME]", name)
        return message
#------------Check Day------------#
def check_day(month, day, dict):   
    for date in dict:
        message = pick_template(date["name"])
        send_email(date["email"], message)
#------------Send Email------------#
def send_email(email, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, 
                            to_addrs=email, 
                            msg=f"Subject:Happy Birthday\n\n{message}".encode("windows-1252")
        )
        

if __name__ == "__main__":
    main()

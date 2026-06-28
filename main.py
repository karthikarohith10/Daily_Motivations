import smtplib
import random

with open("quotes.txt") as file:
    new_list = file.readlines()
    random_quote = random.choice(new_list)

my_email = ""
password = ""

with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs="karthimadathil@gmail.com",msg=f"Subject: Daily Motivation from Rohith\n\n{random_quote}\n\n This is an automated email. Kindly do not reply !")



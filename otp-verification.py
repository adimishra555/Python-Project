
import math
import random
import smtplib
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to generate OTP
def generate_otp(length=6):
    digits = "0123456789"
    return ''.join(random.choice(digits) for i in range(length))

# Email sender details
sender_email = "amishra37200@gmail.com"
app_password = "gewz quro oegd jueg"  

# Generate OTP
OTP = generate_otp()
otp_message = f"{OTP} is your OTP."

# Get recipient email
recipient_email = input("Enter your email: ")

# Create email message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = recipient_email
msg["Subject"] = "Your OTP Verification Code"
msg.attach(MIMEText(otp_message, "plain"))

try:
    # Setup SMTP connection
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)
    
    # Send email
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()
    
    print("OTP sent successfully!")
    
    # Verify OTP
    user_otp = input("Enter Your OTP >>: ")
    if user_otp == OTP:
        print("Verified ✅")
    else:
        print("Incorrect OTP. Please try again ❌")

except smtplib.SMTPAuthenticationError:
    print("Authentication error! Please check  App Password settings.")
except Exception as e:
    print(f" Error : {e}")
















































# import os
# import math
# import random
# import smtplib


# digits="0123456789"
# OTP=""
# for i in range(6):
#     OTP+=digits[math.floor(random.random()*10)]
# otp = OTP + " is your OTP"
# msg= otp

# s = smtplib.SMTP('smtp.gmail.com', 587)
# s.starttls()
# s.login("Your Gmail Account", "You app password")
# emailid = input("Enter your email: ")
# s.sendmail('&&&&&&&&&&&',emailid,msg)
# a = input("Enter Your OTP >>: ")
# if a == OTP:
#     print("Verified")
# else:
#     print("Please Check your OTP again")

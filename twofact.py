import random

# Stored username and password
stored_username = "admin"
stored_password = "admin123"

# Read login credentials
username = input("Enter Username: ")
password = input("Enter Password: ")

# Verify password
if username == stored_username and password == stored_password:

    print("Password Verified.")

    # Generate a random 6-digit OTP
    otp = random.randint(100000, 999999)

    print("Generated OTP:", otp)

    # Read OTP from user
    user_otp = int(input("Enter OTP: "))

    # Verify OTP
    if user_otp == otp:
        print("Two-Factor Authentication Successful!")
    else:
        print("Invalid OTP.")

else:
    print("Invalid Username or Password.")
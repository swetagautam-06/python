# Stored username and password
stored_username = "admin"
stored_password = "admin123"

# Read user credentials
username = input("Enter Username: ")
password = input("Enter Password: ")

# Verify username and password
if username == stored_username and password == stored_password:
    print("Login Successful!")
else:
    print("Invalid Username or Password.")
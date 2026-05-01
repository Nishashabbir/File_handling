

# Project: Smart Login Logger
#  What it does

# This program:

# asks user for username & password
# checks if login is correct
# logs every attempt (success or failure) into a file
# saves time + message for each event

#  Basically: a mini authentication system with logging

# from datetime import datetime

# USER_DATA={
#     "nisha" : "1234",
#     "admin" : "587943"
# }



# def loggin():
#     while True:
#         username=input("Enter your username : ")
#         password= input("Enter password: ")
#         if username in USER_DATA and USER_DATA[username]==password:
#             with open("test.txt" , "a") as f:
#                 f.write(f"the user logged in successfully at {datetime.now()}\n")
#                 print("Login successful! ")
#                 break
#         else:
#             with open("test.txt" , "a") as f:
#                 f.write(f"The user attempted to log in at : {datetime.now()}\n")
#             print("Wrong credentials , Try again !")

# loggin()       

# second version 

from datetime import datetime
import getpass

# fake database (for demo)
USER_DATA = {
    "nisha": "1234",
    "admin": "admin123"
}

def log(message):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {message}\n")

def login():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ") #we imported getpass to use getpass method , this method hides the password input 

    if username in USER_DATA and USER_DATA[username] == password:
        print("Login successful ")
        log(f"SUCCESS: {username} logged in")
    else:
        print("Login failed ")
        log(f"FAILED: login attempt for username '{username}'")

# run program
login()







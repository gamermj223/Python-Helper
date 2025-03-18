import time
import random

username = "You"
ai_name = "Bob"
when_sending_message = ": "
active = True
user_asked_exit = False

def exit():
    global user_asked_exit
    if user == "exit":
        user_asked_exit = True
        print(ai_name+when_sending_message+"Are you sure?")
    
    if user_asked_exit == True:
        active = False

while active == True:

    user = input(username+when_sending_message)

    exit()
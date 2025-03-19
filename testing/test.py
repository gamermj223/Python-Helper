import time
import random
from greettings import greets

username = "You"
ai_name = "Bob"
when_sending_message = ": "
user_asked_exit = False
running = True
greeted = False

def greeting():
    
    global greeted, greets

    if greeted == False:
        greetss = random.choice(greets['ai']) #if this if statement is called more than once a error will happened, but it will only ever be called once so. yaaaaaaaa.
        print(greetss)
        greeted = True
        
def exitr():
    global user_asked_exit, running
    if user == "exit":
        user_asked_exit = True
        print(ai_name+when_sending_message+"Are you sure?")
    
    if user_asked_exit == True:
        running = False
        
while running:
    user = input("You: ")

    greeting()
    exitr()
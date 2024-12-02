import time
import random
from greettings import greets

running = True
greeted = False

def greeting():
    
    global greeted, greets

    if greeted == False:
        greets = random.choice(greets['ai']) #if this if statement is called more than once a error will happened, but it will only ever be called once so. yaaaaaaaa.
        print(greets)

        
while running:

    greeting()

    user = input("You: ")


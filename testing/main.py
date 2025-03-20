import commands
import random

running = True
greeted = False
user = ""

def get_commands():

    global greeted
    
    greeting = commands.ai_greeting_first() #if greeted is returned with True it will send a welcoem message.
    greeted = commands.greeted_true() #revices if greeted is True/False.
    
    print(greeting) #this prints the welocme greeting.

while running:
    
    get_commands()

    user = input("You: ").lower()
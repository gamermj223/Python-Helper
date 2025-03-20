from words import greetings
import random

sent = False
greeted = False

def greeted_true():
    return greeted

def ai_greeting_first():
    global sent, greeted

    greets = random.choice(greetings['greeting'])

    send = random.randint(1,2)

    if send == 1 and not sent:
        sent = True
        greeted = True
        greeted_true() #this sends the greeted var
        return greets #this sends the welcome message.

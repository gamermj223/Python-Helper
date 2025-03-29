import words
import random
import time
import datetime
import sys
import pyttsx3

ai_name = "PyBuddy"
ai_cou = ": "
user = ""
ai_print = ai_name + ai_cou

now = datetime.datetime.now()

greeted_first = False
greeted_first_second = False
sent = False
send_first_greet = random.randint(2,2)
greeting_done = False

def speek(chatbot):
    engine = pyttsx3.init()

    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)

    engine.say(chatbot)

    engine.runAndWait()

def user_greeting_first(user):
    global sent, greeted_first, send_first_greet, greeted_first_second

    if send_first_greet == 2 and sent == False and greeted_first_second == True:
        if user in words.greetings["user_waking_up_bot"]:
            print(ai_print + random.choice(words.greetings["bot_waking_up"]))
            chatbot = random.choice(words.greetings["bot_waking_up"])
            speek(chatbot)
            sent = True

def greeting_responded(user):
    global greeted_first, greeting_done   # Access the global variable

    if sent == True and greeting_done == False and user in words.greetings["user_responding_words_good"]:
        print(ai_print+ random.choice(words.greetings["ai_responed"]))  # Respond randomly
        greeting_done = True

def ai_greeting_first():
    global sent, greeted_first, send_first_greet, greeted_first_second

    if send_first_greet == 1 and not sent:
        send_first_greet = True
        sent = True
        print(ai_print + random.choice(words.greetings['greeting']))
    elif send_first_greet == 2:
        greeted_first_second = True

def tell_time(user):
    global greeting_done, now
    if greeting_done == True and user in "time" and user in words.comands["time"]:
        print(ai_print + "The time is " + now.strftime("%H:%M"))
    elif greeting_done == True and user in "time":
        print(ai_print + "The time is " + now.strftime("%H:%M"))

def exit(user):

    if user == "exit":
        print("exiting")
        print(ai_print + "exiting the program")
        sys.exit()


def times(user):
    pass
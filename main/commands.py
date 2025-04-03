import words
import random
import time
from datetime import datetime
import sys
import pyttsx3
<<<<<<< HEAD
=======
import re
>>>>>>> db0ee3e7035b0185bfed887265e89bdb94d0d109

ai_name = "PyBuddy"
ai_cou = ": "
user = ""
ai_print = ai_name + ai_cou

greeted_first = False
greeted_first_second = False
sent = False
greeting_done = False
send_first_greet = random.randint(1,2)

def speek(chatbot):
    engine = pyttsx3.init()

    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)

    engine.say(chatbot)

    engine.runAndWait()

def user_greeting_first(user):
    global sent, greeted_first, send_first_greet, greeted_first_second

    if send_first_greet == 2 and sent == False and greeted_first_second == True:
        if any(word in user.lower() for word in words.greetings["user_waking_up_bot"]):
            chatbot = random.choice(words.greetings["bot_waking_up"])
            print(ai_print + chatbot)
            speek(chatbot)
            sent = True

def greeting_responded(user):
    global greeted_first, greeting_done   # Access the global variable

    if sent == True and greeting_done == False and any(word in user.lower() for word in words.greetings["user_responding_words_good"]):
        chatbot = random.choice(words.greetings["ai_responed"])
        print(ai_print + chatbot)  # Respond randomly  
        speek(chatbot)

        greeting_done = True

def ai_greeting_first():
    global sent, greeted_first, send_first_greet, greeted_first_second

    if send_first_greet == 1 and not sent:
        send_first_greet = True
        sent = True
        chatbot = random.choice(words.greetings['greeting'])
        print(ai_print + chatbot)
        speek(chatbot)
    elif send_first_greet == 2:
        greeted_first_second = True

def tell_time(user):
    global greeting_done
    if greeting_done == True and any(word in user.lower() for word in words.comands["time"]):
        current = datetime.now().strftime("%I:%M %p")
        if any(word in user.lower() for word in words.comands["time_respond_words1"]):
            chatbot = random.choice(words.comands["time_respond1"]) + " the time is " + current
            print(ai_print + chatbot)
            speek(chatbot)
        else:
            chatbot = "The time is " + current
            print(ai_print + chatbot)
            speek(chatbot)

def skip(user):
    global greeted_first, greeted_first_second, sent, greeting_done
    if user == "skip":
        greeted_first = True
        greeted_first_second = True
        sent = True
        greeting_done = True


def exit(user):

    if user == "exit":
        print("exiting")
        print(ai_print + "exiting the program")
        sys.exit()


def math(user):
    if any(word in user.lower() for word in words.comands["math"]):
        if any(word in user.lower() for word in "time"):
            a, b = re.findall(r'-?\d+\.?\d*', user)
            a, b = [float(num) for num in [a,b]]

            print(a,b)
            print(a*b)
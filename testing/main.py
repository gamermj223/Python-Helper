import commands
import random
import words

running = True
greeted = False
user_greeting_back = False
ai_name = "PyBuddy"
ai_cou = ": "
user = ""

def greeting_responded():
    global greeted, user   # Access the global variable

    if greeted and user in words.greetings["user_responding_words_good"]:
        print(ai_name + ai_cou + random.choice(words.greetings["ai_responed"]))  # Respond randomly



def get_commands():

    global greeted
    
    greeting = commands.ai_greeting_first() #if greeted is returned with True it will send a welcoem message.
    
    if greeted == False:
        print(ai_name + ai_cou + greeting) #this prints the welocme greeting.
        greeted = commands.greeted_true() #revices if greeted is True/False.
    
while running:
    
    get_commands()
    greeting_responded()

    user = input("You: ").lower()
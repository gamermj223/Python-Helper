import commands
import random
import words

running = True
user_greeting_back = False
ai_name = "PyBuddy"
ai_cou = ": "
user = ""

running1 = True

while running:
    
    commands.ai_greeting_first()


    user = input("You: ").lower()

    commands.greeting_responded(user)
    commands.user_greeting_first(user)
    commands.tell_time(user)
    commands.exit(user)
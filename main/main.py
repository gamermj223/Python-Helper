import commands
import random
import words
import speech_recognition as sr

recognizer = sr.Recognizer()

running = True
user_greeting_back = False
ai_name = "PyBuddy"
ai_cou = ": "
user = ""

running1 = True

t = 2

while running:
    
    commands.ai_greeting_first()

    if t == 2:
        user = input("You: ")
    elif t == 1:

        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = recognizer.listen(source, timeout=1, phrase_time_limit=2)
            user = recognizer.recognize_google(audio)

        try:
            # Now it should work because 'source' is within the 'with' block
            print("You said: " + user)
        except sr.WaitTimeoutError:
            print("No speech detected in time.")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print("Error with the Speech API; {0}".format(e))

    commands.greeting_responded(user)
    commands.user_greeting_first(user)
    commands.tell_time(user)
    commands.exit(user)
    commands.math(user)
    commands.skip(user)
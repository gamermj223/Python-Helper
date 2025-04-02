import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Open the audio file
with sr.Microphone() as source:
    # Record the audio data
    audio_data = recognizer.record(source)

    try:
        # Recognize the speech
        text = recognizer.recognize_google(audio_data)
        print("Recognized speech: ", text)
    except sr.UnknownValueError:
        print("Speech recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from service; {e}")
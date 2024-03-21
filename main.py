import pyttsx3
import speech_recognition as sr

# Mark Anthony D. Ramos
# BSIT-2

def talk(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

listener = sr.Recognizer()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "jacob" in command:
                if "cat noise" in command: # Hey Jacob, can you make cat noise?
                    response = "I don't know but... let me try....! Meow! Meow!.... Did it work?"
                elif "friends" in command: # Hey Jacob, do you have friends?
                    response = "I do have friends who are also AI. They are Siri, Bard, and Alexa"
                elif "artist" in command: # Hey Jacob, do you know any artist?
                    response = "I do know few artists. Mostly I know Taylor Swift. I am such a big fan"
                else:
                    response = "Sorry, I didn't catch that. Can you repeat?"

                print(response)
                talk(response)
    except:
        pass
        command = "No Mic"
        print(command)

take_command()

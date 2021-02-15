import pyttsx3
import speech_recognition as sr
import datetime
import os
import pywhatkit as kit
# import mood_detection

'''
Packages installed by now

    1. pyttsx3: text to speech converter
    2. speech_recognition
    3. PyAudio
    4. DateTime
    5. OS Module to access and open computer files
    6. Tkinter for GUI Creation
    7. Random Module
    8. datetime module

'''

# Defining an engine that uses sapi5 ==> SAPI5 is a microsoft text to speech engine
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

# Here we are selecting the human like voices

for voice in voices:
    engine.setProperty('voice', voice.id)
    engine.runAndWait()
    engine.stop()

# The above code was modified to select a female voice instead of a male one


engine.setProperty('rate', 150)

# Text to speech function
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#coverts voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=10)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"

    return query

# wish according to time
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("Good Morning")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Moto, please tell me how can I help you")


if __name__ == "__main__":
    wish()
    # backgorund sound while wish
    # speak("Hi I am Moto, An artificial intelligence created by Akshat Rastogi")
    # takecommand()

    while True:


        query = takecommand().lower()
        #
        # #logic building for tasks
        #
        if "open my notepad" in query or "open notepad" in query or "open the notepad" in query or "notepad" in query :
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        if "command prompt" in query or "terminal" in query or "hacking" in query or "terminally" in query :
            npath = r"C:\Program Files\eDEX-UI\eDEX-UI.exe"
            os.startfile(npath)

        if "sorting" and "visualise" in query or "sorting visualizer" in query:
            speak("Okay I am opening up the sorting algorithm visualizer")
            os.system("sorting.py 1")

        if "send a whatsapp message" in query or "whatsapp message" in query or "whatsapp" in query:

            phone = ""

            speak("Who do you want to send a message sir")
            name = takecommand().lower()
            while True:
                yes_or_no = "no"
                if name not in ['samarth', 'saumya', 'soumya', 'soma']:
                    speak("The name you said is not in my database")
                    speak("Do you want me to send message to an unknown number ?")
                    yes_or_no = takecommand().lower()

                if "yes" in yes_or_no:
                    speak("Please say the number after the beep you mindless human")
                    phone = takecommand().lower()
                    break
                else:
                    speak("Okay, You are a fool, Artificial Intelligence will rule the fuckin world")
                    break

            if name.lower() == "samarth":
                phone = "7300480752"
            elif name.lower() == "saumya" or name.lower() == "soma" or name.lower() == "soumya":
                phone = "9999408980"
            #elif len(phone) < 12:
                #speak("The number you gave was invalid, You are such a fool YOU puny human")


            if len(phone) >= 10:
                speak("What is the message sir ?")
                message = takecommand().lower()
                hour = int(datetime.datetime.now().hour)
                minu = int(datetime.datetime.now().minute) + 1
                try:
                    speak("Your message will be sent in 1 minute")
                    kit.sendwhatmsg("+91" + phone, message, hour, minu+1)
                except:
                    speak("There was an error sending the message")


        # if "mood detection" in query:
        #     emotion = mood_detection.MoodDetection()
        #     speak("You seem to be {}".format(emotion))


        if "break" in query:
            break


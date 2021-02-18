import pyautogui as pag
import time
import pyttsx3
import speech_recognition as sr

pag.FAILSAFE = False

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

# Here we are selecting the human like voices



def speak(audio):
    engine.setProperty('rate', 160)
    for voice in voices:
        engine.setProperty('voice', voice.id)
        engine.runAndWait()
        engine.stop()
    f = open('text_to_print.txt', 'w')
    f.write(audio)
    f.close()
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand_sleep():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=100000000000000000)
    try:
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        return "none"
    return query


def alwaysActive():
    while True:
        for i in range(0,100):
            pag.moveTo(0, i*5)
        for i in range(3):
            pag.press('shift')

        query_lol = takecommand_sleep()
        if 'stop' in query_lol or 'inactive' in query_lol:
            speak("I am inactivating always on display")
            break
        else:
            time.sleep(15)

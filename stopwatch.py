import time
import os
import pyttsx3
import speech_recognition as sr

def Stop_Watch():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0])
    engine.setProperty('rate', 180)

    def speak(audio):
        engine.say(audio)
        print(audio)
        engine.runAndWait()

    def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=5, phrase_time_limit=1000000000000000000)
        try:
          print("Recognizing...")
          query = r.recognize_google(audio, language='en-in')
        except:
          return takecommand()

        return query

    speak("Speak Start or Stop to operate the stopwatch")

    query = ""
    while 'start' not in query:
      query = takecommand()

    speak("Stop Watch Started")

    if 'start' in query:
      start_time = time.time()


    query1 = ""
    while 'stop' not in query1:
      query1 = takecommand()

    if 'stop' in query1:
      end_time = time.time()


    def time_convert(sec):
      mins = sec // 60
      sec = sec % 60
      hours = mins // 60
      mins = mins % 60
      speak("Stopwatch Ended")
      speak("Time Elapsed was {0} hours {1} minutes and {2} seconds".format(int(hours),int(mins),int(sec)))
      print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))


    time_lapsed = end_time - start_time
    time_convert(time_lapsed)

    return
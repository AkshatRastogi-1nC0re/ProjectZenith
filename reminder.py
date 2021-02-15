import time
import os
import pyttsx3
import speech_recognition as sr
from datetime import datetime

def Remind():

    time.sleep(10)

    # 25 seconds buffer time
    start_time = time.time()
    listA = []

    engine = pyttsx3.init('sapi5')

    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[0])

    engine.setProperty('rate', 160)

    def speak(audio):
        engine.say(audio)
        print(audio)
        engine.runAndWait()

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

    def take_time():
        speak("What time should I set the reminder for")
        time = takecommand()
        if time == "none":
            return take_time()
        if ":" in time:
            temp_list = time.split(":")
            hour = temp_list[0]
            min = temp_list[1]
        elif len(time) == 3:
            hour = time[0]
            min = time[1:]
        elif len(time) == 4:
            hour = time[0:2]
            min = time[2:]
        else:
            speak("I didnt quite catch that, Can you repeat the time")
            return take_time()

        return hour, min

    hour, min = take_time()


    time_final = hour + ":" + min + ":" + "00"
    print(time_final)
    if len(time_final) == 8 or len(time_final) == 7:
        speak("What is the reminder for ?")
        reminder_command = takecommand()
        print(reminder_command)
    else:
        speak("There was some problem ! Please try again ")

    def Reminder(timex, reminder_txt):
        def todaysDate():
            daily_clock = time.localtime()
            daily_date = time.strftime("%a, %b %d %Y", daily_clock)
            data = "----------------\n" + daily_date + "\n----------------"
            with open("history_reminder.txt", 'a') as output:
                output.write("\n" + data + '\n')
                output.close()
                return Alarm()

        def Alarm():
            global listA
            end_time = time.time()
            time_evolved = end_time - start_time
            print(time_evolved)
            end_time1 = timex
            reminder = reminder_txt
            all = "Time: " + end_time1 + " Your Reminder is: " + reminder
            listA.append(all)
            with open("history_reminder.txt", 'a') as output:
                output.write(all + '\n')
            speak("Reminder Set. Commencing Count Down")
            its_time = False
            while its_time == False:
                its_time = False
                clock = time.localtime()  # get struct_time
                Timer = time.strftime("%a, %b %d %Y, %X%p (%Z)", clock)
                if end_time1 in Timer:
                    its_time = True
                    # print("Your Reminder is:\n(", reminder, ")")
                    # string2 = "He he he he haas dele rinkiya ke papa he he he he "
                    string = f"Reminder for {reminder}"
                    # speak(string2)
                    speak(string)
                    # speak(string2)
                    speak(string)
                    # time.sleep(8)

                else:
                    start = time.strftime("%X")
                    format = '%H:%M:%S'
                    time_left = datetime.strptime(end_time1, format) - datetime.strptime(start,format)

                    print(time_left)

                    time.sleep(1)
                    its_time = False
        todaysDate()


    try:
        Reminder(time_final, reminder_command)
    except:
        speak("There was some error..Please take a look at the code")

    return

#ENDOFCODE- Made By Akshat Rastogi
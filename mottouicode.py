import pyttsx3
import speech_recognition as sr
import datetime 
import os
import sys
import random
import requests
import winsound
from instaloader import instaloader
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import pyjokes
import pyautogui
import time
import PyPDF2
import pygeoip
import requests
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from mottoui import Ui_MainWindow
import weather
import face_recognition_moto
import mood_detection_moto
import always_active
import badminton
import tossing
import stone_paper_scissor
import scare_moto
import random_choosing
import dictionary
import email_automation
import face_mask_detection
import love_calculator
import news_api
import online_search
import password_generator
import pyperclip
import quotes
import security_camera
import pygame
import shopping_automation
import spam_bot
import text_to_handwriting
import Zero_Width_Fingerprinting
from spotifymusic import spotipy_lol
import tictactoe
import timetable
import email_reading
import calculator_voice

naam = ""
mrms = ""
sorm = ""
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

# Here we are selecting the human like voices

for voice in voices:
    engine.setProperty('voice', voice.id)
    engine.runAndWait()
    engine.stop()
    break

f = open('text_to_print.txt', 'w')
f.write("Welcome")
f.close()

# The above code was modified to select a female voice instead of a male one
engine.setProperty('rate', 150)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, language='en-in')
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()


def speak(audio):
    pygame.mixer.music.set_volume(0.1)
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
    pygame.mixer.music.set_volume(0.02)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=1000000000000000000)
    try:
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        return "none"
    return query

def speak3(audio):
    for voice in voices:
        engine.setProperty('voice', voice.id)
        engine.runAndWait()
        engine.stop()

    engine.say(audio)
    print(audio)
    engine.runAndWait()

def speak2(audio):
    for voice in voices:
        engine.setProperty('voice', voice.id)
        engine.runAndWait()
        engine.stop()
        break
    f = open('text_to_print.txt', 'w')
    f.write(audio)
    f.close()
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        return day_of_the_week

#coverts voice to text


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()


    def takecommand(self):
        pygame.mixer.music.set_volume(0.05)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            # print("Listening...")
            f = open('text_to_print.txt', 'w')
            f.write("Listening...")
            f.close()
            r.pause_threshold = 1
            audio = r.listen(source, timeout=2.5, phrase_time_limit=10)
        try:
            # print("")
            f = open('text_to_print.txt', 'w')
            f.write("Recognizing...")
            f.close()
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except Exception as e:
            return "none"

        return query
    
    def TaskExecution(self):
        pygame.mixer.init()
        pygame.mixer.music.load("background_music.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.4)
        time.sleep(3)

        global naam
        global mrms
        global sorm
        speak2("Starting Moto")
        speak2("Authorising Command Access by Facial Recognition")
        speak2("Please look in the camera")
        identity = ""
        try:
            identity = face_recognition_moto.recognizeFace()
        except:
            speak2("Your Identity could not be verified")

        if identity not in ["AkshatRastogi", "SamarthGoyal", "SaumyaTripathi"]:
            speak2("You are not authorised to access Moto")
            speak2("Encrypting Servers and Shutting down")
            time.sleep(2)
            scare_moto.scare()
            sys.exit()

        if identity == "AkshatRastogi":
            naam = "Akshat"
            mrms = "Mister"
            sorm = "Sir"
        elif identity == "SaumyaTripathi":
            naam = "Saumya"
            mrms = "Miss"
            sorm = "Maam"
        elif identity == "SamarthGoyal":
            naam = "Samarth"
            mrms = "Mister"
            sorm = "Sir"

        speak2("Authorization Complete")
        speak2(f"Welcome {mrms} {naam}")
        # speak2("Trying to activate servers")
        # speak2("Servers are online")
        speak2("Moto is waking up")
        time.sleep(1)
        pygame.mixer.music.set_volume(0.1)
        wish()
        # ipAdd = requests.get('https://api.ipify.org').text

        if naam in ["Akshat", "Samarth"]:
            speak(f"Mister {naam} What can I do for you today?")
        elif naam in ["Saumya"]:
            speak(f"Miss {naam} What can I do for you today ?")
        else:
            speak("Hello, What can I do for you today")

        while True:

            self.query = self.takecommand().lower()

            if "hello moto" in self.query:
                speak(f"Hello {mrms}")
                res = requests.get('https://ipinfo.io')
                data = res.json()
                city = data['city']
                temp_city, weather_desc, hmdt, wind_spd = weather.Weather(str(city))
                temp_city = str(temp_city)[:5]
                speak(f"It is {weather_desc}y outside with a temperature of {temp_city} degree Celsius")
                speak("Overall, its a lovely day to be alive")
            # Checked

            elif "how are you" in self.query:
                speak(f"I am getting better everyday {mrms}")
            # Checked

            #how does my day look like
            #whats my time table
            elif "how does my day look like" in self.query or "time table" in self.query or "timetable" in self.query:
                today = tellDay()
                time_ta = timetable.TimeTable[today]
                if today in ['Saturday', 'Sunday']:
                    speak(f"You dont have any classes today {mrms}")
                speak("You have the following schedule today")
                for i in time_ta:
                    speak(f"At {i[0]} you have a {i[-1]} class")


            elif "who created you" in self.query:
                speak("I am created by a team of young scientists at Bennett University")
            # Checked

            elif "read my emails" in self.query or ("read" in self.query and "email" in self.query):
                speak("Fetching Emails")
                list_of_emails = email_reading.read_email_from_gmail()
                speak("Your top three emails are")
                for i in range(3):
                    from_ac = list_of_emails[i][0]
                    message = list_of_emails[i][1]
                    speak(f"You have an email from {from_ac}")
                    speak(message)
                    winsound.Beep(1000, 500)


            # Checked

            elif "minimum specifications" in self.query:
                speak("The minimum hardware specifications required to run moto are")
                speak("Atleast 4 gigabytes of ram although 8 is recommended")
                speak("A camera with Intel or Ryzen processor")
                speak("80 gigabytes of hard disk space and a dual core processor")
            # Checked

            elif "open notepad" in self.query:
                npath ="C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(npath)
            #Checked

            elif "bennett university" in self.query:
                string = "Bennett University is a private university located in Greater Noida, Uttar Pradesh in the National Capital Region, India. Founded in 2016 by Times of India Group and established under Uttar Pradesh Act No. 24 of 2016, the university has a fully residential 68-acre campus, near the proposed metro station on the Noida-Greater Noida metro railway line."
                speak(string)
            #Checked

            elif  "app" in self.query and "play store" in self.query:
                webbrowser.open("https://play.google.com/store/apps/details?id=com.willowood.akshatrastogi.willowoodagri&hl=en_US&gl=US")
                time.sleep(3)
                speak(f"Your app is doing good {mrms}")
            #Checked

            elif  "open android studio" in self.query and "play store" in self.query:
                mpath = r"C:\Program Files\Android\Android Studio\bin\studio64.exe"
                os.startfile(mpath)

            elif "who is" in self.query and "samarth" in self.query:
                string = "Mister Samarth Goyal is one of my founders and developers."
                speak(string)

            elif "who is" in self.query and "saumya" in self.query:
                string = "Miss Saumya Tripathi is one of my founders and developers."
                speak(string)

            elif "who is" in self.query and "akshat" in self.query:
                string = "Mister Akshat Rastogi is one of my founders and developers."
                speak(string)

            elif "weather" in self.query:
                res = requests.get('https://ipinfo.io')
                data = res.json()
                city = data['city']
                temp_city, weather_desc, hmdt, wind_spd = weather.Weather(str(city))
                temp_city = str(temp_city)[:5]
                speak(f"It is {weather_desc}y outside with a temperature of {temp_city} degree Celsius")
                speak(f"Current humidity is {hmdt} percent and wind is expected to blow at an approximate speed of {wind_spd} kilometers per hour")
            #Checked

            elif "open mozilla firefox" in self.query or "open firefox" in self.query:
                mpath =r"C:\Program Files\Firefox Developer Edition\firefox.exe"
                os.startfile(mpath)
            #Checked

            # dictionary giraffe
            #word meaning of halua
            elif "dictionary" in self.query or "word meaning of" in self.query:
                meaning = dictionary.dictionary_lol((self.query.split()[-1]))
                speak(f"{meaning}")


            #Checked

            # instagram automation
            elif "instagram automation" in self.query or "automate my instagram" in self.query or "automate instagram" in self.query:
                speak("Automating your instagram account")
                os.system('instagram_automation.py')

            # love calculator
            # calculate love
            elif "love calculator" in self.query or "calculate love" in self.query or "love with" in self.query:
                speak("Opening love calculator")
                speak("Who is the first person")
                time.sleep(3)
                speak("Who is the second person")
                time.sleep(3)
                speak("Calculating Compatibility percentage by using Love Algorithm")
                percentage = love_calculator.love()
                speak(f"They both are {percentage} percent compatible with each other")

            #Checked

            #times new roman - 12 font
            #I am going out
            #mask detection
            elif "i am going out" in self.query or "mask detection" in self.query:
                speak(f"Hey {mrms} {naam} can you please face the camera")
                answer = face_mask_detection.recognize_mask()
                if answer == "Mask Detected":
                    speak("You are wearing a mask")
                    speak("That's good")
                    speak("Be Safe")
                elif answer == "Mask not Detected":
                    speak("You are not wearing a mask")
                    speak("Please wear a mask")
                    speak("You should not go out without wearing the mask")
                else:
                    speak("Your face was not detected")
                    speak("Anyways have a safe journey")

            #Checked


            elif "send email" in self.query or "send mail" in self.query or "send male" in self.query or 'email' in self.query:
                speak("Do you want to send multiple emails or a single email ?")
                som = self.takecommand().lower()

                dic = {'samarth' : 'e20cse084@bennett.edu.in', 'saumya' : 'e20cse030@bennett.edu.in', 'akshat' : 'e20cse003@bennett.edu.in'}

                list_Recipuents = []
                if som.startswith('m'):
                    som = 'multiple'
                    speak("How many people do you want to send mail to")
                    try:
                        num = int(self.takecommand().lower())
                    except:
                        speak("Invalid Option")
                        num = 3

                    while num>0:
                        speak(f"Who do you want to send mail to {mrms} {naam}")
                        name = get_audio().lower()
                        if name.startswith('sam'):
                            name = 'samarth'
                        elif name.startswith('ak'):
                            name = 'akshat'
                        elif name.startswith('sau') or name.startswith('sou'):
                            name = 'saumya'
                        else:
                            name = 'samarth'


                        list_Recipuents.append(dic[name])

                    speak(f"What is the message {mrms}")
                    msg = self.takecommand()
                    email_automation.send_mail(list_Recipuents, msg)

                elif som.startswith('s'):
                    som = 'single'
                    speak(f"Who do you want to send mail to {mrms}")
                    name = self.takecommand().lower()
                    if name.startswith('sam'):
                        name = 'samarth'
                    elif name.startswith('ak'):
                        name = 'akshat'
                    elif name.startswith('sau') or name.startswith('sou'):
                        name = 'saumya'
                    else:
                        name = 'samarth'

                    list_Recipuents.append(dic[name])

                    speak(f"What is the message {mrms}")
                    msg = self.takecommand()
                    email_automation.send_mail(list_Recipuents, msg)

                speak("Message Sent")

            #Checked


            elif ("open ms teams" or "open microsoft teams") in self.query:
                tpath = r"C:\Users\Akshat\AppData\Local\Microsoft\Teams\current\Teams.exe"
                os.startfile(tpath)

            elif "mood" in self.query:
                try:
                    final_mood = mood_detection_moto.recogniseMood()
                    speak(f"You seem to be {final_mood}")
                    if final_mood == "happy":
                        speak(f"It feels good to know that I have served you well {mrms} {naam}")
                    elif final_mood == "sad":
                        speak(f"I know you are having a bad day {mrms} {naam}")
                        speak("I dont know what happened but just remember, you created me")
                        speak("You can achieve anything you want")
                    elif final_mood == "neutral":
                        speak("You should keep working on what you want in order to achieve your goals")
                    else:
                        speak("What can I do ?")
                except:
                    speak("There was some problem")
                    speak("My best guess is that your face was not visible")


            # elif "open command prompt" in self.query:
            #     os.system("Start cmd")
            # latex


            elif "play" in self.query and "music" in self.query:
               music_dir = r"C:\Users\Akshat\Documents\GitHub\Project-ASS\songs"
               songs = os.listdir(music_dir)
               rd = random.choice(songs)
               os.startfile(os.path.join(music_dir,rd))

            elif "ip address" in self.query:
                ip = get("https://api.ipify.org").text
                speak(f"your ip address is {ip}")

            #Checked

            elif "bitcoin mining" in self.query or "mine bitcoin" in self.query:
                speak("Bitcoin Mining Started")
                speak("The system will mine bitcoins right now")
                speak("Say stop to stop mining")
                import bitcoin_mining
                bitcoin_mining.mine_bitcoins()
                speak("Bitcoin Mining Successful")
                speak("The resulting hash value has been stored in a text file")

            #Checked

            elif "gesture control" in self.query or "gesture" in self.query:
                speak("Gesture Control Activated")
                speak("You need something blue on your hand in order to control the system")
                speak("Current Functionalities only include scrolling down on social media platforms")
                import control_social_media_by_hands
                control_social_media_by_hands.gesture_controls()
                speak("Thank You for using Gesture Controls")

            elif "wikipedia" in self.query:
                speak("searching Wikipedia...")
                query1 = self.query.replace("wikipedia","")
                results = wikipedia.summary(query1,sentences=2)
                speak("According to Wikipedia")
                speak(results)
                
            elif "open youtube website" in self.query:
                webbrowser.open("www.youtube.com")

            elif "open gmail" in self.query:
                webbrowser.open("www.gmail.com")

            elif "open stackoverflow" in self.query:
                webbrowser.open("www.stackoverflow.com")

            elif "open facebook" in self.query:
                webbrowser.open("www.facebook.com")

            elif "function in python" in self.query:
                x = 'def sample(a,b):\n\tsam = a+b\n\treturn sam'
                pyperclip.copy(text=x)
                speak("okay")
                pyautogui.hotkey('ctrl', 'v', interval = 0.15)

            elif "class in python" in self.query:
                x = 'class Sample:\n\tdef __init__(self, a, b):\n\t\tself.a = a\n\t\tself.b = b'
                pyperclip.copy(text=x)
                speak("okay")
                pyautogui.hotkey('ctrl', 'v', interval = 0.15)

            elif "edit text in android" in self.query:
                x = '<TextView\n\tandroid:layout_width="wrap_content"\n\tandroid:layout_height="wrap_content"\n\tandroid:layout_marginStart="30dp"\n\tandroid:layout_marginEnd="30dp"\n\tandroid:layout_marginTop="50dp"\n\tandroid:gravity="center"\n\tandroid:text="Enter Customer ID"\n\tandroid:textColor="@color/colorTextPrimary"\n\tandroid:textSize="14sp"/>'
                pyperclip.copy(text=x)
                speak("okay")
                pyautogui.hotkey('ctrl', 'v', interval = 0.15)

            elif "indent in android" in self.query:
                x = 'Intent registerIntent = new Intent(SampleActivity1.this, SampleActivity2.class);\nSplashScreen.this.startActivity(registerIntent);'
                pyperclip.copy(text=x)
                speak("okay")
                pyautogui.hotkey('ctrl', 'v', interval = 0.15)

            elif "declare a button in android" in self.query:
                x = 'final Button button1 = findViewById(R.id.sampleid);'
                pyperclip.copy(text=x)
                speak("okay")
                pyautogui.hotkey('ctrl', 'v', interval = 0.15)

            elif "declare an edit text in android" in self.query or "declare a edit text in android" in self.query:
                x = 'final EditText et1 = findViewById(R.id.sampleid)'
                pyperclip.copy(text=x)
                speak("okay")
                pyautogui.hotkey('ctrl', 'v', interval = 0.15)

            elif "declare an image in android" in self.query:
                x = 'final Image im1 = findViewById(R.id.sampleid)'
                pyperclip.copy(text=x)
                speak("okay")
                pyautogui.hotkey('ctrl', 'v', interval = 0.15)


            elif "open lms" in self.query:
                webbrowser.open("https://lms.bennett.edu.in/login/index.php")

            elif "open google" in self.query:
                speak("What should I search on google?")
                cm = self.takecommand().lower()
                webbrowser.open("https://www.google.com/search?q=" + str(cm.lower()))

            # elif "send message" in self.query:
            #     nu = int("Please enter the mobile number with : ")
            #     nu1 = str(nu)
            #     kit.sendwhatmsg(nu1,"His this message was sent using python", 10,28)

            elif "always active" in self.query:
                speak("Activating Always Active Mode")
                speak("Say Stop anytime to disable this feature")
                always_active.alwaysActive()
                speak("Thanks for using always active mode")

            # toss a coin
            elif "toss a coin" in self.query:
                lol = tossing.toss()
                speak(f"{lol}")

            # a or b
            #cat or dog
            elif " or " in self.query:
                lol = random_choosing.random_choosing1(self.query)
                speak(f"{lol}")

            #I want to play some games
            #I want to play game
            #Lets play a game
            elif "to play some games" in self.query or "to play game" in self.query or "play a game" in self.query or "play game" in self.query:
                speak("Okay lets play a game")
                speak("I have the following games")
                speak("1     Badminton Game")
                speak("2     Tossing Game")
                speak("3     Stone Paper Scissor")
                speak("4     Tic Tac Toe")
                speak("To play a game say the index number of that game")
                indn = self.takecommand().lower()

                if "one" in indn or "1" in indn:
                    speak("You have selected Badminton")
                    speak("The rules are as follows")
                    speak("You need to find something red around you and use that as the badminton racket")
                    speak("I will give you 15 seconds to get that")
                    time.sleep(15)
                    speak("Okay Lets Start")
                    points = badminton.play_badminton()
                    speak("oops, Seems like you lost")
                    speak(f"You scored {points} points")

                elif "two" in indn or "2" in indn or 'tu' in indn:
                    speak("You have selected Tossing")
                    speak("Rules are simple")
                    speak("You have to choose heads or tails")
                    speak("Are you ready?")
                    speak("Lets Go")
                    point = 0
                    while True:
                        speak("What do you choose ?")
                        user_ans = self.takecommand().lower()
                        if user_ans.startswith('h'):
                            user_ans = 'heads '
                        elif user_ans.startswith('t'):
                            user_ans = 'tails'
                        lol = tossing.toss()
                        speak(f"The result was {lol}")
                        if user_ans.lower() == lol:
                            speak("You win")
                            point = point + 1
                            speak(f"You have {point} points")
                        elif 'end' in user_ans.lower():
                            speak("Thank You for playing")
                        else:
                            speak("You lose")
                            speak(f"You have {point} points")
                            break

                elif "three" in indn or "3" in indn:
                    speak("You have selected Stone Paper Scissor")
                    speak("The rules are as follows")
                    speak("You need to choose between stone paper and scissor")
                    speak("What do you choose?")
                    user_ans = self.takecommand().lower()
                    if user_ans == "stone":
                        cc, stat = stone_paper_scissor.SPS("stone")
                        speak(f"I chose {cc} You {stat} ")
                    elif user_ans == "paper":
                        cc, stat = stone_paper_scissor.SPS("stone")
                        speak(f"I chose {cc} You {stat} ")
                    elif user_ans == "scissor":
                        cc, stat = stone_paper_scissor.SPS("stone")
                        speak(f"I chose {cc} You {stat} ")
                    else:
                        speak("Exiting")

                elif "four" in indn or "4" in indn:
                    speak("You have selected Tic Tac Toe")
                    speak("This is a mutiplayer game, so I suggest the presence of two players to play this game")
                    speak("Starting Stone Paper Scissor")
                    tictactoe.show_tik_tok()
                else:
                    speak("That was not a valid input")

            elif "video on youtube" in self.query or "youtube video" in self.query:
                speak("What is the name of the video?")
                sm = self.takecommand().lower()
                kit.playonyt(sm)

            elif "zero width" in self.query or "text encryption" in self.query or "encryption" in self.query:
                speak("Accessing Zero Width Fingerprinting")
                #public and private message
                speak("I need you to open project terminal and input public and private messages")
                speak("Please input the public message")
                pub_m = input()
                speak("Please input private message")
                pri_m = input()
                speak("Starting Zero Width Fingerprinting")
                Zero_Width_Fingerprinting.get_zwf_text(pub_m, pri_m)
                speak("The encrypted message has been copied to your clipboard")

            # tell me a quote
            # motivate me
            elif "quotes" in self.query or "quote" in self.query or "motivate" in self.query:
                speak("I have just the right quote for you")
                quote, author = quotes.get_quote()
                speak(str(author + " rightly said " + quote))

            #Security Camera
            # turn on security mode

            elif "security" in self.query:
                speak("Activating Super Security Mode")
                security_camera.security_camera()

            #shopping
            #amazon
            elif "shopping" in self.query or "amazon" in self.query:
                speak(f"What item do you want to shop {mrms}")
                item = self.takecommand().lower()
                shopping_automation.shopping_automation_lol(item)
                speak("Here are the top results")

            #spam
            #spamming
            elif "spam" in self.query or "spamming" in self.query:
                speak(f"What message do you want to spam {mrms}")
                mess = self.takecommand().lower()
                speak("The spamming will start in 10 seconds")
                speak("Open the application on which you want to spam")
                time.sleep(10)
                spam_bot.spam(mess)

            # Spotify
            elif "spotify" in self.query or "music by artist" in self.query:

                npath = r"C:\Users\Akshat\AppData\Local\Microsoft\WindowsApps\Spotify.exe"
                os.startfile(npath)
                list_of_artist = ['Arijit Singh', 'Shirley Setia', 'Armaan Malik']
                artist = random.choice(list_of_artist)
                spotipy_lol(artist)

            #Tested -C

            elif "stopwatch" in self.query:
                from stopwatch import Stop_Watch
                Stop_Watch()

            elif "handwriting" in self.query:
                speak("I can convert your text image into handwritten text")
                speak("I need you to open the project terminal and input your text file name")
                a = input("Enter file name :")
                try:
                    text_to_handwriting.text_to_handwriting(a)
                    speak("Your file has been converted and saved in the project directory")
                except:
                    speak("Something went wrong")

            elif "reminder" in self.query:
                from reminder import Remind
                Remind()

            elif "password" in self.query:
                speak("Would you like the default 12 digit password")
                yorn = self.takecommand().lower()
                if yorn.startswith('y'):
                    password = password_generator.generatepassword(4, 4, 4)
                else:
                    speak("How many letters would you like in your password?")
                    nol = int(self.takecommand().lower())
                    speak("How many symbols would you like?")
                    nos = int(self.takecommand().lower())
                    speak("How many numbers would you like?")
                    non = int(self.takecommand().lower())
                    password = password_generator.generatepassword(nol, nos, non)

                pyperclip.copy(password)
                speak("Your password has been generated")
                f = open('text_to_print.txt', 'w')
                f.write(str(password))
                f.close()
                speak("The password has also been copied to the clipboard")

            # News
            elif "news" in self.query:
                speak("On what topic do you want me to scrape news articles ?")
                topic = self.takecommand().lower()
                list_of_news = news_api.get_news(topic)
                speak("Reading the top 5 news articles on the given topic")
                for i in range(5):
                    list_new = list_of_news[i]
                    speak("Article {}".format(str(i+1)))
                    speak(list_new[0])
                    speak("Description")
                    speak(list_new[1])

            elif "voice calculator" in self.query or "calculator" in self.query:
                speak("Activating Voice Calculator Mode")
                speak("What can I calculate for you ")
                query = self.takecommand().lower()
                try:
                    output = calculator_voice.calculate(query)
                    speak(output)
                except:
                    speak("Query not supported in Calculator Mode")

            #what is python
            #search online about honey
            elif "what is" in self.query or "search online" in self.query:
                topic = self.query.split()[-1]
                result = "ok"
                try:
                    result = online_search.online_search(topic)
                    print(result)
                    speak(str(result))
                except:
                    speak("Could not find any search results")
                    speak(result)

            elif "command prompt" in self.query or "terminal" in self.query or "hacking" in self.query or "terminally" in self.query:
                npath = r"C:\Program Files\eDEX-UI\eDEX-UI.exe"
                os.startfile(npath)

            elif "sorting" and "visualise" in self.query or "sorting visualizer" in self.query:
                speak("Okay I am opening up the sorting algorithm visualizer")
                os.system("sorting.py")

            elif "send a whatsapp message" in self.query or "whatsapp message" in self.query or "whatsapp" in self.query:
                phone = ""
                speak("Who do you want to send a message sir")
                name = self.takecommand().lower()
                while True:
                    yes_or_no = "no"
                    if name not in ['samarth', 'saumya', 'soumya', 'soma']:
                        speak("The name you said is not in my database")
                        speak("Do you want me to send message to an unknown number ?")
                        yes_or_no = self.takecommand().lower()

                    if "yes" in yes_or_no:
                        speak("Please say the number")
                        phone = self.takecommand().lower()
                        break
                    else:
                        break

                if name.lower() == "samarth":
                    phone = "7300480752"
                elif name.lower() == "saumya" or name.lower() == "soma" or name.lower() == "soumya":
                    phone = "9999408980"
                # elif len(phone) < 12:
                # speak("The number you gave was invalid, You are such a fool YOU puny human")

                if len(phone) >= 10:
                    speak("What is the message sir ?")
                    message = self.takecommand().lower()
                    hour = int(datetime.datetime.now().hour)
                    minu = int(datetime.datetime.now().minute) + 1
                    try:
                        speak("Your message will be sent in 1 minute")
                        kit.sendwhatmsg("+91" + phone, message, hour, minu + 1)
                    except:
                        speak("There was an error sending the message")


            elif "set alarm" in self.query:
                nn = int(datetime.datetime.now().hour)
                inp = int(input("Enter the time"))
                if nn == inp:
                    mus = r"C:\Users\Akshat\Documents\GitHub\Project-ASS\songs"
                    songs = os.listdir(mus)
                    os.startfile(os.path.join(mus,songs[0]))

            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke("en")
                speak(joke)

            elif "shut down the system" in self.query:
                os.system("shutdown /s /t 5")

            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")

            elif "sleep the system" in self.query:
                os.system("rundll32.exe owrprof.dll, SetSuspendState 0,1,0")

            elif "switch the window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")


            #Where am I
            #Whats my location
            #Whats my geolocation
            
            elif "where am i" in self.query or "location" in self.query or "geolocation" in self.query:
                speak("please hold on..")
                try:
                    res = requests.get('https://ipinfo.io')
                    data = res.json()
                    city = data['city']
                    # ipAdd = requests.get('https://api.ipify.org').text
                    # print(ipAdd)
                    # url = 'https://get.geojs.io/vl/ip/geo/'+ipAdd+'.json'
                    # geo_requests = requests.get(url)
                    # geo_data = geo_requests.json()
                    # city = geo_data['city']
                    # country = geo_data['country']
                    speak(f"I think you are in {city}")
                except Exception as e:
                    speak("Sorry I am unable to currently find your location")
                    pass
            
            elif "instagram profile" in self.query or "profile on instagram" in self.query:
                speak( "Please enter the user name correctly")
                name = input("Enter username here:")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"Here is the profile of the user {name}")
                time. sleep(5)
                speak("Would you like to download profile picture of this account.")
                condition = self.takecommand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()              #pip install instadownloader
                    mod. download_profile(name, profile_pic_only=True)
                    speak("The profile picture has been saved in our main folder. now i am ready")
                else:
                    pass

            elif "take screenshot" in self.query or "take a screenshot" in self.query:
                    speak("Please tell me the name for this screenshot file")
                    name = self.takecommand().lower()
                    speak("please wait while I take sreenshot")
                    time.sleep(3)
                    img = pyautogui.screenshot()
                    img.save(f"C:\\Users\\Akshat\\Desktop\\{name}.png")
                    speak("Screenshot has been saved on your Desktop.")

            elif "read a pdf" in self.query or "read pdf" in self.query:
                pdf_reader()

            elif "hide all files" in self.query or "hide this folder" in self.query or "visible for everyone" in self.query:
                speak("Do you wish to hide this folder or make it visible for everyone")
                condition = self.takecommand().lower()
                if "hide" in condition:
                    os.system("attrib +h /s /d")
                    speak("all the files in this folder are now hidden.")

                elif "visible" in condition:
                    os.system("attrib -h /s /d")
                    speak("all the files in this folder are now visible to everyone.")
                
                elif "leave it" in condition or "leave for now" in condition:
                    speak("Ok sir")

            elif "stop" in self.query:
                speak("Thanks for availing my service.")
                sys.exit()
            #Sample Sentence
            # not for some time
            # go to sleep
            # let me work this
            # nope
            #not for a while
            elif "not for some time" in self.query or "not for sometime" in self.query or "sleep" in self.query or "let me work" in self.query or "nope" in self.query or "" in self.query:
                speak("Thanks for availing my services")
                speak("Just say the words Wake Up if you need me anytime soon")
                pygame.mixer.music.set_volume(0.00)
                while True:
                    print("Listening")
                    text = get_audio()
                    if text.count("wake up") > 0:
                        speak("I am ready")
                        speak("What can I do for you ?")
                        break
            else:
                speak("Done")
                # speak("Do you have any other request?")




def wish():
    hour = int(datetime.datetime.now().hour)
    if 0<hour<12:
        speak("Good morning!")
    elif 12<=hour<16:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Moto")
    # ct = datetime.datetime.now().hour
    # speak(f"It is {ct} hours")

def pdf_reader() :
    speak("Please enter the full name of the pdf with extension:")
    pn = input("Please enter the full name of the pdf with extension:")
    book = open(pn,'rb')
    pdfReader = PyPDF2.PdfFileReader(book) 
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in this book {pages}")
    speak("Please enter the page number I have to read")
    pg = int(input ("Please enter the page number: ") )
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)


startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_3.clicked.connect(self.close)


    def startTask(self):
        self.ui.movie = QtGui.QMovie("CorruptLinearElk-size_restricted.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("new_updated_logo.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("D4Ll.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser_2.setText(label_date)
        self.ui.textBrowser_3.setText(label_time)
        f = open('text_to_print.txt', 'r')
        text = f.readline()
        f.close()
        self.ui.textBrowser_69.setText(text)


app = QtWidgets.QApplication(sys.argv)
motto = Main()
motto.show()
exit(app.exec_())
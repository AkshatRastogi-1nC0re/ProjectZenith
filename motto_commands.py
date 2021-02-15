import pyttsx3
import speech_recognition as sr
import datetime 
import os
import sys
import random
import requests
from instaloader import instaloader
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import pyjokes
import pyautogui
import time
import PyPDF2
import dictionary

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices',voices[1].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=10)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        speak("Please say it again.")
        return "none"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)
    if 0<hour<12:
        speak("Good morning!")
    elif 12<=hour<16:
        speak("Good afternoon!")
    elif 16<hour<20:
        speak("Good evening!")    
    else:
        speak("Good night!")
    ct = datetime.datetime.now().hour
    speak(f"It is {ct} hours")
    speak("I am Motto. What can I do for you?")

def pdf_reader() :
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

if __name__ == "__main__":
    wish()
    while True:
    # if 1:

        query = takecommand().lower()

        if "open notepad" in query:
            npath ="C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open mozilla firefox" in query:
            mpath ="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(mpath)
        
        elif ("open ms teams" or "open microsoft teams") in query:
            tpath ="C:\\Users\\Saurabh Tripathi\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Teams"
            os.startfile(tpath)

        elif "open command prompt" in query:
           os.system("Start cmd")

        elif "play music" in query:
           music_dir = ""
           songs = os.listdir(music_dir)
           rd = random.choice(songs)
           os.startfile(os.path.join(music_dir,songs))

        elif "ip address" in query:
           ip = get("https://api.ipify.org").text
           speak(f"your ip address is {ip}")


        # what is the meaning of Sun
        elif "meaning" in query:
            word = (query.lower().split(" "))[-1]
            meaning = dictionary.dictionary(word)
            speak(meaning)

        elif "wikipedia" in query:
            speak("searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            speak(results)
            
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open gmail" in query:
            webbrowser.open("www.gmail.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open lms" in query:
            webbrowser.open("https://lms.bennett.edu.in/login/index.php")

        elif "open google" in query:
            speak("What should I search on google?")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
           nu = int("Please enter the mobile number with : ") 
           nu1 = str(nu)
           kit.sendwhatmsg(nu1,"His this message was sent using python", 10,28)

        elif "play a song on youtube" in query:
            speak("What is the name of the song?")
            sm = takecommand().lower()
            kit.playonyt(sm)

        elif "no stop" in query:
            speak("Thanks for availing my service.")
            sys.exit()

        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            inp = int(input("Enter the time"))
            if nn == inp:
                mus = " "
                songs = os.listdir(mus)
                os.startfile(os.path.join(mus,songs[0]))

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke("en")
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe owrprof.dll, SetSuspendState 0,1,0")

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        
        elif "where am i" in query:
            speak("please hold on..")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/vl/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"I think you are in {city} in the country {country} ")
            except Exception as e:
                speak("Sorry I am unable to currently find your location")
                pass
        
        elif "instagram profile" in query or "profile on instagram" in query:
            speak("Please enter the user name correctly")
            name = input("Enter username here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Here is the profile of the user {name}")
            time. sleep(5)
            speak("Would you like to download profile picture of this account.")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()              #pip install instadownloader
                mod. download_profile(name, profile_pic_only=True)
                speak("The profile picture has been saved in our main folder. now i am ready")
            else:
                pass
       
        elif "take screenshot" in query or "take a screenshot" in query:
                speak("Please tell me the name for this screenshot file")
                name = takecommand().lower()
                speak("please wait while I take sreenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"Desktop/{name}.png")
                speak("Screenshot has been saved on your Desktop.")

        elif "read a pdf" in query or "read pdf" in query:
            pdf_reader()

        elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
            speak("Do you wish to hide this folder or make it visible for everyone")
            condition = takecommand().lower()
            if "hide" in condition:
                os.system("attrib +h /s /d")
                speak("all the files in this folder are now hidden.")

            elif "visible" in condition:
                os.system("attrib -h /s /d")
                speak("all the files in this folder are now visible to everyone.")
            
            elif "leave it" in condition or "leave for now" in condition:
                speak("Ok sir")

        speak("Do you have any other request?")
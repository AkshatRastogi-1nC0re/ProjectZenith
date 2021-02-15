import pygame
from time import sleep
import pyttsx3



def scare():

    engine = pyttsx3.init('sapi5')

    voices = engine.getProperty('voices')

    # Here we are selecting the human like voices



    def speak(audio):
        engine.setProperty('rate', 160)
        for voice in voices:
            engine.setProperty('voice', voice.id)
            engine.runAndWait()
            engine.stop()
            break
        engine.say(audio)
        engine.runAndWait()

    # def takecommand_sleep():
    #     r = sr.Recognizer()
    #     with sr.Microphone() as source:
    #         r.pause_threshold = 1
    #         audio = r.listen(source, timeout=5, phrase_time_limit=1000000000000000000)
    #     try:
    #         query = r.recognize_google(audio, language='en-in')
    #     except Exception as e:
    #         return "none"
    #     return query

    pygame.init()
    window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    pygame.mixer.init()
    pygame.mixer.music.load(r'scare resources\ratsasan.mp3')
    pygame.mixer.music.play()
    speak("You are not authorised to access moto")
    sleep(4)
    speak("Go away!")
    sleep(1)
    speak("Right Now")
    pygame.mixer.music.load(r'scare resources\scary.mp3')
    pygame.mixer.music.play()
    sleep(1)
    image = pygame.image.load(r'scare resources\scr4.jpg')
    window.blit(image, (0,0))
    pygame.display.update()
    sleep(5)
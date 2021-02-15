import pywhatkit
import webbrowser
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import random

# pywhatkit.playonyt("Python")get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s')
# cm = "Halua"

# a or b
# cat or dog or halua

def random_choosing(stmt):
    listA = stmt.split()
    try:
        while 'or' in listA:
            listA.remove('or')
    except:
        pass

    print(listA)

    return random.choice(listA)

print(random_choosing('cat or dog or halua'))

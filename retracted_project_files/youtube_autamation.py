from selenium import webdriver
import win32com.client as comctl
from bs4 import BeautifulSoup
import time
import urllib.request
import urllib.parse
import re
import webbrowser
import urllib.request
import urllib.parse
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
wsh = comctl.Dispatch("WScript.Shell")
# ChromeDriverManager().install()

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get('https://www.youtube.com')
search=driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')

n="rinkiya ke papa"

search.send_keys(n)
wsh.SendKeys('{Enter}')
driver.implicitly_wait(5)
drive=driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a")
drive.click()
while(1):
    response=driver.page_source
    time.sleep(20)
    soup=BeautifulSoup(response,'lxml')
    current=soup.find(class_="ytp-time-current")
    last=soup.find(class_='ytp-time-duration')
    if current.text==last.text:
        continue
from selenium import webdriver
import win32com.client as comctl
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
import time


def get_zwf_text(public_message, private_message):
    wsh = comctl.Dispatch("WScript.Shell")
    # ChromeDriverManager().install()
    opts = webdriver.FirefoxOptions()
    opts.headless = False
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=opts)
    driver.get('https://neatnik.net/steganographr/')
    public = driver.find_element_by_xpath('//*[@id="public"]')
    public.send_keys(public_message)
    private = driver.find_element_by_xpath('//*[@id="private"]')
    private.send_keys(private_message)
    time.sleep(1)
    drive=driver.find_element_by_xpath("/html/body/main/form[1]/fieldset/p[4]/button")
    drive.click()
    time.sleep(2)
    elem = driver.find_element_by_xpath('/html/body/main/section/textarea')
    elem.send_keys("p")
    elem.send_keys(Keys.CONTROL, 'a') #highlight all in box
    elem.send_keys(Keys.CONTROL, 'c') #copy
    print("Text has been copied to clipboard")
    driver.close()


# get_zwf_text('surya', 'samarth')
#ENDOFCODE - Made By Akshat Rastogi

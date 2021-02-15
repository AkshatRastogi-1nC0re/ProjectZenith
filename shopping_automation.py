from selenium import webdriver
import win32com.client as comctl
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time



def shopping_automation_lol(search_item):
    wsh = comctl.Dispatch("WScript.Shell")
    # ChromeDriverManager().install()
    opts = webdriver.FirefoxOptions()
    opts.headless = False
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=opts)
    action = ActionChains(driver)
    time.sleep(1)

    driver.get('http://www.amazon.in')
    time.sleep(1)

    firstLevelMenu = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span/span')
    action.move_to_element(firstLevelMenu).perform()
    time.sleep(1)

    secondLevelMenu = driver.find_element_by_xpath('//*[@id="nav-flyout-ya-signin"]/a/span')
    secondLevelMenu.click()
    time.sleep(1)

    signinelement = driver.find_element_by_xpath('//*[@id="ap_email"]')
    signinelement.send_keys("8433098945")
    time.sleep(1)

    cont = driver.find_element_by_xpath('//*[@id="continue"]')
    cont.click()
    time.sleep(1)

    passwordelement = driver.find_element_by_xpath('//*[@id="ap_password"]')
    passwordelement.send_keys("akshat28")
    time.sleep(1)

    login = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
    login.click()
    time.sleep(1)

    '----------------------------X-------------------------X------------------------------------------------'

    searchbar = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
    searchbar.send_keys(search_item)
    searchbar.send_keys(Keys.ENTER)

    print("Here are the top results")


# shopping_automation("rinkiya ke papa")

#ENDOFCODE - Made By Akshat Rastogi

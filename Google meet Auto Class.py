from selenium import webdriver
import pyautogui
import datetime
from time import sleep
import sys
driver = webdriver.Chrome('chromedriver.exe')                                               # opening chrome
now = datetime.datetime.now()                                                               # current date
class_hour = 0                                                                              # hour of class
class_min = 0                                                                               # minute of class
email = ''                                                                                  # full email
username = ''                                                                               # SMART username
password = ''                                                                               # SMART password
hour = int(now.hour)                                                                        # current hour
minute = int(now.minute)                                                                    # current minute
wait = ((class_hour - hour)*60 + class_min - minute)*60                                     # time to wait(in seconds)


def auto_class():
    driver.get('https://meet.google.com/_meet')                                             # open google meet
    sleep(2)
    pyautogui.click(1496, 34)                                                               # maximize the tab
    sleep(2)
    pyautogui.click(1864, 218)                                                              # click 'sign in'
    driver.find_element_by_xpath('//input[@names=\"identifier\"]').send_keys(email)          # enter email
    pyautogui.click(1170, 864)                      # click 'next'
    sleep(2)
    driver.find_element_by_xpath("//input[@id=\"username\"]").send_keys(username)           # enter SMART username
    driver.find_element_by_xpath("//input[@names=\"password\"]").send_keys(password)         # enter SMART password
    driver.find_element_by_xpath("//input[@type='submit']").click()                         # click submit
    pyautogui.click(1188, 631)                                                              # enter meeting


if hour == class_hour and  min == class_min:
    auto_class()                                                                            # run the program
    sleep(216000)                                                                           # wait for 1 hour
    sys.exit()                                                                              # exit program
else:
    sleep(wait)                                                                             # wait till class starts
    auto_class()                                                                            # run the program
    sleep(216000)                                                                           # wait for 1 hour
    sys.exit()                                                                              # exit program

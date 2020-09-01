#system libraries
import os
import random
import time

#selenium libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException   
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.chrome.options import Options

#recaptcha libraries
import speech_recognition as sr
import ffmpy
import requests
import urllib
import pydub

def delay ():
    time.sleep(random.randint(2,3))


#create chrome driver
driver = webdriver.Chrome(os.getcwd()+"\\webdriver\\chromedriver.exe") 

#go to website
driver.get("https://www.google.com/recaptcha/api2/demo")

#switch to recaptcha frame
frames=driver.find_elements_by_tag_name("iframe")
driver.switch_to.frame(frames[0]);
delay()

#click on checkbox to activate recaptcha
driver.find_element_by_class_name("recaptcha-checkbox-border").click()

#switch to recaptcha audio control frame
driver.switch_to.default_content()
frames=driver.find_element_by_xpath("/html/body/div[2]/div[4]").find_elements_by_tag_name("iframe")
driver.switch_to.frame(frames[0])
delay()

#switch to recaptcha audio challenge frame
driver.switch_to.default_content()
frames= driver.find_elements_by_tag_name("iframe")
driver.switch_to.frame(frames[-1])
delay()

#click on the play button
driver.find_element_by_xpath("/html/body/div/div/div[3]/div/button").click()
#get the mp3 audio file
src = driver.find_element_by_id("audio-source").get_attribute("src")
print("[INFO] Audio src: %s"%src)



import os
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(os.getcwd()+"\\webdriver\\chromedriver.exe") 
driver.get("https://www.google.com/recaptcha/api2/demo")
driver.find_element_by_class_name("recaptcha-checkbox-border").click()


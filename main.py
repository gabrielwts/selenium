from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get ("C:/Users/75052/Downloads/selenium/index.html")

time.sleep(2)

campo_usuario = driver.find_element
#Clic en radiobutton


#Importar librerías
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time


website1 = 'https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&ifkv=AWnogHc619rtRKmedENHa0TRWRI7z4tRqDOHaqZsgeejPLU9zSsx1inqQWDSTJVHL6GbYA0hiqgSQQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
website2 = 'https://es.wikipedia.org/wiki/Austin'
website3 = 'https://www.w3schools.com/howto/howto_css_custom_checkbox.asp'


path = 'chromedriver.exe'
s = Service(path)
driver = webdriver.Chrome(service = s)

############################################################
#Accionar radiobutton

driver.get(website3)
time.sleep(5)


#verificar comillas
radiobutton = driver.find_element(By.XPATH, "//*[@id='main']/div[3]/div[1]/input[4]")
radiobutton.click()
time.sleep(3)

radiobutton = driver.find_element(By.XPATH, "//*[@id='main']/div[3]/div[1]/input[3]")
radiobutton.click()
time.sleep(3)

driver.close()
print('final de prueba')
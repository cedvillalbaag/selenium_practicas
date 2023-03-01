#Navegar entre pestañas en el mismo navegador

# #Importar librerías
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest
import time


website1 = 'https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&ifkv=AWnogHc619rtRKmedENHa0TRWRI7z4tRqDOHaqZsgeejPLU9zSsx1inqQWDSTJVHL6GbYA0hiqgSQQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
website2 = 'https://es.wikipedia.org/wiki/Austin'

path = 'chromedriver.exe'
s = Service(path)


driver =webdriver.Chrome(service = s)
driver.get(website1)
time.sleep(1)


#Abrir nueva pestaña
driver.execute_script("window.open('');")
time.sleep(1)
driver.switch_to.window(driver.window_handles[1])
driver.get(website2)
time.sleep(1)
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)





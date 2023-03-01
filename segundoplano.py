#SEGUNDO PLANO

#Correr Selenium en segundo plano

#Importar librerías
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options #Agregar


import unittest
import time


website1 = 'https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&ifkv=AWnogHc619rtRKmedENHa0TRWRI7z4tRqDOHaqZsgeejPLU9zSsx1inqQWDSTJVHL6GbYA0hiqgSQQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
website2 = 'https://es.wikipedia.org/wiki/Austin'
website3 = 'https://www.google.com/?hl=es'

chrome_options = Options() #Agregar
chrome_options.add_argument("--headless") #Agregar

path = 'chromedriver.exe'
s = Service(path)
driver = webdriver.Chrome(chrome_options = chrome_options, service = s) #Agregar

############################################################
#Ejercicio

driver.get(website3)
time.sleep(5)


#encontrar elemento por texto de enlace 
element = driver.find_element(By.LINK_TEXT, 'Privacidad')

#Realizar el hoover action
hover = ActionChains(driver).move_to_element(element)
hover.perform()


#Final
print('Prueba Finalizada')
input('escriba algo:')
driver.close()

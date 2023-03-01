#ALERT SIMPLE
# The simple alert class in Selenium displays some information or warning on the screen.
#Pop up generado por lenguaje de programacion al activar elemento en la web.
#https://www.selenium.dev/documentation/webdriver/interactions/alerts/


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

#chrome_options = Options() #Agregar
#chrome_options.add_argument("--headless") #Agregar

path = 'chromedriver.exe'
s = Service(path)
driver = webdriver.Chrome( service = s) #Agregar

############################################################
#Ejercicio Alerta Simple

driver.get('C:/Users/ASUS/Desktop/seleniumcurso_alvarez/alertsimple.html')
time.sleep(3)

#Clic para activar alerta simple
alertasimple = driver.find_element(By.NAME, 'alert').click()

#Cambiar a la caja de alerta simple
alertasimple = driver.switch_to.alert
time.sleep(2)

#Descartar caja de alerta simple
alertasimple.dismiss()


#############################################################

#Final
print('Prueba Finalizada')
input('escriba algo:')
driver.close()

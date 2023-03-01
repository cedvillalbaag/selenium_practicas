# EXPLICIT WAIT
#Dar condiciones para cargar ciertos componentes en un script
#Esperar hasta que cargue componente para que continue con la automatizacion
#para no utilizar time.sleep



# #Importar librerías
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
website3 = 'https://twitter.com/home'


path = 'chromedriver.exe'
s = Service(path)
driver =webdriver.Chrome(service = s)

############################################################
#Explicit Wait

driver.get(website1)
try: 
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME,'identifier'))
    )
finally:
    driver.quit()



print('prueba exitosa')
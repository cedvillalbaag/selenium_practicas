#Importar librerías
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time


# Abrir página web
website = 'https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&ifkv=AWnogHc619rtRKmedENHa0TRWRI7z4tRqDOHaqZsgeejPLU9zSsx1inqQWDSTJVHL6GbYA0hiqgSQQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
path = 'chromedriver.exe'


s = Service(path)
driver = webdriver.Chrome(service = s)
driver.get(website)


#Agregar usuario
usuario = driver.find_element(By.ID, "identifierId")
usuario.send_keys('ced.villalbaag@gmail.com')
usuario.send_keys(Keys.ENTER)
time.sleep(3)


#Agregar clave
clave =  driver.find_element(By.NAME, "Passwd")
clave.send_keys("correogmail2806")
clave.keys(Keys.ENTER)






#Instrucción adicional para evitar que se cierre el navegador
print('Hola Mundo')
input("Esperando que no se cierre webdriver: ")
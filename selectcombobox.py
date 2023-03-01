#SELECT - COMBO BOX

#Desplegar un campo de lista desplegable y seleccionar un valor.

#Importar librerías
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver import ActionChains
#from selenium.webdriver.chrome.options import Options #Agregar

#import unittest
import time

website1 = 'https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&ifkv=AWnogHc619rtRKmedENHa0TRWRI7z4tRqDOHaqZsgeejPLU9zSsx1inqQWDSTJVHL6GbYA0hiqgSQQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
website2 = 'https://es.wikipedia.org/wiki/Austin'
website3 = 'https://www.w3schools.com/howto/howto_custom_select.asp'

#chrome_options = Options() #Agregar
#chrome_options.add_argument("--headless") #Agregar

path = 'chromedriver.exe'
s = Service(path)
driver = webdriver.Chrome(service = s) #Agregar

############################################################
#Ejercicio Realizar Select  - Campo Lista Desplegable

#Abrir web
driver.get(website3)
time.sleep(3)

#Encontrar elemento de combobox
#select = driver.find_element(By.XPATH,"//*[@id='main']/div[3]/div[1]/select")
#time.sleep(5)
#select.click()

#Guardar todos los elemntos de la lista desplegable
#opcion = select.find_elements(By.TAG_NAME,"option")
#time.sleep(3)

#for option in opcion:
    #print(option.get_attribute("value"))
    #option.click()
    #time.sleep(1)
    


#Cierre
#driver.close()
print("prueba con exito")
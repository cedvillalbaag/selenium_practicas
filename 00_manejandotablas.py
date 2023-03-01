#MANEJANDO TABLAS

#

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
website3 = 'https://www.htmlquick.com/es/tutorials/tables.html'

#chrome_options = Options() #Agregar
#chrome_options.add_argument("--headless") #Agregar

path = 'chromedriver.exe'
s = Service(path)
driver = webdriver.Chrome( service = s) #Agregar

############################################################
#Ejercicio Realizar Manejando tablas

#Abrir web
driver.get(website3)
time.sleep(3)

#Manejando Tablas
valor = driver.find_element(By.XPATH, "//*[@id='header-cells']/div/div/table/tbody/tr[2]/td[3]").text
print(valor)


rows = len(driver.find_elements(By.XPATH, "//*[@id='header-cells']/div/div/table/tbody/tr"))
cols = len(driver.find_elements(By.XPATH, "//*[@id='header-cells']/div/div/table/tbody/tr[2]/td"))


#Cierre
print(rows)
print(cols)
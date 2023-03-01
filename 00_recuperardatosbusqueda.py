#RECUPERAR DATOS DE LA BARRA DE BUSQUEDA DE GOOGLE

#DAR CLIC EN HYPERLINK DE LA PAGINA
# VERIFICAR QUE LOS LINKS SE ENCUENTREN BIEN ESCRITOS

#Importar librerías
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import unittest
import time


website1 = 'https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&ifkv=AWnogHc619rtRKmedENHa0TRWRI7z4tRqDOHaqZsgeejPLU9zSsx1inqQWDSTJVHL6GbYA0hiqgSQQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
website2 = 'https://es.wikipedia.org/wiki/Austin'
website3 = 'https://www.google.com/'


path = 'chromedriver.exe'
s = Service(path)
driver = webdriver.Chrome(service = s)

############################################################
#Ejercicio

driver.get(website3)
time.sleep(5)


#encontrar elemento del hyperlink

busqueda = driver.find_element(By.NAME, 'q')
busqueda.send_keys("Longhorns")
time.sleep(2)

#Ciclo para que recorra lista
for i in range(1,11):
    elementos = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div/ul/li["+str(i)+"]/div/div[2]").text
    print('elementos')

#Final
print('Prueba Finalizada')

input('escriba algo:')
driver.close()
# SUBIR ARCHIVO 

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
import HtmlTestRunner


website1 = 'https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&ifkv=AWnogHc619rtRKmedENHa0TRWRI7z4tRqDOHaqZsgeejPLU9zSsx1inqQWDSTJVHL6GbYA0hiqgSQQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
website2 = 'https://es.wikipedia.org/wiki/Austin'
website3 = 'https://www.htmlquick.com/es/tutorials/tables.html'

#chrome_options = Options() #Agregar
#chrome_options.add_argument("--headless") #Agregar

path = 'chromedriver.exe'
s = Service(path)
#driver = webdriver.Chrome( service = s) #Agregar


path = 'chromedriver.exe'
s = Service(path)
driver = webdriver.Chrome(service = s)

       
website = "https://www.htmlquick.com/es/reference/tags/input-file.html"
driver.get(website)        
elemento = driver.find_element(By.NAME,'archivosubido').click()
time.sleep(2)
        

       

driver.close()
print("prueba finalizada")




#############################################################



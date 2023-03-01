# Mover Mouse

# Mover mouse y dar clic

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
driver = webdriver.Chrome( service = s) #Agregar


################## Unitest ##########################################
#Declarar clase
class suite(unittest.TestCase):
    #1.- Inicialización
    def setUp(self):
        path = 'chromedriver.exe'
        s = Service(path)
        driver = webdriver.Chrome(service = s)
        self.driver = driver


#IMPORTANTE: SIEMPRE COLOCAR TEST ANTES DEL NOMBRE DE LA FUNCION
    def test_manejandomouse(self):
        driver = self.driver
        website = "https://selenium-python.readthedocs.io/locating-elements.html"
        driver.get(website)
        time.sleep(5)

        #Encontrar los puntos de origen y destino
        mouse_mov = self.driver.find_element(By.LINK_TEXT, "2. Getting Started")
        mouse_mov2 = self.driver.find_element(By.LINK_TEXT, "6. Page Objects")

        #Para movimiento y dar clic en los enlaces indicados
        movimiento = ActionChains(self.driver)
        movimiento.move_to_element(mouse_mov).move_to_element(mouse_mov2).click().perform()
        time.sleep(3)

    

    #Finalización de las variables(limpieza)
    def tearDown(self):
        #Cierre de Navegador
        self.driver.quit()


#Funcion para que corran los UnitTest
if __name__ == '__main__':
    unittest.main()
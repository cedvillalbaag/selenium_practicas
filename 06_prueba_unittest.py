#UNITTEST

#Modulo para desarrollar funciones que son pruebas y generar reportes
#https://docs.python.org/3/library/unittest.html


#Importar librería
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

import unittest

# Abrir página web


################## Unitest ##########################################
#Declarar clase
class usando_unittest(unittest.TestCase):
    def setUp(self):
        
        path = 'chromedriver.exe'
        s = Service(path)
        driver = webdriver.Chrome(service = s)
        self.driver = driver


#IMPORTANTE: SIEMPRE COLOCAR TEST ANTES DEL NOMBRE DE LA FUNCION
    def test_buscar(self):
        driver = self.driver
        website = "https://www.google.com/?hl=es"
        driver.get(website)

        #Verificacion que estamos en la pagina correcta
        self.assertIn("Google", driver.title)
        element = driver.find_element(By.NAME, "q")
        element.send_keys("Carlos")
        element.send_keys(Keys.RETURN)
        time.sleep(5)

        assert "No se encontro el elemento" not in driver.page_source

    def tearDown(self):
        #Cierre de Navegador
        self.driver.close()


#Funcion para que corran los UnitTest
if __name__ == '__main__':
    unittest.main()

#############################################################



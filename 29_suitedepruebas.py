#Suite de Pruebas

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
    def test_buscar1(self):
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
    
    def test_buscar2(self):
        driver = self.driver
        website = "https://www.amazon.com/"
        driver.get(website)

    def test_buscar3(self):
        driver = self.driver
        website = "https://www.lapatilla.com/"
        driver.get(website)



    #Finalización de las variables(limpieza)
    def tearDown(self):
        #Cierre de Navegador
        self.driver.quit()


#Funcion para que corran los UnitTest
if __name__ == '__main__':
    unittest.main()

#############################################################



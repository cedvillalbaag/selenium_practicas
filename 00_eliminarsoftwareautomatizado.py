# ELIMINAR UN SOFTWARE DE PRUEBA ESTA CONTROLANDO CHROME ()

# Eliminar un software de prueba esta controlando chrome


#Descarga masiva de archivos pdf 
#https://www.youtube.com/watch?v=W0treuZhp5I


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

#path = 'chromedriver.exe'
#s = Service(path)
#driver = webdriver.Chrome( service = s) #Agregar


################## Unitest ##########################################
#Declarar clase
class suite(unittest.TestCase):
    #1.- Inicialización
    def setUp(self):
        chromeOptions = Options()
        chromeOptions.add_experimental_option("prefs", {
        "download.default_directory":"C://Users/ASUS/Desktop/seleniumcurso_alvarez",
        

        })
        #chromeOptions.add_experimental_option("excludeSwitches", ['enable-automation'])
        path = 'chromedriver.exe'
        s = Service(path)
        driver = webdriver.Chrome(service = s, options = chromeOptions)
        self.driver = driver


#IMPORTANTE: SIEMPRE COLOCAR TEST ANTES DEL NOMBRE DE LA FUNCION
    def test_descargandoarchivos(self):
        #driver = self.driver
        website = "https://www.w3schools.com/howto/tryit.asp?filename=tryhow_html_download_link"
        self.driver.get(website)
        time.sleep(2)
        
        #Cambiar de frame
        iframe = self.driver.find_element(By.ID,"iframeResult")
        self.driver.switch_to.frame('iframeResult')

        #time.sleep(3)
        self.driver.find_element(By.XPATH, '/html/body/p[2]/a/img').click()
        time.sleep(5)


       

    

    #Finalización de las variables(limpieza)
    def tearDown(self):
        #Cierre de Navegador
        self.driver.quit()
        print("prueba con exito")


#Funcion para que corran los UnitTest
if __name__ == '__main__':
    unittest.main()
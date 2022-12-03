#Importaciones del paquete de selenium y webdriver para poder implementar sus clases y metodos, interaccion con el navegador
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#Importacion de By para elegir locator strategy
from selenium.webdriver.common.by import By
import time


# Creamos la sesion de Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

#Acceder a la URL 
driver.get('http://www.google.com')

# queremos hacer una busqueda, para eso necesitamos escribir en la barra de google.
# lo buscamos por classname y le pasamos el nombre de la clase que leemos en el HTML

search_field = driver.find_element(By.CLASS_NAME, "gLFyf") #nos quedamos con el elemento en particular
search_field.clear() #clear borra el texto que viene por default

search_field.send_keys("selenium") #la busqueda se hace con send_keys

# ahora tenemos que hacer click en Busqueda. primero tenemos que identificar el boton al 
# que le queremos hacer click

search_button = driver.find_element(By.XPATH, '//div[@class="FPdoLc lJ9FBc"]//input[@name="btnK"]')
search_button.click()
time.sleep(3)

# nos vamos quedando con los titulos que salen de la busqueda y los guardamos en una lista 
heading_list = driver.find_elements(By.XPATH, '//h3[@class="LC20lb MBeuO DKV0Md"]')

#recorremos solamente los 10 primeros elementos y los printeamos
i = 0
for heading in heading_list:
    print(heading.get_attribute("textContent"))
    i += 1
    if(i > 10):
        break

driver.quit()

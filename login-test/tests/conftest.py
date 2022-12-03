import pytest
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from config.config import TestData

#Creamos la instancia de la sesion del browser y lo tiramos abajo
@pytest.fixture(scope="class")
def init_driver():
    if TestData.browser == "Chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver # devuelve la instancia de driver
    driver.quit()


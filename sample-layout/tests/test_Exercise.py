from pages.TextInputPage import TextInputPage
from config.config import TestData
import pytest 

class TestCase: #tiene que empezar con mayuscula
    
    def test_title(self, init_driver): # es el init_driver de conftest (asi funciona el fixture, con el mismo nombre tiene que ser)
        self.textInputPage = TextInputPage(init_driver)
        title = self.textInputPage.get_page_title()
        assert title == TestData.page_title, 'Titulo incorrecto'

    @pytest.mark.parametrize("actual, expected", [('bootcamp', 'bootcamp'), ('bootcamp', 'botcamp')])
    def test_button(self, init_driver, actual, expected):
        self.textInputPage = TextInputPage(init_driver)
        text = self.textInputPage.do_exercise(actual)
        assert text == expected, 'Texto del boton incorrecto'


#PARA PROBARLO:
    # EN ESTE ARCHIVO, BOTON DERECHO --> OPEN IN INTEGRATED TERMINAL
    # ESCRIBIR PYTEST EN LA TERMINAL Y TOCAR TAB HASTA QUE APAREZCA EL NOMBRE DEL ARCHIVO A TESTEAR (test_Exercise.py en este caso)
    # ENTER
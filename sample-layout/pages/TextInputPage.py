from pages.BasePage import BasePage
from config.config import TestData
from config.locators import Locators

class TextInputPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)
    
    def get_page_title(self):
        return self.get_title()

    def do_exercise(self, value):
        self.do_send_keys(Locators.text_input, value)
        self.do_click(Locators.text_button)
        text = self.get_element_text(Locators.text_button)
        return text

#metodos para interactuar especificamente con text input page


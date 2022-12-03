from pages.BasePage import BasePage
from config.config import TestData
from config.locators import Locators

class TextInputPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)
    
    def go_to_log_in_page(self):
        self.do_click(Locators.sample_app)

    def get_log_in_status(self):
        return self.get_element_text(Locators.login_status)

    def complete_log_in(self, usermame, password):
        self.do_send_keys(Locators.username_placeholder, usermame)
        self.do_send_keys(Locators.password_placeholder, password)
        self.do_click(Locators.login_button)
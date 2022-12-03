from pages.TextInputPage import TextInputPage
from config.config import TestData
import pytest

class TestCase: #tiene que empezar con mayuscula
    
    def test_enter_login(self, init_driver):
        self.textInputPage = TextInputPage(init_driver)
        self.textInputPage.go_to_log_in_page()
        text = self.textInputPage.get_log_in_status()
        assert text == TestData.logged_out

    @pytest.mark.parametrize("username, password, result", [("belen", "pwd", "Welcome, belen!"), 
                                                            ("belen", "pws", "Invalid username/password"),
                                                            ("", "pws", "Invalid username/password"),
                                                            ("", "pwd", "Invalid username/password"),
                                                            ("", "", "Invalid username/password"),
                                                            ("belen", "", "Invalid username/password")])
    def test_log_in(self, init_driver, username, password, result):
        self.textInputPage = TextInputPage(init_driver)

        self.textInputPage.go_to_log_in_page()
        self.textInputPage.complete_log_in(username, password)
        text = self.textInputPage.get_log_in_status()
        assert text == result
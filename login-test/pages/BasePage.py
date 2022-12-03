from selenium.webdriver.common.by import By

class BasePage:
    
    #initializer
    def __init__(self, driver):
        self.driver = driver

    def find_element_xpath(self, locator):
        return self.driver.find_element(By.XPATH, locator)

    def do_send_keys(self, locator, value):
        self.find_element_xpath(locator).send_keys(value)
        
    def do_click(self, locator):
        self.find_element_xpath(locator).click()

    def get_element_text(self, locator):
        return self.find_element_xpath(locator).text
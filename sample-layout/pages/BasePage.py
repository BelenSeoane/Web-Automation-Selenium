from selenium.webdriver.common.by import By

class BasePage:
    
    #initializer
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def find_element_xpath(self, locator):
        return self.driver.find_element(By.XPATH, locator)

    def do_send_keys(self, locator, value):
        element = self.find_element_xpath(locator)
        element.send_keys(value)

    def do_click(self, locator):
        element = self.find_element_xpath(locator)
        element.click()

    def get_element_text(self, locator):
        element = self.find_element_xpath(locator)
        text = element.text
        return text

# super clase, tiene los metodos compartidos para las demas paginas
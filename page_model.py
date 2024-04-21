
from general_page import GeneralPage
from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webelement import WebElement



class TheInternetPage(GeneralPage):

    def __init__(self, chosen_browser):
        super().__init__(url='https://the-internet.herokuapp.com/',chosen_browser=chosen_browser)

    

    def links(self) -> list[WebElement]:
        return self.browser.find_elements(By.XPATH, "//ul//a")

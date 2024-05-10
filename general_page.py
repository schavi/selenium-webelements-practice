

from selenium.webdriver import Firefox
from selenium.webdriver import Edge
from selenium.webdriver import Chrome

from selenium import webdriver
from selenium.webdriver.common.by import By

from datetime import datetime
import os

class GeneralPage:

    def __init__(self, url:str, chosen_browser:str="firefox"):
        '''
        Sets up a GeneralPage object instance.

        :param str url: The base URL of the website.
        :param str chosen_browser: Which browser to use. Accepted values are "firefox", "edge" and "chrome".
        '''

        match chosen_browser:
            case "firefox":
                options = webdriver.FirefoxOptions()
                self.browser = webdriver.Firefox(options=options)
            case "edge":
                options = webdriver.EdgeOptions()
                self.browser = webdriver.Edge()
            case "chrome":
                options = webdriver.ChromeOptions()
                self.browser = webdriver.Chrome()
            case _:
                print("Chosen browser not recognized, defaulting to Firefox.")
                options = webdriver.FirefoxOptions()
                self.browser = webdriver.Firefox(options=options)
        self.url = url

    def open(self):
        self.browser.get(self.url)
        self.browser.set_window_size(1920, 1080)
        self.browser.maximize_window()

    def close(self):
        self.browser.quit()

    def refresh(self):
        self.browser.refresh()

    def current_url(self):
        return self.browser.current_url

    def save_full_screenshot(self):
        filename = f"[{self.browser.title}]_{datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}.png"
        screenshot_path = os.path.join(os.getcwd(), 'screenshots', filename)
        print(f"Sceenshot attempt: {screenshot_path}")
        self.browser.find_element(By.TAG_NAME, "body").screenshot(screenshot_path)




from selenium import webdriver


from page_model import TheInternetPage


import pytest


class TestTheInternetPageFirefox:

    BASEURL = "https://the-internet.herokuapp.com/"

    def setup_method(self):
        self.page = TheInternetPage(chosen_browser="firefox")

        self.page.browser.implicitly_wait(7)

        self.page.open()

    def teardown_method(self):
        self.page.close()

    

    def test_links(self):
        for link in self.page.links():
            print(link.text)





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
        for link in self.page.main_links():
            print(link.text)

    

    def test_basic_auth(self):
        #load http://admin:admin@url then click on link and check if autenthicated
        #confirmation popups will come up that need to be handled
        pass



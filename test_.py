

from selenium import webdriver
from selenium.webdriver import ActionChains

from page_model import TheInternetPage

from time import sleep

import pytest


class TestTheInternetPageFirefox:

    BASEURL = "https://the-internet.herokuapp.com/"

    def setup_method(self):
        self.page = TheInternetPage(chosen_browser="firefox")

        self.page.browser.implicitly_wait(3)

        self.page.open()

    def teardown_method(self):
        self.page.close()

    

    def test_links(self):
        for link in self.page.main_links():
            print(link.text)

    
    def test_add_remove(self):
        link_text = "Add/Remove Elements"
        self.page.main_links()[1][self.page.main_links()[0].index(link_text)].click()
        assert len(self.page.add_remove_delete_buttons()) == 0, "Added elements already present"
        self.page.add_remove_add_button().click()
        assert len(self.page.add_remove_delete_buttons()) == 1, f"Page should have 1 added element; has {len(self.page.add_remove_delete_buttons())}"
        self.page.add_remove_add_button().click()
        assert len(self.page.add_remove_delete_buttons()) == 2, f"Page should have 2 added elements; has {len(self.page.add_remove_delete_buttons())}"
        self.page.add_remove_delete_buttons()[0].click()
        assert len(self.page.add_remove_delete_buttons()) == 1, f"Page should have 1 added element; has {len(self.page.add_remove_delete_buttons())}"
        self.page.add_remove_delete_buttons()[0].click()
        assert len(self.page.add_remove_delete_buttons()) == 0, "Added elements not removed"


    def test_checkboxes(self):
        link_text = "Checkboxes"
        self.page.main_links()[1][self.page.main_links()[0].index(link_text)].click()
        assert self.page.checkboxes_1_checkbox().get_attribute("checked") == None, "Checkbox 1 was already checked"
        assert self.page.checkboxes_2_checkbox().get_attribute("checked") == "true", "Checkbox 2 was already unchecked"
        self.page.checkboxes_1_checkbox().click()
        assert self.page.checkboxes_1_checkbox().get_attribute("checked") == "true", "Couldn't check checkbox 1"
        self.page.checkboxes_2_checkbox().click()
        assert self.page.checkboxes_2_checkbox().get_attribute("checked") == None, "Couldn't uncheck checkbox 2"

    
    def test_context_menu(self):
        link_text = "Context Menu"
        self.page.main_links()[1][self.page.main_links()[0].index(link_text)].click()
        action_chains = ActionChains(self.page.browser)
        action_chains.context_click(self.page.context_menu_hotspot()).perform()
        try:
            self.page.browser.switch_to.alert.accept()
        except:
            assert False, "Alert wasn't found"


    def test_drag_and_drop(self):
        link_text = "Drag and Drop"
        self.page.main_links()[1][self.page.main_links()[0].index(link_text)].click()
        assert self.page.drag_and_drop_content_A() == "A", "Default content should be 'A'"
        assert self.page.drag_and_drop_content_B() == "B", "Default content should be 'B'"
        action_chains = ActionChains(self.page.browser)
        action_chains.drag_and_drop(self.page.drag_and_drop_div_A(),self.page.drag_and_drop_div_B()).perform()  # TODO it doesn't "let go" of the element properly
        assert self.page.drag_and_drop_content_A() == "B", "Content should be 'B'"
        assert self.page.drag_and_drop_content_B() == "A", "Content should be 'A'"

    
    def test_dropdown_list(self):
        link_text = "Dropdown"
        self.page.main_links()[1][self.page.main_links()[0].index(link_text)].click()
        self.page.dropdown_select().select_by_value("1")
        assert self.page.dropdown_options()[1].get_attribute("selected") == "true", "Failed to select option 1"
        self.page.dropdown_select().select_by_value("2")
        assert self.page.dropdown_options()[2].get_attribute("selected") == "true", "Failed to select option 2"


    def test_dynamic_controls(self):
        pass


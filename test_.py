

from page_model import TheInternetPage

from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

import pytest

from random import choice as randomchoice



class TestTheInternetPageFirefox:

    PROTOCOL ="https://"
    BASEURL = "the-internet.herokuapp.com/"

    def setup_method(self):
        self.page = TheInternetPage(chosen_browser="firefox")

        self.page.browser.implicitly_wait(3)

        self.page.open()

    def teardown_method(self):
        self.page.close()

    

    def test_links(self):
        for link in self.page.main_links():
            print(link.text)

    
    # A-B testing


    # Add/Remove Elements
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


    # Basic Auth
    @pytest.mark.parametrize("username, password, valid", [("admin", "admin", True),
                                                           ("invalid", "invalid", False)
                                                          ])
    def test_basic_auth(self, username, password, valid):
        self.page.browser.get(self.PROTOCOL + username + ":" + password + "@" + self.BASEURL + "/basic_auth")
        if valid:
            assert self.page.basic_auth_success_mesage() != None, "Success message wasn't found"
        else:
            self.page.browser.switch_to.alert.dismiss()     # invalid credentials make the authorization alert pop-up
            assert "Not authorized" in self.page.browser.page_source, "Couldn't find 'Not authorized' message on page"


    # Broken images


    # Challenging DOM
    def test_challenging_dom_buttons(self):
        link_text = "Challenging DOM"
        self.page.main_links()[1][self.page.main_links()[0].index(link_text)].click()
        blue_button_color = "rgb(43, 166, 203)"
        red_button_color = "rgb(198, 15, 19)"
        green_button_color = "rgb(93, 164, 35)"
        assert self.page.challenging_dom_blue_button().value_of_css_property("background-color") == blue_button_color
        assert self.page.challenging_dom_red_button().value_of_css_property("background-color") == red_button_color
        assert self.page.challenging_dom_green_button().value_of_css_property("background-color") == green_button_color


    def test_challenging_dom_table_contents(self):
        link_text = "Challenging DOM"
        self.page.main_links()[1][self.page.main_links()[0].index(link_text)].click()
        for column_name in self.page.challenging_dom_table_header():
            print(column_name, end=" ")
        print("\n")
        for row in self.page.challenging_dom_table_content():
            for column in row:
                print(column, end=" ")
            print()
        print("\n")


    # Checkboxes
    def test_checkboxes(self):
        link_text = "Checkboxes"
        self.page.main_links()[1][self.page.main_links()[0].index(link_text)].click()
        assert self.page.checkboxes_1_checkbox().get_attribute("checked") == None, "Checkbox 1 was already checked"
        assert self.page.checkboxes_2_checkbox().get_attribute("checked") == "true", "Checkbox 2 was already unchecked"
        self.page.checkboxes_1_checkbox().click()
        assert self.page.checkboxes_1_checkbox().get_attribute("checked") == "true", "Couldn't check checkbox 1"
        self.page.checkboxes_2_checkbox().click()
        assert self.page.checkboxes_2_checkbox().get_attribute("checked") == None, "Couldn't uncheck checkbox 2"

    
    # Context Menu
    def test_context_menu(self):
        link_text = "Context Menu"
        self.page.main_links()[1][self.page.main_links()[0].index(link_text)].click()
        action_chains = ActionChains(self.page.browser)
        action_chains.context_click(self.page.context_menu_hotspot()).perform()
        try:
            self.page.browser.switch_to.alert.accept()
        except:
            assert False, "Alert wasn't found"


    # Digest auth

    # Disappearing elements


    # Drag and Drop
    def test_drag_and_drop(self):
        link_text = "Drag and Drop"
        self.page.main_links()[1][self.page.main_links()[0].index(link_text)].click()
        assert self.page.drag_and_drop_content_A() == "A", "Default content should be 'A'"
        assert self.page.drag_and_drop_content_B() == "B", "Default content should be 'B'"
        action_chains = ActionChains(self.page.browser)
        action_chains.drag_and_drop(self.page.drag_and_drop_div_A(),self.page.drag_and_drop_div_B()).perform()  # TODO it doesn't "let go" of the element properly
        assert self.page.drag_and_drop_content_A() == "B", "Content should be 'B'"
        assert self.page.drag_and_drop_content_B() == "A", "Content should be 'A'"

    
    # Dropdown
    def test_dropdown_list(self):
        link_text = "Dropdown"
        self.page.main_links()[1][self.page.main_links()[0].index(link_text)].click()
        self.page.dropdown_select().select_by_value("1")
        assert self.page.dropdown_options()[1].get_attribute("selected") == "true", "Failed to select option 1"
        self.page.dropdown_select().select_by_value("2")
        assert self.page.dropdown_options()[2].get_attribute("selected") == "true", "Failed to select option 2"


    # Dynamic content

    # Dynamic controls

    # Dynamic loading


    # Entry ad
    def test_entry_ad(self):
        link_text = "Entry Ad"
        self.page.main_links()[1][self.page.main_links()[0].index(link_text)].click()
        assert self.page.entry_ad_window_is_visible(), "Couldn't locate ad window"
        self.page.entry_ad_close().click()
        assert not self.page.entry_ad_window_is_visible(), "The ad window didn't close"

    # Exit intent


    # File Download
    def test_file_download(self):
        link_text = "File Download"
        self.page.main_links()[1][self.page.main_links()[0].index(link_text)].click()
        randomchoice(self.page.file_download_links()).click()
        # TODO check result


    # File upload--TODO--

    # Floating Menu

    # Forgot Password

    # Form Authentication--TODO----NEXT--

    # Frames--TODO----NEXT--

    # Geolocation

    # Horizontal Slider--TODO----NEXT--

    # Hovers--TODO--

    # Infinite Scroll--TODO--

    # Inputs

    # JQuery UI Menus--TODO--

    # JavaScript Alerts--TODO--

    # JavaScript onload event error

    # Key Presses--TODO----NEXT--

    # Large & Deep DOM

    # Multiple Windows--TODO----NEXT--

    # Nested Frames--TODO----NEXT--

    # Notification Messages

    # Redirect Link

    # Secure File Download

    # Shadow DOM--TODO--

    # Shifting Content

    # Slow Resources--TODO--

    # Sortable Data Tables

    # Status Codes

    # Typos

    # WYSIWYG Editor--TODO--


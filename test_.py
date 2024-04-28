

from page_model import TheInternetPage

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

import pytest

from random import choice as randomchoice



class TestTheInternetPageFirefox:

    PROTOCOL ="https://"
    BASEURL = "the-internet.herokuapp.com"

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

    # File upload--TODO--

    # Floating Menu

    # Forgot Password


    # Form Authentication
    def test_form_authentication_login(self):
        link_text = "Form Authentication"
        self.page.main_links()[1][self.page.main_links()[0].index(link_text)].click()
        self.page.form_auth_username_field().send_keys(self.page.form_auth_username())
        self.page.form_auth_password_field().send_keys(self.page.form_auth_password())
        self.page.form_auth_login_button().click()
        assert self.page.form_auth_login_alert_status() == "success", "Login failed"
    
    def test_form_authentication_login_invalid(self):
        link_text = "Form Authentication"
        self.page.main_links()[1][self.page.main_links()[0].index(link_text)].click()
        self.page.form_auth_username_field().send_keys("username")
        self.page.form_auth_password_field().send_keys("invalidpass")
        self.page.form_auth_login_button().click()
        assert self.page.form_auth_login_alert_status() == "error", "Error alert not found"
    
    # Uses test_form_authentication_login()
    def test_form_authentication_logout(self):
        self.test_form_authentication_login()
        self.page.form_auth_logout_button().click()
        assert self.page.form_auth_login_alert_status() == "success", "Logout alert not found"


    # Frames
    def test_frames_nested_frames(self):
        link_text = "Frames"
        self.page.main_links()[1][self.page.main_links()[0].index(link_text)].click()
        self.page.frames_nested_frames_link().click()
        self.page.browser.switch_to.frame(self.page.frames_nested_bottom())
        assert "BOTTOM" in self.page.browser.page_source, "Couldn't switch to bottom frame"
        self.page.browser.switch_to.default_content()
        self.page.browser.switch_to.frame(self.page.frames_nested_top())
        self.page.browser.switch_to.frame(self.page.frames_nested_top_left())
        assert "LEFT" in self.page.browser.page_source, "Couldn't switch to top left frame"
        self.page.browser.switch_to.default_content()
        self.page.browser.switch_to.frame(self.page.frames_nested_top())
        self.page.browser.switch_to.frame(self.page.frames_nested_top_middle())
        assert "MIDDLE" in self.page.browser.page_source, "Couldn't switch to top middle frame"
        self.page.browser.switch_to.default_content()
        self.page.browser.switch_to.frame(self.page.frames_nested_top())
        self.page.browser.switch_to.frame(self.page.frames_nested_top_right())
        assert "RIGHT" in self.page.browser.page_source, "Couldn't switch to top right frame"

    def test_frames_iframe(self):
        link_text = "Frames"
        self.page.main_links()[1][self.page.main_links()[0].index(link_text)].click()
        self.page.frames_iframe_link().click()
        self.page.browser.switch_to.frame(self.page.frames_iframe_editor_iframe())
        assert self.page.frames_iframe_editor_content().text == "Your content goes here.", "Couldn't fetch content from editor inside iframe"


    # Geolocation


    # Horizontal Slider
    def test_horizontal_slider(self):
        link_text = "Horizontal Slider"
        self.page.main_links()[1][self.page.main_links()[0].index(link_text)].click()
        self.page.horizontal_slider_slider().send_keys(Keys.ARROW_RIGHT * 6)
        assert self.page.horizontal_slider_value() == 3, "Couldn't increase slider value with keys"
        self.page.horizontal_slider_slider().send_keys(Keys.ARROW_LEFT * 5)
        assert self.page.horizontal_slider_value() == 0.5, "Couldn't decrease slider value with keys"


    # Hovers
    def test_hovers(self):
        link_text = "Hovers"
        self.page.main_links()[1][self.page.main_links()[0].index(link_text)].click()
        actions = ActionChains(self.page.browser)
        actions.move_to_element(self.page.hovers_images()[1]).perform()
        assert self.page.hovers_names()[1].is_displayed(), "Info wasn't displayed on hover"


    # Infinite Scroll--TODO--

    # Inputs

    # JQuery UI Menus--TODO--

    # JavaScript Alerts--TODO--

    # JavaScript onload event error


    # Key Presses
    def test_key_presses(self):
        link_text = "Key Presses"
        self.page.main_links()[1][self.page.main_links()[0].index(link_text)].click()
        self.page.key_presses_input().send_keys("abc")
        assert self.page.key_presses_result() == "C", "Didn't return correct keypress (letters)"
        self.page.key_presses_input().send_keys(Keys.BACK_SPACE)
        assert self.page.key_presses_result() == "BACK_SPACE", "Didn't return correct keypress (special)"
        self.page.key_presses_input().send_keys(Keys.ARROW_LEFT)
        assert self.page.key_presses_result() == "LEFT", "Didn't return correct keypress (navigation)"
        self.page.key_presses_input().send_keys(Keys.F1)
        assert self.page.key_presses_result() == "F1", "Didn't return correct keypress (function)"
        self.page.key_presses_input().send_keys(".")
        assert self.page.key_presses_result() == "PERIOD", "Didn't return correct keypress (punctuation)"


    # Large & Deep DOM


    # Multiple Windows
    def test_multiple_windows(self):
        link_text = "Multiple Windows"
        self.page.main_links()[1][self.page.main_links()[0].index(link_text)].click()
        self.page.multple_windows_new_window_link().click()
        windows = self.page.browser.window_handles
        assert len(windows) == 2, "New window didn't open"


    # Nested Frames - this exists under Frames

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


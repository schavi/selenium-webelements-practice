
from general_page import GeneralPage
from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select




class TheInternetPage(GeneralPage):

    def __init__(self, chosen_browser):
        super().__init__(url='https://the-internet.herokuapp.com/',chosen_browser=chosen_browser)

    

    def main_links(self) -> list[WebElement]:
        return self.browser.find_elements(By.XPATH, "//ul//a")


    #A-B testing


    def add_remove_add_button(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//button[@onclick='addElement()']")

    def add_remove_delete_buttons(self) -> list[WebElement]:
        return self.browser.find_elements(By.XPATH, "//button[@onclick='deleteElement()']")


    #Basic auth

    #Broken images

    #Challenging dom


    def checkboxes_1_checkbox(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//form[@id='checkboxes']/input[@type='checkbox']")
    
    def checkboxes_2_checkbox(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//form[@id='checkboxes']/input[@type='checkbox'][2]")


    
    def context_menu_hotspot(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//div[@id='hot-spot']")


    #Digest auth


    def disappearing_elements_home_link(self) -> WebElement:
        element_text = "Home"
        return self.browser.find_element(By.XPATH, f"//a[text()='{element_text}']")
    
    def disappearing_elements_about_link(self) -> WebElement:
        element_text = "About"
        return self.browser.find_element(By.XPATH, f"//a[text()='{element_text}']")
    
    def disappearing_elements_contact_link(self) -> WebElement:
        element_text = "Contact Us"
        return self.browser.find_element(By.XPATH, f"//a[text()='{element_text}']")
    
    def disappearing_elements_portfolio_link(self) -> WebElement:
        element_text = "Portfolio"
        return self.browser.find_element(By.XPATH, f"//a[text()='{element_text}']")
    
    def disappearing_elements_gallery_link(self) -> WebElement:
        element_text = "Gallery"
        return self.browser.find_element(By.XPATH, f"//a[text()='{element_text}']")
    


    def drag_and_drop_div_A(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//div[@id='column-a']")

    def drag_and_drop_div_B(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//div[@id='column-b']")
    
    def drag_and_drop_content_A(self) -> str:
        return self.drag_and_drop_div_A.find_element(By.XPATH, "/header") #./header or its fine this way?

    def drag_and_drop_content_B(self) -> str:
        return self.drag_and_drop_div_B.find_element(By.XPATH, "/header")


    
    def dropdown_select(self) -> Select:
        return Select(self.browser.find_element(By.XPATH, "//select"))
    
    def dropdown_options(self) -> list[WebElement]:
        return self.browser.find_elements(By.XPATH, "//option")


    #Dynamic content


    def dynamic_controls_checkbox(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//form[@id='checkbox-example']//input[@type='checkbox']")
    
    def dynamic_controls_remove_button(self) -> WebElement:
        element_text = "Remove"
        return self.browser.find_element(By.XPATH, f"//form[@id='checkbox-example']//button[text()='{element_text}']")

    def dynamic_controls_add_button(self) -> WebElement:
        element_text = "Add"
        return self.browser.find_element(By.XPATH, f"//form[@id='checkbox-example']//button[text()='{element_text}']")

    def dynamic_controls_textfield(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//form[@id='input-example']//input[@type='text']")
    
    def dynamic_controls_enable_button(self) -> WebElement:
        element_text = "Enable"
        return self.browser.find_element(By.XPATH, f"//form[@id='input-example']//button[text()='{element_text}']")

    def dynamic_controls_disable_button(self) -> WebElement:
        element_text = "Disable"
        return self.browser.find_element(By.XPATH, f"//form[@id='input-example']//button[text()='{element_text}']")

    
    #Dynamic loading

    #Entry ad

    #Exit intent

    #File download

    #File upload

    # Floating Menu

    # Forgot Password

    # Form Authentication

    # Frames

    # Geolocation

    # Horizontal Slider

    # Hovers

    # Infinite Scroll

    # Inputs

    # JQuery UI Menus

    # JavaScript Alerts

    # JavaScript onload event error

    # Key Presses

    # Large & Deep DOM

    # Multiple Windows

    # Nested Frames

    # Notification Messages

    # Redirect Link

    # Secure File Download

    # Shadow DOM

    # Shifting Content

    # Slow Resources

    # Sortable Data Tables

    # Status Codes

    # Typos

    # WYSIWYG Editor




from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

from general_page import GeneralPage



class TheInternetPage(GeneralPage):

    def __init__(self, chosen_browser):
        super().__init__(url='https://the-internet.herokuapp.com/',chosen_browser=chosen_browser)

    

    def main_links(self) -> tuple[list[str],list[WebElement]]:
        link_elements = self.browser.find_elements(By.XPATH, "//ul//a")
        return ([element.text for element in link_elements], link_elements)


    # A-B testing


    def add_remove_add_button(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//button[@onclick='addElement()']")

    def add_remove_delete_buttons(self) -> list[WebElement]:
        return self.browser.find_elements(By.XPATH, "//button[@onclick='deleteElement()']")


    
    def basic_auth_success_mesage(self) -> str:
        return self.browser.find_element(By.XPATH, "//div[@class='example']//p").text


    # Broken images


    def challenging_dom_blue_button(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//div[@class='row']//div[@class='large-2 columns']//a[1]")

    def challenging_dom_red_button(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//div[@class='row']//div[@class='large-2 columns']//a[2]")

    def challenging_dom_green_button(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//div[@class='row']//div[@class='large-2 columns']//a[3]")

    def challenging_dom_table_header(self) -> list[str]:
        return [element.text for element in self.browser.find_elements(By.XPATH, "//div[@class='row']//div[@class='large-10 columns']//thead//th")]
    
    def challenging_dom_table_content(self) -> list[list[str]]:
        no_of_rows = len(self.browser.find_elements(By.XPATH, "//div[@class='row']//div[@class='large-10 columns']//tbody//tr"))
        content = []
        for i in range(no_of_rows):
            content.append([element.text for element in self.browser.find_elements(By.XPATH, f"//div[@class='row']//div[@class='large-10 columns']//tbody//tr[{i+1}]/td")])
        return content


    def checkboxes_1_checkbox(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//form[@id='checkboxes']/input[@type='checkbox']")
    
    def checkboxes_2_checkbox(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//form[@id='checkboxes']/input[@type='checkbox'][2]")


    
    def context_menu_hotspot(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//div[@id='hot-spot']")


    # Digest auth


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
        return self.drag_and_drop_div_A().find_element(By.XPATH, "./header").text

    def drag_and_drop_content_B(self) -> str:
        return self.drag_and_drop_div_B().find_element(By.XPATH, "./header").text


    
    def dropdown_select(self) -> Select:
        return Select(self.browser.find_element(By.XPATH, "//select"))
    
    def dropdown_options(self) -> list[WebElement]:
        return self.browser.find_elements(By.XPATH, "//option")


    # Dynamic content

    # Dynamic controls
    
    # Dynamic loading

    # Entry ad--TODO----NEXT--

    # Exit intent

    
    def file_download_links(self) -> list[WebElement]:
        return self.browser.find_elements(By.XPATH, "//div[@class='example']//a")


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


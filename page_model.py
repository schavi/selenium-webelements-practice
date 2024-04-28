

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from general_page import GeneralPage



class TheInternetPage(GeneralPage):

    def __init__(self, chosen_browser):
        super().__init__(url='https://the-internet.herokuapp.com/',chosen_browser=chosen_browser)

    

    def main_links(self) -> tuple[list[str],list[WebElement]]:
        link_elements = self.browser.find_elements(By.XPATH, "//ul//a")
        return ([element.text for element in link_elements], link_elements)


    # A-B testing


    # Add/Remove Elements
    def add_remove_add_button(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//button[@onclick='addElement()']")

    def add_remove_delete_buttons(self) -> list[WebElement]:
        return self.browser.find_elements(By.XPATH, "//button[@onclick='deleteElement()']")


    # Basic Auth
    def basic_auth_success_mesage(self) -> str:
        return self.browser.find_element(By.XPATH, "//div[@class='example']//p").text


    # Broken images


    # Challenging DOM
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


    # Checkboxes
    def checkboxes_1_checkbox(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//form[@id='checkboxes']/input[@type='checkbox']")
    
    def checkboxes_2_checkbox(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//form[@id='checkboxes']/input[@type='checkbox'][2]")


    # Context Menu
    def context_menu_hotspot(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//div[@id='hot-spot']")


    # Digest auth

    # Disappearing Elements

    # Drag and Drop


    # Dropdown
    def dropdown_select(self) -> Select:
        return Select(self.browser.find_element(By.XPATH, "//select"))
    
    def dropdown_options(self) -> list[WebElement]:
        return self.browser.find_elements(By.XPATH, "//option")


    # Dynamic content

    # Dynamic controls
    
    # Dynamic loading


    # Entry ad
    def entry_ad_window_is_visible(self) -> bool:
        try:
            WebDriverWait(self.browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='modal']")))
        except:
            return False
        return True

    def entry_ad_close(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//div[@class='modal-footer']")


    # Exit intent
    
    # File Download


    # File upload
    def file_upload_file_input(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//input[@id='file-upload']")
    
    def file_upload_upload_button(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//input[@id='file-submit']")
    
    def file_upload_uploaded_filename(self) -> str:
        return self.browser.find_element(By.XPATH, "//div[@id='uploaded-files']").text


    # Floating Menu

    # Forgot Password


    # Form Authentication
    def form_auth_username(self) -> str:
        return self.browser.find_element(By.XPATH, "//h4//em[1]").text

    def form_auth_password(self) -> str:
        return self.browser.find_element(By.XPATH, "//h4//em[2]").text

    def form_auth_username_field(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//input[@id='username']")

    def form_auth_password_field(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//input[@id='password']")

    def form_auth_login_button(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//button[@type='submit']")
    
    def form_auth_login_alert_status(self) -> str:
        '''
        Returns "success" or "error".
        '''

        # The class of this element is either "flash success" or "flash error"
        return self.browser.find_element(By.XPATH, "//div[@id='flash']").get_attribute("class")[6:]

    def form_auth_logout_button(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//a[@href='/logout']")


    # Frames
    def frames_nested_frames_link(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//a[@href='/nested_frames']")
    
    def frames_iframe_link(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//a[@href='/iframe']")
    
    def frames_nested_top(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//frame[@src='/frame_top']")
    
    def frames_nested_top_left(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//frame[@src='/frame_left']")
    
    def frames_nested_top_middle(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//frame[@src='/frame_middle']")
    
    def frames_nested_top_right(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//frame[@src='/frame_right']")
    
    def frames_nested_bottom(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//frame[@src='/frame_bottom']")

    def frames_iframe_editor_iframe(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//div[@class='example']//div[@class='tox-edit-area']/iframe")
    
    def frames_iframe_editor_content(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//p")


    # Geolocation


    # Horizontal Slider
    def horizontal_slider_slider(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//input[@type='range']")
    
    def horizontal_slider_value(self) -> float:
        '''
        Returns a value from {0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5}. 
        '''

        return float(self.browser.find_element(By.XPATH, "//span[@id='range']").text)


    # Hovers
    def hovers_images(self) -> list[WebElement]:
        return self.browser.find_elements(By.XPATH, "//div[@class='example']//img")
    
    def hovers_names(self) -> list[WebElement]:
        return self.browser.find_elements(By.XPATH, "//div[@class='figcaption']/h5")


    # Infinite Scroll
    def infinite_scroll_content(self) -> list[WebElement]:
        return self.browser.find_elements(By.XPATH, "//div[@class='jscroll-added']")


    # Inputs


    # JQuery UI Menus
    def jquery_ui_menus_enabled_item(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//ul[@id='menu']/li[2]")
        
    def jquery_ui_menus_back_to_jquery_ui_item(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//ul[@id='menu']/li[2]/ul/li[2]")


    # JavaScript Alerts
    def javascript_alerts_alert_button(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
    
    def javascript_alerts_confirm_button(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    
    def javascript_alerts_prompt_button(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    
    def javascript_alerts_result(self) -> str:
        return self.browser.find_element(By.XPATH, "//p[@id='result']").text


    # JavaScript onload event error


    # Key Presses
    def key_presses_input(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//input[@id='target']")
    
    def key_presses_result(self) -> str:
        # Text of this element is "You entered: {Key}"
        return self.browser.find_element(By.XPATH, "//p[@id='result']").text[13:]
    

    # Large & Deep DOM
    # This is just to test the usage of XPath axes
    def large_deep_dom_412_div(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//div[@id='sibling-45.2']//ancestor::div[5]//child::div[1]")


    # Multiple Windows
    def multple_windows_new_window_link(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//a[text()='Click Here']")


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


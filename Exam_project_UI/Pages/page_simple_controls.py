
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from Exam_project_UI.data.valid_email_name import email,name



class PageCheckElements:
    URL = 'https://ultimateqa.com/simple-html-elements-for-automation/'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.click_me_button_loc = '//a[text()="Click Me"]'
        self.name_field = '//input[@id="et_pb_contact_name_0"]'
        self.email_field = '//input[@id="et_pb_contact_email_0"]'
        self.Email_Me_button = '//button[@name="et_builder_submit_button"]'
        self.checkbox_radio_button_loc = '//input[@value="{}"]'
        self.dropdown_menu_loc = '//select'
        self.dropdown_element = '//*[text()="{}"]'


    def open(self):
        self.driver.get(self.URL)
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()

    # Check_button

    def check_button_is_clickable(self):
        self.driver.find_element(By.XPATH, self.click_me_button_loc).click()

    def check_page_url_after_click_button(self, page_result):
        return self.driver.current_url == f'https://ultimateqa.com/{page_result}/'

    # fill fields

    def filling_out_name_field(self):
        self.driver.find_element(By.XPATH, self.name_field).send_keys(name)

    def filling_out_email_field(self):
        self.driver.find_element(By.XPATH, self.email_field).send_keys(email)

    def click_email_me_button(self):
        self.driver.find_element(By.XPATH, self.Email_Me_button).click()

    def check_result_after_filling_fields(self):
        return self.driver.find_element(By.XPATH, '//p[text()="Thanks for contacting us"]').text

    # Radio Buttons

    def select_radio_button(self, value):
        locator = self.driver.find_element(By.XPATH, self.checkbox_radio_button_loc.format(value))
        locator.click()

    def check_radio_button_is_selected(self, value):
        result = self.driver.find_element(By.XPATH, self.checkbox_radio_button_loc.format(value))
        return result.is_selected()

    # Check Box

    def check_folder(self, value: str):
        element = self.driver.find_element(By.XPATH, self.checkbox_radio_button_loc.format(value))
        if not element.is_selected():
            element.click()
        else:
            print("CheckBox is selected")

    def select_check_boxes_from_list(self, boxes: list):
        for box in boxes:
            self.check_folder(box)

    def check_boxes_are_selected(self,boxes):
        for box in boxes:
            element = self.driver.find_element(By.XPATH, self.checkbox_radio_button_loc.format(box))
            if not element.is_selected():
                return False
        return True


    # Dropdown

    def expand_dropdown_menu(self):
        self.driver.find_element(By.XPATH, self.dropdown_menu_loc).click()

    def select_element_from_dropdown_menu(self, value):
        self.driver.find_element(By.XPATH, self.dropdown_element.format(value)).click()

    def option_check(self, value):
        result = self.driver.find_element(By.XPATH, self.dropdown_element.format(value))
        return result.is_selected()






















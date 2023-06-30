from selenium.webdriver.common.by import By

from base.base_element import BaseElement
from base.base_page import BasePage


class TextBoxPage(BasePage):
    TEXT_BOX_BUTTON = "//*[contains(@class,'accordion')]//span[contains(text(),'Text Box')]"
    FULL_NAME_FIELD = "//*[@id='userName']"
    EMAIL_FIELD = "//*[@id='userEmail']"
    CURRENT_ADDRESS_FIELD = "//*[@id='currentAddress']"
    PERMANENT_ADDRESS_FIELD = "//*[@id='permanentAddress']"
    SUBMIT_BUTTON = "//*[@id='submit']"
    ERROR_EMAIL_FIELD = "//*[contains(@class,'field-error')]"
    FULL_NAME_OUTPUT = "//*[@id='output']//*[@id='name']"
    EMAIL_OUTPUT = "//*[@id='output']//*[@id='email']"
    CURRENT_ADDRESS_OUTPUT = "//*[@id='output']//*[@id='currentAddress']"
    PERMANENT_ADDRESS_OUTPUT = "//*[@id='output']//*[@id='permanentAddress']"

    def select_textbox_from_list(self):
        BaseElement(By.XPATH, self.TEXT_BOX_BUTTON).find_element().click()

    def enter_full_name(self, text):
        BaseElement(By.XPATH, self.FULL_NAME_FIELD).find_element().send_keys(text)

    def enter_email(self, text):
        BaseElement(By.XPATH, self.EMAIL_FIELD).find_element().send_keys(text)

    def enter_current_address(self, text):
        BaseElement(By.XPATH, self.CURRENT_ADDRESS_FIELD).find_element().send_keys(text)

    def enter_permanent_address(self, text):
        BaseElement(By.XPATH, self.PERMANENT_ADDRESS_FIELD).find_element().send_keys(text)

    def click_submit_button(self):
        BaseElement(By.XPATH, self.SUBMIT_BUTTON).find_element().click()

    def is_display_error_email(self):
        if BaseElement(By.XPATH, self.ERROR_EMAIL_FIELD).find_element():
            return False
        else:
            return True



    def get_output_full_name(self):
        return BaseElement(By.XPATH, self.FULL_NAME_OUTPUT).find_element().text

    def is_validate_output_full_name(self, expected_text):
        return expected_text in BaseElement(By.XPATH, self.FULL_NAME_OUTPUT).find_element().text

    def get_output_output_email(self):
        return BaseElement(By.XPATH, self.EMAIL_OUTPUT).find_element().text

    def is_validate_output_email(self, expected_text):
        return expected_text in BaseElement(By.XPATH, self.EMAIL_OUTPUT).find_element().text

    def get_output_current_address(self):
        return BaseElement(By.XPATH, self.CURRENT_ADDRESS_OUTPUT).find_element().text

    def is_validate_current_address(self, expected_text):
        return expected_text in BaseElement(By.XPATH, self.CURRENT_ADDRESS_OUTPUT).find_element().text

    def get_output_permanent_address(self):
        return BaseElement(By.XPATH, self.PERMANENT_ADDRESS_OUTPUT).find_element().text

    def is_validate_permanent_address(self, expected_text):
        return expected_text in BaseElement(By.XPATH, self.PERMANENT_ADDRESS_OUTPUT).find_element().text

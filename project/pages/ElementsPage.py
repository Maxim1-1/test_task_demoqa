from selenium.webdriver.common.by import By

from base.base_element import BaseElement
from base.base_page import BasePage


class ElementsPage(BasePage):
    ELEMENTS_HEADER = "//*[contains(@class,'main-header')]"
    ELEMENT_BUTTON_IN_LIST = "//*[contains(text(),'Elements')]/../*[@class='header-right']"

    def get_headers_page(self):
        return BaseElement(By.XPATH, self.ELEMENTS_HEADER).find_element().text

    def click_button_element(self):
        return BaseElement(By.XPATH, self.ELEMENT_BUTTON_IN_LIST).find_element().click()

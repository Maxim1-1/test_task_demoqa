from selenium.webdriver.common.by import By

from base.base_element import BaseElement
from base.base_page import BasePage


class MainPage(BasePage):
    BUTTON_ELEMENTS = "//*[contains(@class,'category-cards')]//*[contains(text(),'Elements')]"

    def button_element_click_(self):
        BaseElement(By.XPATH, self.BUTTON_ELEMENTS).find_element().click()
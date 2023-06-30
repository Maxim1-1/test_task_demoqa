from selenium.webdriver.common.by import By

from base.base_element import BaseElement
from base.base_page import BasePage


class AlertsFrameWindowsPage(BasePage):
    BROWSER_WINDOW_BUTTON_MENU = "//*[contains(@class,'accordion')]//span[contains(text(),'Browser Windows')]"
    NEW_TAB_BUTTON = "//button[contains(@id,'tabButton')]"
    ALERTS_FRAME_WINDOW = "//*[contains(text(),'Alerts, Frame & Windows')]/../*[@class='header-right']"
    NEW_TAB_TEXT = "//*[@id='sampleHeading']"

    def select_browser_window_from_list(self):
        BaseElement(By.XPATH, self.BROWSER_WINDOW_BUTTON_MENU).find_element().click()

    def new_button_click(self):
        BaseElement(By.XPATH, self.NEW_TAB_BUTTON).find_element().click()

    def alerts_frame_windows_click(self):
        BaseElement(By.XPATH, self.ALERTS_FRAME_WINDOW).find_element().click()

    def is_validate_open_new_tab(self):
        text = BaseElement(By.XPATH, self.NEW_TAB_TEXT).find_element().text
        if text:
            return True
        else:
            return False

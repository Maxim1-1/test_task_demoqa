from selenium.webdriver.common.by import By

from base.base_element import BaseElement
from base.base_page import BasePage
from base.browser import Browser


class AlertsFrameWindowsPage(BasePage):
    BROWSER_WINDOW_BUTTON_MENU = "//*[contains(@class,'accordion')]//span[contains(text(),'Browser Windows')]"
    NEW_TAB_BUTTON = "//button[contains(@id,'tabButton')]"
    ALERTS_FRAME_WINDOW = "//*[contains(text(),'Alerts, Frame & Windows')]/../*[@class='header-right']"

    def select_browser_window_from_list(self):
        BaseElement(By.XPATH, self.BROWSER_WINDOW_BUTTON_MENU).find_element().click()

    def new_button_click(self):
        BaseElement(By.XPATH, self.NEW_TAB_BUTTON).find_element().click()

    def alerts_frame_windows_click(self):
        BaseElement(By.XPATH, self.ALERTS_FRAME_WINDOW).find_element().click()

    def get_current_tab(self):
        driver = Browser().get_instance()
        return driver.current_window_handle

    def switch_to_new_tab(self, tab):
        driver = Browser().get_instance()
        driver.switch_to.window(tab)

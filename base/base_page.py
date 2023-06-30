from base.browser import Browser


class BasePage:
    def refresh_page(self):
        Browser().get_instance().refresh_page()

    def get_current_tab(self):
        driver = Browser().get_instance()
        return driver.current_window_handle

    def switch_to_new_tab(self, tab):
        driver = Browser().get_instance()
        driver.switch_to.window(tab)

    def switch_to_last_tab(self):
        driver = Browser().get_instance()
        return self.switch_to_new_tab(driver.window_handles[-1])

    def get_all_tabs(self):
        driver = Browser().get_instance()
        return driver.window_handles




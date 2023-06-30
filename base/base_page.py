from base.browser import Browser


class BasePage:
    def refresh_page(self):
        Browser().get_instance().refresh_page()

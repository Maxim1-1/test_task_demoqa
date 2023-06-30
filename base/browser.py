import logging
from base.Singleton import Singleton
from base.browser_factory import BrowserFactory


class Browser(metaclass=Singleton):
    logging.basicConfig(filename='logs.log', format='%(asctime)s %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)
    driver = None


    def get_driver(self, browser):
        self.driver = BrowserFactory(browser).factory_browser()
        return self.driver

    def get_instance(self):
        return self.driver

    def quit(self):
        self.driver.quit()

    def switch_to_window(self, number_window):
        self.logger.info(f'Switch to window')
        window = self.driver.window_handles[number_window]
        self.driver.switch_to.window(window)

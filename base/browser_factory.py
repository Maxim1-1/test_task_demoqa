import logging
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class BrowserFactory:
    logging.basicConfig(filename='logs.log', format='%(asctime)s %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)
    driver = None

    def __init__(self, browser):
        self.browser = browser

    def factory_browser(self):
        if self.browser == 'chrome':
            self.logger.info(f'Chrome driver create')
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif self.browser == 'firefox':
            self.logger.info(f'Firefox driver create')
            self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        else:
            self.logger.info(f'The browser was not created')
        return self.driver

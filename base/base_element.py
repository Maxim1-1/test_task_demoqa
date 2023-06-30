from logging import Logger
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

from base.browser import Browser
from project import config


class BaseElement:
    logging.basicConfig(filename='logs.log', format='%(asctime)s %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    timeout = config.timeout

    def __init__(self, method, locator):
        self.method = method
        self.locator = locator

    def find_element(self):
        try:
            element = WebDriverWait(Browser().get_instance(), self.timeout).until(
                EC.element_to_be_clickable((self.method, self.locator)))
            return element
        except TimeoutException:
            self.logger.warning("Элемент не найден")

    def wait_element(self):
        try:
            element = WebDriverWait(Browser().get_instance(), self.timeout).until(
                EC.presence_of_element_located((self.method, self.locator)))
        except TimeoutException:
            self.logger.warning("Элемент не найден")

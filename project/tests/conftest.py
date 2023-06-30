import time

import pytest

from base.browser import Browser
from project import config

browser = config.browser
URL = config.URL

@pytest.fixture
def set_up():
    driver = Browser().get_driver(browser)
    driver.maximize_window()
    driver.get(URL)
    yield
    driver.quit()

from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions

from base.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.url = url

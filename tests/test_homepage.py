import time

import pytest
from selenium.webdriver import ActionChains, Keys

from pom.home_page import HomePage
from pom.home_page_locators import HomePageLocators


@pytest.mark.usefixtures('driver')
class TestHomepage:

    @pytest.fixture(autouse=True)
    def open(self, driver):
        self.homepage = HomePage(driver, 'https://www.selenium.dev/')
        self.homepage.open()

    def test_get_links(self):
        links = ','.join([elem.text for elem in self.homepage.elements_are_present(HomePageLocators.NAV_LINKS)])
        assert links == HomePageLocators.NAV_LINKS_REF

    def test_search_button_correct(self):
        button = self.homepage.element_is_present(HomePageLocators.SEARCH_BUTTON)
        button.click()
        input_field = self.homepage.element_is_present(HomePageLocators.SEARCH_FIELD)
        input_field.send_keys(HomePageLocators.SEARCH_TEXT_GOOD)
        result = self.homepage.element_is_present(HomePageLocators.SEARCH_RESULTS_GOOD)
        assert result.text == HomePageLocators.SEARCH_RESULTS_GOOD_REF

    def test_search_button_incorrect(self):
        button = self.homepage.element_is_present(HomePageLocators.SEARCH_BUTTON)
        button.click()
        input_field = self.homepage.element_is_present(HomePageLocators.SEARCH_FIELD)
        input_field.send_keys(HomePageLocators.SEARCH_TEXT_BAD)
        result = self.homepage.element_is_present(HomePageLocators.SEARCH_RESULTS_FAIL)
        assert result.text == HomePageLocators.SEARCH_RESULTS_FAIL_REF + f'"{HomePageLocators.SEARCH_TEXT_BAD}"'

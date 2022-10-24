from selenium.webdriver.common.by import By


class HomePageLocators:

    NAV_LINKS = (By.XPATH, '//*[@id="main_navbar"]/ul/li/a')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="docsearch"]/button')
    SEARCH_FIELD = (By.XPATH, '//*[@id="docsearch-input"]')
    SEARCH_RESULTS_FAIL = (By.CSS_SELECTOR, '.DocSearch-Title')
    SEARCH_RESULTS_GOOD = (By.CSS_SELECTOR, '.DocSearch-Hit-title')

    NAV_LINKS_REF = 'About,Downloads,Documentation,Projects,Support,Blog,English'
    SEARCH_RESULTS_FAIL_REF = 'No results for '
    SEARCH_RESULTS_GOOD_REF = 'The Selenium Browser Automation Project'

    SEARCH_TEXT_GOOD = 'Selenium'
    SEARCH_TEXT_BAD = 'aslkfgjlsdgklsdj'

import requests
from bs4 import BeautifulSoup


def word_count(url):
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        return f'The word "Selenium" appears {soup.get_text().count("Selenium")} times'

    else:
        return 'Site selenium.dev is unavailable'


URL = 'https://www.selenium.dev/'
print(word_count(URL))

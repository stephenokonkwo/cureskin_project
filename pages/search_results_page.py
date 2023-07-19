from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class SearchResultsPage(Page):
    SEARCH_FEILD = (By.CSS_SELECTOR, "#Search-In-Modal.search__input")

    def search_for_product(self, search_query):
        self.input_text(search_query, *self.SEARCH_FEILD)
        # sleep(.5)

from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class SearchResultsPage(Page):
    SEARCH_FEILD = (By.CSS_SELECTOR, "#Search-In-Modal.search__input")
    SPF_RESULT = (By.CSS_SELECTOR, 'img[srcset*= "//cdn.shopify.com/s/files/1/0293/8775/1508/products/1_b"]')

    def search_for_product(self, search_query):
        self.input_text(search_query, *self.SEARCH_FEILD)

    def verify_search_result(self, expected_result):
        self.verify_element_text(expected_result, *self.SPF_RESULT)

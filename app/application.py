from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.header import Header
from pages.product_result_page import ProductResultsPage


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.product_result_page = ProductResultsPage(self.driver)

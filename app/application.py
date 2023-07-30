from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.header import Header
from pages.product_result_page import ProductResultsPage
from pages.sign_in_page import SignInPage
from pages.menu_page import MenuPage


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.product_result_page = ProductResultsPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.menu_page = MenuPage(self.driver)

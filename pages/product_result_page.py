from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class ProductResultsPage(Page):
    SPF_RESULT = (By.XPATH, '//a[@href= "/products/mineral-sunscreen?_pos=1&_psq=SPF&_ss=e&_v=1.0"]')
    SPF_VERIFICATION = (By.CSS_SELECTOR, 'div.product__title')

    def click_product(self):
        self.wait_for_element_click(*self.SPF_RESULT)
        # sleep(.5)

    def verify_product_result(self, expected_result):
        self.verify_partial_text(expected_result, *self.SPF_VERIFICATION)
        # sleep(.5)

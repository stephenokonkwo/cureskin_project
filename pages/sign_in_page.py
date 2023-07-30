from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    EMAIL_STRING = (By.CSS_SELECTOR, "input#CustomerEmail")

    def verify_user_sign_in(self,):
        self.find_element(*self.EMAIL_STRING)

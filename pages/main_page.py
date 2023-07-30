from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    POP_UP_BTN = (By.XPATH, "//button[@class='popup-close']")

    def open_main_page(self):
        self.open_url('https://shop.cureskin.com/')
        self.wait_for_element_click(*self.POP_UP_BTN)
        # sleep(.5)


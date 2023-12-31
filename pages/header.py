import time
from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Header(Page):
    SEARCH_BTN = (By.CSS_SELECTOR, "search-modal.header__search")
    HAMBURGER_BTN = (By.CSS_SELECTOR, 'details.menu-drawer-container')

    def click_search(self):
        self.wait_for_element_click(*self.SEARCH_BTN)



    def select_menu_btn(self):
        self.wait_for_element_click(*self.HAMBURGER_BTN)

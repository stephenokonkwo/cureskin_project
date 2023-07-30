import time
from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class MenuPage(Page):
    LOGIN_TAB = (By.CSS_SELECTOR, 'a.menu-drawer__account.link.link-with-icon.focus-inset')

    def click_login_tab(self):
        self.wait_for_element_click(*self.LOGIN_TAB)

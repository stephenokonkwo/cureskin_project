from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@when('Tap on user BTN')
def click_login_tab(context):
    context.app.menu_page.click_login_tab()

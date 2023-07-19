from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


# When Test cases
@when('From Header Page, click "Search"')
def click_search(context):
    context.app.header.click_search()



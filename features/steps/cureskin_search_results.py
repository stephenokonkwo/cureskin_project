from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


# When Test cases
@when('Search for {search_query}')
def search_for_product(context, search_query):
    context.app.search_results_page.search_for_product(search_query)

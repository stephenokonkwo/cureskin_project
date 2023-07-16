from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@when('Search for {search_query}')
def search_for_product(context, search_query):
    context.app.search_results_page.search_for_product(search_query)


@then('Verify the results have spf')
def verify_search_result(context):
    context.app.search_results_page.verify_search_result()

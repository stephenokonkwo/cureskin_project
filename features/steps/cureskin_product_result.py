from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@when('Click on product')
def click_product(context):
    context.app.product_result_page.click_product()


@then('Verify the results have {expected_result}')
def verify_product_result(context, expected_result):
    context.app.product_result_page.verify_product_result(expected_result)

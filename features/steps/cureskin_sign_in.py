from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


# Then steps
@then('Verify User sign in page appears')
def verify_user_sign_in(context):
    context.app.sign_in_page.verify_user_sign_in()

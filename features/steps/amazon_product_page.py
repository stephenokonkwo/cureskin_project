from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')
COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")
PRESENT_COLOR = (By.CSS_SELECTOR, 'span.selection')


# Given statements:
@given('Open Amazon product page B074TBCSC8')
def open_amazon_fashion_page(context):
    context.app.product_page.open_amazon_fashion_page()


@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


# When statements:
@when('Hover over New Arrivals tab')
def hover_new_arrival(context):
    context.app.product_page.hover_new_arrival()


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@when('Store product name')
def get_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')


# Then statements:
@then('Verify Men option is present')
def verify_men_option(context):
    context.app.product_page.verify_men_option()


@then('Verify user can click through colors')
def verify_user_can_click_colors(context):
    expected_colors = ['Army Green', 'Black', 'Blue', 'Brown']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # => [WebElement1, WebElement2, WebElement3]

    for color in colors[:4]:
        # WebElement2
        color.click()  # WebElement2.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors += [current_color]

    assert expected_colors == actual_colors, \
        f'Expected colors {expected_colors} did not match actual {actual_colors}'


@then('Verify user can click through Slim-Fit Stretch Jean colors')
def verify_user_can_click_slim_Fit_stretch_Jean_color(context):
    expected_colors = ['Black', 'Blue, Over Dye', 'Bright White', 'Dark Blue Vintage', 'Dark Indigo/Rinsed']
    actual_colors = []
    colors = context.driver.find_elements(
        *COLOR_OPTIONS)  # ==> [WebElement1, WebElement2, WebElement3, WebElement4, WebElement5]

    for color in colors[:5]:
        color.click()  # [WebElement1.click(), then WebElement2.click(), then WebElement3.click(), then WebElement4.click(),  then WebElement5.click()]
        present_color = context.driver.find_element(*PRESENT_COLOR).text
        # actual_colors += [present_color]
        assert present_color in expected_colors, f"Unexpected color {present_color} found"

    # assert expected_colors == actual_colors, \
    #     f'Expected colors {expected_colors} was not a match to actual colors {actual_colors}'

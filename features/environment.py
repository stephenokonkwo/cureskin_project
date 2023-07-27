import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


# Allure command:
# python3 -m behave -f allure_behave.formatter:AllureFormatter -o test_results/feature/test/cureskin_search_results.feature


def browser_init(context, scenario):
    # """
    # :param context: Behave context
    # """

    #### CHROME-CROSS BROWSER- DEFAULT BROWSER ####

    ## regular way
    # driver_path = ChromeDriverManager().install()
    # service = Service(executable_path=driver_path)

    # run on chrome for testing
    service = Service(executable_path='/Users/stephenokonkwo/Desktop/cureskin_project/chromedriver')


    context.driver = webdriver.Chrome(service=service)

    #### FIREFOX-CROSS BROWSER ####
    # context.driver = webdriver.Firefox(executable_path='/Users/stephenokonkwo/Desktop/cureskin_project/geckodriver')

    #### SAFARI-CROSS BROWSER ####
    # context.driver = webdriver.Safari()

    #### HEADLESS MODE ####
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument("--window-size=1920,1080")
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    #### BROWSERSTACK ####
    # LANA'S CODE EXAMPLE
    # desired_cap = {
    #     'browser': 'Chrome',
    #     'os': 'Windows',
    #     'os_version': '11',
    #     'name': scenario.name
    # }

    # DEFAULT: TESTS RUNNING: CHROME 115.0 VIA MAC(VENTURA)
    # desired_cap = {
    #     'bstack:options': {
    #         "os": "OS X",
    #         "osVersion": "Ventura",
    #         "browserVersion": "latest",
    #         "local": "false",
    #         "seleniumVersion": "3.14.0",
    #     },
    #     "browserName": "Chrome",
    # }

    # TESTS RUNNING: CHROME 115.0 VIA WINDOWS 11
    # desired_cap = {
    #     'bstack:options': {
    #         "os": "Windows",
    #         "osVersion": "11",
    #         "browserVersion": "latest-beta",
    #         "local": "false",
    #         "seleniumVersion": "3.14.0",
    #     },
    #     "browserName": "Chrome",
    # }

    # TESTS RUNNING: FIREFOX 115.0 VIA WINDOWS 11
    # desired_cap = {
    #     'bstack:options': {
    #         "os": "Windows",
    #         "osVersion": "11",
    #         "browserVersion": "latest",
    #         "local": "false",
    #         "seleniumVersion": "3.10.0",
    #     },
    #     "browserName": "Firefox",
    # }

    # bs_user = 'stephenokonkwo_Zihb2C'
    # bs_key = 'HEucNHsx1pT1wqHyfTU7'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)
    # context.driver.execute_script(
    #     'browserstack_executor:{"action":"setSessionName", "arguments":{"name": " ' + scenario.name + ' " }}')

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        context.driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Step '
            'failed"}}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()

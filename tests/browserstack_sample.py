import os

from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import have

from selene.support.shared import browser


# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720
# options = UiAutomator2Options().load_capabilities({
#     # Specify device and os_version for testing
#     "platformName": "android",
#     "platformVersion": "9.0",
#     "deviceName": "Google Pixel 3",
#
#     # Set URL of the application under test
#     # "app": "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",
#     "app": os.getenv('app'),
#
#     # Set other BrowserStack capabilities
#     'bstack:options': {
#         "projectName": os.getenv('project_name'),
#         "buildName": os.getenv('build_name'),
#         "sessionName": os.getenv('session_name'),
#
#         # Set your access credentials
#         "userName": os.getenv('user_name'),
#         "accessKey": os.getenv('access_key')
#     }
# })


def test_search():
    with step('Type search request'):
        # browser.open()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).send_keys("BrowserStack")

    with step('Verify content found'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))

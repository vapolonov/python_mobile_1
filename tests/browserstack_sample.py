
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser


# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720
options = UiAutomator2Options().load_capabilities({
    # Specify device and os_version for testing
    "platformName": "android",
    "platformVersion": "9.0",
    "deviceName": "Google Pixel 3",

    # Set URL of the application under test
    "app": "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",

    # Set other BrowserStack capabilities
    'bstack:options': {
        "projectName": "First Python project",
        "buildName": "browserstack-build-VASVAP",
        "sessionName": "BStack first_test",

        # Set your access credentials
        "userName": "vasvap_AXK9zO",
        "accessKey": "HGn98M62SvWqh1AKGwFo"
    }
})

# Test case for the BrowserStack sample Android app.
# If you have uploaded your app, update the test case here.
browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).send_keys("BrowserStack")

browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))


# Invoke driver.quit() after the test is done to indicate that the test is completed.
browser.quit()

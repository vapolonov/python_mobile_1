
from selene.support.shared import browser
from appium import webdriver


def driver_management():
    # Initialize the remote Webdriver using BrowserStack remote URL
    # and options defined above
    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
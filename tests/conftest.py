import pytest
from selene.support.shared import browser
from appium import webdriver

import config
from utils import attach


@pytest.fixture(scope='function', autouse=True)
def driver_management():
    browser.config.driver = webdriver.Remote(
        config.settings.remote_url, options=config.settings.driver_options
    )
    browser.config.timeout = 4
    yield
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_xml(browser)
    attach.add_video(browser.driver.session_id)
    browser.quit()





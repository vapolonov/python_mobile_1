import pytest
from selene.support.shared import browser
from appium import webdriver

import config


@pytest.fixture(scope='function', autouse=True)
def driver_management():
    browser.config.driver = webdriver.Remote(
        config.settings.remote_url, options=config.settings.driver_options
    )
    browser.config.timeout = 4
    yield
    browser.quit()

#
# @pytest.fixture(scope='session', autouse=True)
# def load_env():
#     load_dotenv()




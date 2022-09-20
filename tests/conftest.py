import os

import pytest
from dotenv import load_dotenv
from selene.support.shared import browser
from appium import webdriver

from utils import attach


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def driver_management():
    user = os.getenv('user_name')
    key = os.getenv('access_key')
    url = os.getenv('remote_url')

    desired_capabilities = {
        "app": "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",
        "deviceName": "Google Pixel 3",
        "platformVersion": "9.0",
        "platformName": "android",
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-VASVAP",
            "sessionName": "BStack first_test vasvap"
        }
    }
    browser.config.driver = webdriver.Remote(
        command_executor=f"https://{user}:{key}@{url}/wd/hub",
        desired_capabilities=desired_capabilities
    )
    browser.config.timeout = 4
    yield driver_management
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_xml(browser)
    attach.add_video(browser.driver.session_id)
    browser.quit()


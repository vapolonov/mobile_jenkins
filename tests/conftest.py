import os
from datetime import date
from appium import webdriver
import pytest
from dotenv import load_dotenv
from selene.support.shared import browser
from utils import attach


@pytest.fixture(scope='session', autouse=True)
def auto_env():
    load_dotenv()


# @pytest.fixture(scope='function', autouse=True)
# def attach_video():
#     yield


@pytest.fixture(scope='function', autouse=True)
def setup():
    desired_capabilities = ({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Samsung Galaxy S20",
        "os_version": "10.0",
        "app": "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",
        "build": "browserstack-build-" + str(date.today()),
        'bstack:options': {
            "sessionName": "QA.GURU Python project test",
            "projectName": "QA.GURU Python project",
        }
    })

    user_name = os.getenv('user_name')
    access_key = os.getenv('access_key')
    browser.config.driver = webdriver.Remote("http://" + str(user_name) + ":" + str(access_key) +
                                             "@hub-cloud.browserstack.com/wd/hub", desired_capabilities)
    browser.config.timeout = 4
    session_id = browser.config.driver.session_id

    yield

    attach.add_screenshot(browser)
    attach.add_xml(browser)
    attach.add_video(session_id, 'Test video')
    browser.quit()

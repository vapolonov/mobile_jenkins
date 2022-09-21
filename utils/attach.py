import allure
import requests
import os
from allure_commons.types import AttachmentType


def get_video_url(session_id: str):
    session = requests.Session()
    session.auth = (os.getenv('user_name'), os.getenv('access_key'))
    response = session.get(f'https://api.browserstack.com/app-automate/sessions/{session_id}.json')
    return response.json().get('automation_session').get('video_url')


def add_video(session_id: str, name: str):
    html = ("<html><body><video width='100%' height='100%' controls autoplay><source src='"
            + get_video_url(session_id)
            + "' type='video/mp4'></video></body></html>")
    allure.attach(html, name, AttachmentType.HTML, '.html')


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_xml(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source_xml', AttachmentType.XML)
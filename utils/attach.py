
import allure
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source_html', AttachmentType.HTML)


def add_xml(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source_xml', AttachmentType.XML)


def add_video(browser):
    video_url = (f'https://app-automate.browserstack.com/s3-upload/bs-video-logs-euw/s3.eu-west-1/{browser.driver.session_id}/video-' + browser.driver.session_id + '.mp4')
    html = (f'<html><body>'
            f'<video width="100%" height="100%" controls autoplay><source src="{video_url}" type="video/mp4">'
            f'</video></body></html>')
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')

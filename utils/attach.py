
import allure
from allure_commons.types import AttachmentType

from utils import browserstack


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source_html', AttachmentType.HTML)


def add_xml(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source_xml', AttachmentType.XML)


def add_video(session_id, *, name='video recording'):
    video_url = browserstack.video_url(session_id=session_id)
    html = ('<html><body>'
            '<video width="100%" height="100%" controls autoplay>'
            f'<source src="{video_url}" type="video/mp4">'
            '</video></body></html>')
    allure.attach(html, name=name, attachment_type=allure.attachment_type.HTML, extension='.html')

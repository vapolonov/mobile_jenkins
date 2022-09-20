import requests

import config


def video_url(*, session_id):
    session_details = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(config.settings.user_name, config.settings.access_key),
    ).json()

    return session_details['automation_session']['video_url']
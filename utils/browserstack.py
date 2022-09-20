import os

import requests
from dotenv import load_dotenv


def video_url(*, session_id):
    load_dotenv()
    session_details = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(os.getenv('user_name'), os.getenv('access_key')),
    ).json()

    return session_details['automation_session']['video_url']
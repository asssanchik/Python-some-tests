import pytest
import requests
from configuration import CHANNELS_URL

@pytest.fixture
def get_api_v1_channels():
    response = requests.get(CHANNELS_URL + '/api/v1/channels?platform=Unico&prev_program=false&device_type=web')
    return response

import pytest
import requests
from random import randrange
from configuration import CHANNELS_URL

@pytest.fixture
def get_api_v1_channels():
    response = requests.get(CHANNELS_URL + '/api/v1/channels?platform=Unico&prev_program=false&device_type=web')
    return response

@pytest.fixture
def make_number():
    number = randrange(1, 100, 5)
    yield 
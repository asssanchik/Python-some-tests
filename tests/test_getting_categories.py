import requests
from configuration import SERVICE_URL

def test_getting_categories():
    response = requests.get(url = SERVICE_URL)
    print(response.json())


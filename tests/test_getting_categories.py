import requests

from jsonschema import validate

from configuration import SERVICE_URL

from src.enums.global_enums import GlobalErrorMessages, GlobalCorrectMessages
from src.schemas.get_v2_categories import GET_V2_CATEGORIES

def test_getting_categories():
    response = requests.get(url = SERVICE_URL + '/web/main?apikey=KNnpXL0TCyMm9F0qFqF5vsBzj3O4NGBs&for_kids=false&locale=ru&content_lang=ru&limit=4')
    reseived_banners = response.json()
 #   print(reseived_banners)
    assert response.status_code == 200, GlobalCorrectMessages.CORRECT_STATUS_CODE.value
    assert len(reseived_banners) == 4, GlobalCorrectMessages.CORRECT_ELEMENT_COUNT.value
    for banner in reseived_banners:
        validate(banner, GET_V2_CATEGORIES)



## [{'alias': 'originals-ma', 'banner_size': None}]
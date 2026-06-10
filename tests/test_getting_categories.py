import requests

from configuration import SERVICE_URL


from src.baseclasses.response import Response
from src.schemas.get_v2_categories import GET_V2_CATEGORIES

def test_getting_categories():
    r = requests.get(url = SERVICE_URL + '/web/main?apikey=KNnpXL0TCyMm9F0qFqF5vsBzj3O4NGBs&for_kids=false&locale=ru&content_lang=ru&limit=4')
    response = Response(r)
    response.assert_status_code(200).validate(GET_V2_CATEGORIES)




## [{'alias': 'originals-ma', 'banner_size': None}]
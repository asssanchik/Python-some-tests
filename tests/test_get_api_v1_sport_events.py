import requests

from configuration import SERVICE_URL
from src.baseclasses.response import Response
from src.pydantic_schemas.pydantic_api_v1_sport_events import PydanticAPIV1SportEvents

 #resp = requests.get(SERVICE_URL + '/api/v1/sport/events?apikey=KNnpXL0TCyMm9F0qFqF5vsBzj3O4NGBs')
# print(resp.json())

def test_getting_sport_events():
    response = requests.get(SERVICE_URL + '/api/v1/sport/events?apikey=KNnpXL0TCyMm9F0qFqF5vsBzj3O4NGBs')
    test_object = Response(response)
    test_object.assert_status_code(300).validate(PydanticAPIV1SportEvents)



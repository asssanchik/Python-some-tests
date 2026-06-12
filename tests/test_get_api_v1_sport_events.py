import requests

from configuration import SERVICE_URL
from src.baseclasses.response import Response


 #resp = requests.get(SERVICE_URL + '/api/v1/sport/events?apikey=KNnpXL0TCyMm9F0qFqF5vsBzj3O4NGBs')
# print(resp.json())

def test_getting_sport_events():
    response = requests.get(SERVICE_URL + '/api/v1/sport/events?apikey=KNnpXL0TCyMm9F0qFqF5vsBzj3O4NGBs')
    test_object = Response(response)
    test_object.assert_status_code(200)


{
  "data": [
    {
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "alias": "string",
      "title_1": "string",
      "title_2": "string",
      "description": "string",
      "event_start_time": "2026-06-12T12:31:22.534Z",
      "event_end_time": "2026-06-12T12:31:22.534Z",
      "weight": 0,
      "button_text": "string",
      "is_published": true,
      "tournament": {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "title": "string",
        "alias": "string",
        "categories": [
          {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "title": "string",
            "alias": "string"
          }
        ]
      },
      "channel": {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "title": "string",
        "alias": "string",
        "stream_url": "string",
        "number": 0,
        "is_free": true
      },
      "title_1_posters": {
        "logotype": "string",
        "horizontal": "string",
        "vertical": "string",
        "background": "string"
      },
      "title_2_posters": {
        "logotype": "string"
      }
    }
  ],
  "pagination": {
    "offset": 0,
    "limit": 0,
    "total": 0,
    "has_more": false
  }
}
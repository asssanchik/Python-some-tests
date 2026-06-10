from jsonschema import validate


class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response.json, list):
            for item in self.response.json:
                validate(item, schema)
        else:
            validate(self.response.json, schema)


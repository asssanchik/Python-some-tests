#from jsonschema import validate

from src.enums.global_enums import GlobalErrorMessages, GlobalCorrectMessages

class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):

        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.model_validate(item)
        else:
            schema.model_validate(self.response_json)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response.status_code in status_code, GlobalCorrectMessages.CORRECT_STATUS_CODE.value
        else:
            assert self.response.status_code == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self
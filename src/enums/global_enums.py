from enum import Enum


class GlobalCorrectMessages(Enum):
     CORRECT_STATUS_CODE = "Received status code is equal to expected"
     CORRECT_ELEMENT_COUNT = "Number of items is equal to expected."

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code is not equal to expected."
    WRONG_ELEMENT_COUNT = "Number of items is not equal to expected."
    ID_MUST_BE_UUID = "Id must be a valid UUID."

from enum import Enum


class GlobalCorrectMessages(Enum):
     CORRECT_STATUS_CODE = "Received status code is equal to expected"

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code is not equal to expected."


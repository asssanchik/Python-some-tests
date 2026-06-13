from src.enums.global_enums import GlobalErrorMessages

class Events:
    def __init__(self):
        self.result = {}

    def set_status(self, status = GlobalErrorMessages.WRONG_STATUS_CODE.value):
        self.result["status"] = status
        return self

    

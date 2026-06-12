from pydantic import BaseModel, validator
from uuid import UUID
from src.enums.global_enums import GlobalErrorMessages

class PydanticAPIV1SportEvents(BaseModel):
    id: str
    alias: str
    title_1: str
    description: str
    event_start_time: str
    event_end_time: str
    weight: int
    button_text: str
    is_published: bool

@validator('id')
def check_id_is_uuid(cls, id):
        try:
            UUID(id)
        except ValueError:
            raise ValueError(GlobalErrorMessages.ID_MUST_BE_UUID.value)
        return id
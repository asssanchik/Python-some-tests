from pydantic import BaseModel, validator
from uuid import UUID
from src.enums.global_enums import GlobalErrorMessages

from typing import List

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

class PydanticAPIV1SportEventsResponse(BaseModel):
    data: List[PydanticAPIV1SportEvents]
    has_more: bool
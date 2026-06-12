from pydantic import BaseModel

class PydanticAPIV1SportEvents(BaseModel):
    id: str
    alias: str
    title_1: str
    title_2: str
    description: str
    event_start_time: str
    event_end_time: str
    weight: int
    button_text: str
    is_published: bool


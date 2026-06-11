from pydantic import BaseModel, validator, Field

class PydanticGetV2Categories(BaseModel):
    alias: str
    items_total: int
    long_description: str
    short_description: str
    title: str


    @validator('items_total')
    def items_total_validator(cls, v):
        if v > 2:
            raise ValueError("Items more than 2")
        else:
            return v




#"alias": {"type": "string"},
     #       "items_total": {"type": "number"},
      #      "long_description": {"type": "string"},
       #     "short_description": {"type": "string"},
        #    "title": {"type": "string"}
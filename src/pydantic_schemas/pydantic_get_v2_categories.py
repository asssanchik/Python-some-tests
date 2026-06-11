from pydantic import BaseModel

class PydanticGetV2Categories(BaseModel):
    alias: str
    items_total: int
    title: str


  #  @validator('items_total')
  #  def items_total_validator(cls, v):
    #    if v > 2:
    #    raise ValueError("Items more than 2")
    #    else:
#       return v





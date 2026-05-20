from pydantic import BaseModel
from typing import Literal, Optional

class ConversionRequest(BaseModel):
    category: str
    from_unit: str
    to_unit: str
    value: float

class ConversionResponse(BaseModel):
    value: float
    from_unit: str
    to_unit: str
    result: float
    category: str
    formatted_result: Optional[str] = None
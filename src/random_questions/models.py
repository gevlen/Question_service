from pydantic import BaseModel, Field


class CountAddResponseV2(BaseModel):
    questions_num: int = Field(..., ge=1, le=100)

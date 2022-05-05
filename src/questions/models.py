from pydantic import BaseModel, Field

from datetime import datetime
from typing import Optional


class QuestionResponseV1(BaseModel):
    id: int = Field(..., ge=1)
    external_id: Optional[int] = None
    question: str
    answer: str
    created_at_jservice: Optional[datetime] = None
    created_at_db: datetime
    category_id: Optional[int] = Field(..., ge=1)


class QuestionAddResponseV1(BaseModel):
    question: str
    answer: str
    category_id: Optional[int] = Field(..., ge=1)

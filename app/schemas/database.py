from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from . import MoneyComeType


class PaymentForm(BaseModel):
    amount: int
    category_id: int
    comment: Optional[str]
    created_at: Optional[datetime] = None


class PaymentJSON(BaseModel):
    id: int
    created_at: datetime
    category_id: int
    amount: int
    comment: Optional[str]


class CategoryForm(BaseModel):
    name: str
    color: str
    money_come_type: MoneyComeType


class CategoryJSON(BaseModel):
    id: int
    name: str
    color: str
    money_come_type: MoneyComeType


class LimitForm(BaseModel):
    category_id: int
    amount: int


class LimitJSON(BaseModel):
    id: int
    category_id: int
    amount: int

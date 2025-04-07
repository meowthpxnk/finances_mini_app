from datetime import datetime, timezone
from typing import TYPE_CHECKING, Optional

from pydantic import BaseModel
from sqlalchemy import DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.schemas import MoneyComeType, PaymentForm, PaymentJSON

from .__Base import Base


if TYPE_CHECKING:
    from .Category import Category


class Payment(Base):
    id: Mapped[int] = mapped_column(primary_key=True)

    amount: Mapped[int] = mapped_column(Integer, nullable=False)
    comment: Mapped[str] = mapped_column(String, nullable=True)

    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    category: Mapped["Category"] = relationship(back_populates="payments")

    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )

    def __init__(self, form: PaymentForm) -> None:
        super().__init__(form)

    def jsonify(self) -> PaymentJSON:
        return PaymentJSON(
            id=self.id,
            amount=self.amount,
            created_at=self.created_at,
            comment=self.comment,
            category_id=self.category.id if self.category else None,
        )

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.schemas import LimitForm, LimitJSON

from .__Base import Base


if TYPE_CHECKING:
    from .Category import Category


class Limit(Base):
    id: Mapped[int] = mapped_column(primary_key=True)

    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    category: Mapped["Category"] = relationship(back_populates="payments")

    amount: Mapped[int] = mapped_column(Integer, nullable=False)

    def __init__(self, form: LimitForm) -> None:
        super().__init__(form)

    def jsonify(self) -> LimitJSON:
        return LimitJSON(
            id=self.id,
            amount=self.amount,
            category_id=self.category_id,
        )

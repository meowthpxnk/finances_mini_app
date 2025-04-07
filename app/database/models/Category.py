from typing import TYPE_CHECKING

from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.schemas import CategoryForm, CategoryJSON, MoneyComeType

from .__Base import Base


if TYPE_CHECKING:
    from .Limit import Limit
    from .Payment import Payment


class Category(Base):
    id: Mapped[int] = mapped_column(primary_key=True)

    color: Mapped[str] = mapped_column(String, nullable=True)
    name: Mapped[str] = mapped_column(String, nullable=True)

    payments: Mapped[list["Payment"]] = relationship(back_populates="category")
    limit: Mapped["Limit"] = relationship(back_populates="category")

    money_come_type: Mapped[MoneyComeType] = mapped_column(Enum(MoneyComeType))

    def __init__(self, form: CategoryForm) -> None:
        super().__init__(form)

    def jsonify(self) -> CategoryJSON:
        return CategoryJSON(
            id=self.id,
            name=self.name,
            color=self.color,
            money_come_type=self.money_come_type,
        )

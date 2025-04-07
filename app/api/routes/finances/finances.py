from app import bot, db
from app.api.routes._base_router import APIRouter
from app.database.models import Category, Limit, Payment
from app.schemas import CategoryForm, LimitForm, MoneyComeType, PaymentForm


router = APIRouter(
    tags=["Finances"],
)


@router.get("/category")
async def get_categories():
    categories = Category.select_where()
    return [item.jsonify() for item in categories]


@router.post("/category")
async def create_category(form: CategoryForm):
    item = Category(form)
    db.session.add(item)
    db.session.commit()


@router.get("/payment")
async def get_payments():
    payments = Payment.select_where()
    return [item.jsonify() for item in payments]


@router.post("/payment")
async def create_payment(form: PaymentForm):
    Category.exists(Category.id == form.category_id, arg=True)

    item = Payment(form)

    db.session.add(item)
    db.session.commit()


@router.post("/payment/{id}")
async def delete_payment(id: int):
    item = Payment.select_where(Payment.id == id, first=True)

    db.session.delete(item)
    db.session.commit()


@router.get("/limit")
async def get_limits():
    limits = Limit.select_where()
    return [item.jsonify() for item in limits]


@router.post("/limit")
async def create_limit(form: LimitForm):
    category = Category.exists(Category.id == form.category_id, arg=True)

    if not category.money_come_type == MoneyComeType.INCOME:
        raise Exception("Limit can be created only for outcome type category.")

    if category.limit:
        raise Exception("Limit already exist for this cateogry.")

    item = Limit(form)
    db.session.add(item)
    db.session.commit()

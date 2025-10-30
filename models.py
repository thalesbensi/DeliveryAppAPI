from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, DECIMAL
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import ChoiceType

db = create_engine("sqlite:///database.db")

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    email = Column("email", String, nullable=False, unique=True)
    password = Column("password", String, nullable=False)
    active = Column("active",Boolean, nullable=False, default=True)
    admin = Column("admin", Boolean, nullable=False, default=False)

    def __init__(self, name, email, password, active=True, admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.admin = admin


class Order(Base):
    __tablename__ = "orders"

    ORDER_STATUS = (
        ("PENDING", "PENDING"),
        ("CANCELED", "CANCELED"),
        ("COMPLETED", "COMPLETED"),
    )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", ChoiceType(choices=ORDER_STATUS), nullable=False, default="PENDING")
    user_id = Column("user_id", Integer, ForeignKey("users.id"), nullable=False)
    price = Column("price", DECIMAL , nullable=False)

    def __init__(self, user_id, status="PENDING", price=0):
        self.user_id = user_id
        self.status = status
        self.price = price


class Items(Base):
    __tablename__ = "items"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    flavor = Column("flavor", String, nullable=False)
    size = Column("size", nullable=False)
    quantity = Column("quantity", Integer, nullable=False)
    unit_price = Column("price", DECIMAL , nullable=False)
    order_id = Column("order_id", Integer, ForeignKey("orders.id"), nullable=False)

    def __init__(self, flavor, size, quantity, order_id):
        self.flavor = flavor
        self.size = size
        self.quantity = quantity
        self.order_id = order_id
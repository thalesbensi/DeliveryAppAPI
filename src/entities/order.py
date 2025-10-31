from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey

from src.database.core import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String, nullable=False, default="PENDING")
    user_id = Column("user_id", Integer, ForeignKey("users.id"), nullable=False)
    price = Column("price", DECIMAL , nullable=False)

    def __init__(self, user_id, status="PENDING", price=0):
        self.user_id = user_id
        self.status = status
        self.price = price
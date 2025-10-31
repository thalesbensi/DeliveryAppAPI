from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL

from src.database.core import Base


class Item(Base):
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
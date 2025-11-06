from sqlalchemy import Column, Integer, String, Boolean

from src.api.core.database.core import Base


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
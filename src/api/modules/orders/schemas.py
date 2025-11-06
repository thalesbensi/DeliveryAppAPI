from pydantic import BaseModel


class OrderSchema(BaseModel):
    user_id : int

    class Config:
        from_attributes = True
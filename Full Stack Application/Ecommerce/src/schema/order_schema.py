from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

from src.schema.order_item_schema import OrderItemSchema


class OrderRequest(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    address: str
    contact: str
    totalBillAmount: float
    order_items: list[OrderItemSchema]


class OrderItemResponse(BaseModel):
    id: int
    order_id: int
    title: str
    price: float
    description: str
    qty: int
    totalPrice: float
    product_image: str
    warranty_information: Optional[str] = None
    product_id: int

    class Config:
        from_attributes = True


class OrderResponse(BaseModel):
    id: int
    user_id: int
    totalBillAmount: float
    name: str
    email: str
    contact: str
    address: str
    date: datetime
    payment_mode: str
    order_items: list[OrderItemResponse]

    class Config:
        from_attributes = True
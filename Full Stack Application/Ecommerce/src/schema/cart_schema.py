from typing import Optional
from pydantic import BaseModel


class CartRequest(BaseModel):
    user_id: int
    product_id: int


class ProductResponse(BaseModel):
    id: int
    title: str
    price: float
    description: Optional[str] = None
    warranty_information: Optional[str] = None
    rating: Optional[str] = None
    product_image: str
    category_id: int

    class Config:
        from_attributes = True


class CartItemResponse(BaseModel):
    cart_id: int
    product_id: int
    product: ProductResponse

    class Config:
        from_attributes = True


class CartResponse(BaseModel):
    cart_items: list[CartItemResponse]


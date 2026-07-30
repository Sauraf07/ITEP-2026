from pydantic import BaseModel


class CartRequest(BaseModel):
    product_id:int

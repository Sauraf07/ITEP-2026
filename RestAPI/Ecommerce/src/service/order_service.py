from src.repository.order_repository import OrderRepository


class OrderService:
    def __init__(self,order_repo:OrderRepository):
        self.order_repo = order_repo



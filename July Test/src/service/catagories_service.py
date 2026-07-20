from src.repository.catagories_repo import CategoriesRepository
from src.models.categories import Categories


class CategoriesService:
    def __init__(self, cata_repo: CategoriesRepository):
        self.cata_repo = cata_repo

    async def create_category(self, category: Categories):
        return await self.cata_repo.create(category)

    async def get_all_categories(self):
        return await self.cata_repo.get_all_categories()
    
    async def delete_category(self, category_id: int):
        return await self.cata_repo.delete_category(category_id)
    
    async def update_category(self, category_id: int, updated_category: Categories):
        return await self.cata_repo.update_category(category_id, updated_category)
    
import shutil

from fastapi import UploadFile, Path
from src.models.category import Category

from src.repository.category_repository import CategoryRepository

BASE_DIR = Path(__file__).resolve().parent.parent
class CategoryService():
    def __init__(self,category_repo:CategoryRepository):
        self.category_repo = category_repo

    async def create(self,category_name:str,category_image:UploadFile):
        file_path = BASE_DIR.joinpath("public","images",category_name.filename)
        with open(file_path,"wb") as buffer:
            shutil.copyfileobj(category_image.file,buffer)
        await category_image.close()

        category = Category(category_name=category_name,category_image="/public/images/"+category_image.filename)
        return await self.category_repo.create(category)
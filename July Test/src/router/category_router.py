from fastapi import APIRouter, Depends
from starlette import status
from fastapi.params import Form

from src.dependency.repository_dependency import authenticate
from src.models import Categories
from src.dependency.service_dependency import get_catagories_service

router = APIRouter(prefix="/category", tags=["Category"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_category(category=Depends(authenticate),category_name: str = Form(...), cate_service=Depends(get_catagories_service)):
    return await cate_service.create_category(Categories(name=category_name))

@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_categories(category=Depends(authenticate),cate_service=Depends(get_catagories_service)):
      return await cate_service.get_all_categories()


@router.get("/{category_id}", status_code=status.HTTP_200_OK)
async def get_category_by_id(category_id: int, cate_service=Depends(get_catagories_service),category=Depends(authenticate)):
    return await cate_service.get_category_by_id(category_id)

@router.delete("/{category_id}", status_code=status.HTTP_200_OK)
async def delete_category(category_id: int, cate_service=Depends(get_catagories_service),category=Depends(authenticate)):
      return await cate_service.delete_category(category_id)

@router.put("/{category_id}", status_code=status.HTTP_200_OK)
async def update_category(category_id: int, category_name: str = Form(...), cate_service=Depends(get_catagories_service),category=Depends(authenticate)):
    updated_category = Categories(name=category_name)
    return await cate_service.update_category(category_id, updated_category)
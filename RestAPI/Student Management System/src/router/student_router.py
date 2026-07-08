from fastapi import APIRouter, Depends
from starlette import status

from src.dependency.student_dependency import get_student_service
from src.schema.student_schema import StudentResponse,StudentReq
from src.services.student_service import StudentService

router = APIRouter(prefix="/student",tags=["Student"])

@router.post("/create",response_model=StudentResponse,status_code=status.HTTP_201_CREATED)
async def create_student(request:StudentReq,student_service:StudentService=Depends(get_student_service)):
    return await student_service.create(request)

@router.get("/",response_model=list[StudentResponse],status_code=status.HTTP_200_OK)
async def get_students(student_service:StudentService=Depends(get_student_service)):
    students = await student_service.get_all()
    return students

@router.get("/{student_id}",response_model=StudentResponse,status_code=status.HTTP_200_OK)
async def get_student(student_id:int,student_service:StudentService=Depends(get_student_service)):
    student = await student_service.get_by_id(student_id)
    return student

@router.put("/update/{student_id}",response_model=StudentResponse,status_code=status.HTTP_200_OK)
async def update_student(student_id:int,request:StudentReq,student_service:StudentService=Depends(get_student_service)):
    # Implementation for updating a student
    return await student_service.update(student_id, request)

@router.delete("/delete/{student_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_student(student_id:int,student_service:StudentService=Depends(get_student_service)):
    # Implementation for deleting a student
    await student_service.delete(student_id)
    return {"message": "Student deleted successfully"}
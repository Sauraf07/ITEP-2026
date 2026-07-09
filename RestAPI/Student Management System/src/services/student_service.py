from src.exception.resource_not_found import ResourceNotFound
from src.models.student import Student
from src.repository.student_repository import StudentRepository
from src.schema.student_schema import StudentReq


class StudentService:
    def __init__(self,session,student_repo:StudentRepository):
        self.session = session
        self.student_repo = student_repo


    async def create(self,request:StudentReq):
        student = Student(name = request.name,email=request.email,course=request.course,age=request.age)
        return await self.student_repo.create(student)
    
    async def get_all(self):
        return await self.student_repo.get_all()
    
    async def get_by_id(self,student_id:int):
        db_student = await self.student_repo.get_by_id(student_id)
        if not db_student:
            raise ResourceNotFound(f"Student with id {student_id} not found")
        return db_student

    async def update(self,student_id:int,request:StudentReq):
        updated_student = Student(name=request.name,email=request.email,course=request.course,age=request.age)
        db_student = await self.student_repo.update(student_id,updated_student)
        if not db_student:
            raise ResourceNotFound(f"Student with id {student_id} not found")
        return db_student
    
    async def delete(self,student_id:int):
        db_student = await self.student_repo.delete(student_id)
        if not db_student:
            raise ResourceNotFound(f"Student with id {student_id} not found")
        return db_student
    
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.student import Student


class StudentRepository:
    def __init__(self,session:AsyncSession):
        self.session = session

    async def create(self,student:Student):
        self.session.add(student)
        await self.session.commit()
        await self.session.refresh(student)
        return student
    
    async def get_all(self):
        statements = select(Student)
        result = await self.session.execute(statements)
        return result.scalars().all()

    async def get_by_id(self,student_id:int):
        return await self.session.get(Student,student_id)
    
    async def update(self,student_id:int,updated_student:Student):
        db_student = await self.get_by_id(student_id)
        if not db_student:
            return None
        db_student.name = updated_student.name
        db_student.email = updated_student.email
        db_student.course = updated_student.course
        db_student.age = updated_student.age
        await self.session.commit()
        await self.session.refresh(db_student)
        return db_student
    
    async def delete(self,student_id:int):
        db_student = await self.get_by_id(student_id)
        if not db_student:
            return None
        await self.session.delete(db_student)
        await self.session.commit()
        return db_student
    
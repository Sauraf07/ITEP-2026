from src.model.student import Student
from src.repo.student_repo import StudentRepo


class Student_Service:
    def __init__(self, session):
        self.student_repo = StudentRepo(session)

    async def create_student(self, student: Student):
        return await self.student_repo.create_student(student)

    async def get_all_students(self):
        return await self.student_repo.get_all_students()

    async def get_student_by_id(self, student_id: int):
        return await self.student_repo.get_student_by_id(student_id)

    async def update_student(self, student_id: int, **fields):
        return await self.student_repo.update_student(student_id, **fields)

    async def delete_student(self, student_id: int):
        return await self.student_repo.delete_student(student_id)

from src.model.student import Student
from src.repo.student_repo import StudentRepo


class Student_Service:
    def __init__(self,session):
        self.student_repo = StudentRepo(session)

    async def create_student(self,student:Student):
        return await self.student_repo.create_student(student)

from sqlalchemy import select

from src.model.student import Student


class StudentRepo:
    def __init__(self, session):
        self.session = session

    async def create_student(self, student: Student):
        self.session.add(student)
        await self.session.flush()
        return student

    async def get_all_students(self):
        result = await self.session.execute(select(Student).order_by(Student.id))
        return result.scalars().all()

    async def get_student_by_id(self, student_id: int):
        return await self.session.get(Student, student_id)

    async def update_student(self, student_id: int, **fields):
        student = await self.get_student_by_id(student_id)
        if student is None:
            return None

        for field, value in fields.items():
            if value is not None:
                setattr(student, field, value)

        await self.session.flush()
        return student

    async def delete_student(self, student_id: int):
        student = await self.get_student_by_id(student_id)
        if student is None:
            return False

        await self.session.delete(student)
        await self.session.flush()
        return True

from src.model.student import Student


class StudentRepo:
    def __init__(self,session):
        self.session = session

    async def create_student(self,student:Student):
        self.session.add(student)
        await self.session.flush()
        return student
from sqlalchemy.exc import SQLAlchemyError
import asyncio
from src.db.db_config import SessionLocal
from src.model.student import Student
from src.service import student_services
from src.service.student_services import Student_Service


async def create_student():
    try:
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        gender = input("Enter your gender: ")
        email = input("Enter your email: ")
        phone = input("Enter your phone number: ")
        class_room = input("Enter your class room number: ")
        async with SessionLocal.begin() as session:
            student =  Student(name=name, age=age, gender=gender, email=email, phone=phone,classroom_id=class_room)
            student_service = Student_Service(session)
            student = await student_service.create_student(student)
            await session.refresh(student)
            print(f"Student {student.id} : {student.name}:")
    except SQLAlchemyError as e:
        print(e)

async def main():
    while True:
        print("Press 1 for Student Operation")
        print("Press 2 for Teacher Operation")
        print("Press 3 for Subject Operation")
        print("Press 4 for Classroom Operation")
        print("Press 0 for exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            await create_student()

        elif choice == "0":
            break
asyncio.run(main())
import asyncio
from sqlalchemy.exc import SQLAlchemyError

from src.db.db_config import SessionLocal, init_db
from src.menu.student_menu import student_menu
from src.model.student import Student
from src.service.student_services import Student_Service


async def create_student():
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        gender = int(input("Enter your gender code: "))
        email = input("Enter your email: ")
        phone = int(input("Enter your phone number: "))
        class_room = int(input("Enter your class room number: "))
        async with SessionLocal.begin() as session:
            student = Student(
                name=name,
                age=age,
                gender=gender,
                email=email,
                phone=phone,
                classroom_id=class_room,
            )
            student_service = Student_Service(session)
            student = await student_service.create_student(student)
            await session.refresh(student)
            print(f"Student {student.id} : {student.name}:")
    except (SQLAlchemyError, ValueError) as e:
        print(e)


async def main():
    await init_db()
    while True:
        print("Press 1 for Student Operation")
        print("Press 2 for Teacher Operation")
        print("Press 3 for Subject Operation")
        print("Press 4 for Classroom Operation")
        print("Press 0 for exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            async with SessionLocal() as session:
                await student_menu(session)

        elif choice == "2":
            print("Teacher operations are not implemented yet.")

        elif choice == "3":
            print("Subject operations are not implemented yet.")

        elif choice == "4":
            print("Classroom operations are not implemented yet.")

        elif choice == "0":
            break


asyncio.run(main())

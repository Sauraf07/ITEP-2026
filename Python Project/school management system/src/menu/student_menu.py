from sqlalchemy.exc import SQLAlchemyError

from src.model.student import Student
from src.service.student_services import Student_Service


def _read_int(prompt: str) -> int:
    while True:
        value = input(prompt).strip()
        try:
            return int(value)
        except ValueError:
            print("Enter a valid number.")


def _read_optional_int(prompt: str):
    value = input(prompt).strip()
    if value == "":
        return None

    try:
        return int(value)
    except ValueError:
        print("Enter a valid number.")
        return _read_optional_int(prompt)


async def student_menu(session) -> None:
    student_service = Student_Service(session)

    while True:
        print("\nStudent Operations")
        print("1. Add student")
        print("2. List students")
        print("3. Update student")
        print("4. Delete student")
        print("0. Back")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                student = Student(
                    name=input("Enter your name: ").strip(),
                    age=_read_int("Enter your age: "),
                    gender=_read_int("Enter your gender code: "),
                    email=input("Enter your email: ").strip(),
                    phone=_read_int("Enter your phone number: "),
                    classroom_id=_read_int("Enter your class room number: "),
                )
                created_student = await student_service.create_student(student)
                await session.commit()
                print(f"Student {created_student.id} created successfully.")

            elif choice == "2":
                students = await student_service.get_all_students()
                if not students:
                    print("No students found.")
                else:
                    for student in students:
                        print(
                            f"ID={student.id}, Name={student.name}, Age={student.age}, "
                            f"Gender={student.gender}, Email={student.email}, Phone={student.phone}, "
                            f"Classroom={student.classroom_id}"
                        )

            elif choice == "3":
                student_id = _read_int("Enter student id to update: ")
                updated_student = await student_service.update_student(
                    student_id,
                    name=input("Enter new name (leave blank to keep current): ").strip()
                    or None,
                    age=_read_optional_int(
                        "Enter new age (leave blank to keep current): "
                    ),
                    gender=_read_optional_int(
                        "Enter new gender code (leave blank to keep current): "
                    ),
                    email=input(
                        "Enter new email (leave blank to keep current): "
                    ).strip()
                    or None,
                    phone=_read_optional_int(
                        "Enter new phone number (leave blank to keep current): "
                    ),
                    classroom_id=_read_optional_int(
                        "Enter new class room number (leave blank to keep current): "
                    ),
                )
                if updated_student is None:
                    print("Student not found.")
                else:
                    await session.commit()
                    print("Student updated successfully.")

            elif choice == "4":
                student_id = _read_int("Enter student id to delete: ")
                deleted = await student_service.delete_student(student_id)
                await session.commit()
                print(
                    "Student deleted successfully." if deleted else "Student not found."
                )

            elif choice == "0":
                break

            else:
                print("Invalid choice.")

        except SQLAlchemyError as error:
            await session.rollback()
            print(f"Database error: {error}")

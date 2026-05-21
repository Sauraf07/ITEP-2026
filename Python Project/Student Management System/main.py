import json
try:
    with open("Student Management System/Students.json", "r") as file:
        students = json.load(file)

except FileNotFoundError:
    students = []

except Exception as e:
    print(f"An error occurred: {e}")
    students = []

def save_data():
    with open("Student Management System/Students.json", "w") as file:
        json.dump(students, file, indent=4)

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()


    if choice == "1":

        student_id = input("Enter Student ID: ").strip()

        duplicate = False

        for student in students:
            if student["id"] == student_id:
                duplicate = True
                break

        if duplicate:
            print("Student ID Already Exists!")
            continue

        name = input("Enter Name: ").strip()

        if name == "":
            print("Name Cannot Be Empty")
            continue

        try:
            age = int(input("Enter Age: "))
            marks = float(input("Enter Marks: "))

        except ValueError:
            print("Invalid Input! Age and Marks must be numbers.")
            continue

        if age <= 0:
            print("Invalid Age")
            continue

        if marks < 0 or marks > 100:
            print("Marks Must Be Between 0 and 100")
            continue

        course = input("Enter Course: ").strip()

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "course": course,
            "marks": marks
        }

        students.append(student)

        save_data()

        print("Student Added Successfully!")

    elif choice == "2":

        if len(students) == 0:
            print("No Students Found")

        else:
            print("\n===== STUDENT LIST =====")

            for student in students:

                print(f"""
                        ID      : {student['id']}
                        Name    : {student['name']}
                        Age     : {student['age']}
                        Course  : {student['course']}
                        Marks   : {student['marks']}
                                        """)

    elif choice == "3":

        print("\nSearch By:")
        print("1. ID")
        print("2. Name")

        search_choice = input("Enter choice: ")

        if search_choice == "1":

            search_id = input("Enter Student ID: ")

            found = False

            for student in students:

                if student["id"] == search_id:

                    print("\n===== STUDENT FOUND =====")

                    print(f"""
                        ID      : {student['id']}
                        Name    : {student['name']}
                        Age     : {student['age']}
                        Course  : {student['course']}
                        Marks   : {student['marks']}
                                            """)

                    found = True
                    break

            if not found:
                print("Student Not Found")

        elif search_choice == "2":

            search_name = input("Enter Student Name: ")

            found = False

            for student in students:

                if student["name"].lower() == search_name.lower():

                    print("\n===== STUDENT FOUND =====")

                    print(f"""
                            ID      : {student['id']}
                            Name    : {student['name']}
                            Age     : {student['age']}
                            Course  : {student['course']}
                            Marks   : {student['marks']}
                                                """)

                    found = True

            if not found:
                print("Student Not Found")

        else:
            print("Invalid Choice")

    elif choice == "4":

        update_id = input("Enter Student ID to Update: ")

        found = False

        for student in students:

            if student["id"] == update_id:

                print("\nCurrent Student Details:")

                print(f"""
                        ID      : {student['id']}
                        Name    : {student['name']}
                        Age     : {student['age']}
                        Course  : {student['course']}
                        Marks   : {student['marks']}
                """)

                print("\nEnter New Details")

                new_name = input("Enter New Name: ").strip()
                new_course = input("Enter New Course: ").strip()

                try:
                    new_age = int(input("Enter New Age: "))
                    new_marks = float(input("Enter New Marks: "))

                except ValueError:
                    print("Invalid Input")
                    break

                if new_name != "":
                    student["name"] = new_name

                if new_course != "":
                    student["course"] = new_course

                student["age"] = new_age
                student["marks"] = new_marks

                save_data()

                print("Student Updated Successfully!")

                found = True
                break

        if not found:
            print("Student Not Found")


    elif choice == "5":

        delete_id = input("Enter Student ID to Delete: ")

        found = False

        for student in students:

            if student["id"] == delete_id:

                students.remove(student)

                save_data()

                print("Student Deleted Successfully!")

                found = True
                break

        if not found:
            print("Student Not Found")

    elif choice == "6":

        print("Exiting Program...")
        break
    else:
        print("Invalid Choice")
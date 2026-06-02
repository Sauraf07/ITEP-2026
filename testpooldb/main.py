from mysql.connector import Error
from db_config import *
def fetch_all_data():
    try:
        with pool.get_connection() as conn:
            with conn.cursor() as cursor:
                sql = "select * from employee"
                cursor.execute(sql)
                data = cursor.fetchall()
                for row in data:
                    id,name,salary,age,skill,department = row
                    print(id,name,salary,age,skill,department)
                    print("---------------------------------")
    except Error as e:
        print(e)

def insert_employee():
    try:
        with pool.get_connection() as conn:
            with conn.cursor() as cursor:
                sql = "insert into employee(name,salary,age,skill,department) values(%s,%s,%s,%s,%s)"
                name = input("Enter employee name: ")
                salary = input("Enter employee salary: ")
                age = input("Enter employee age: ")
                skill = input("Enter employee skill: ")
                department = input("Enter employee department: ")
                cursor.execute(sql,(name,salary,age,skill,department))
                conn.commit()
                print("employee inserted successfully")

    except Error as e:
        if conn and conn.is_connected():
            conn.rollback()
        print(e)

# def insert():
#     con = None
#     cursor = None
#     try:
#       con = pool.get_connection()
#       cursor = con.cursor()
#       sql = "insert into employee(name,salary,department) values(%s,%s,%s)"
#       name = input("Enter employee name: ")
#       salary = float(input("Enter employee salary: "))
#       department = input("Enter department: ")
#       cursor.execute(sql,(name,salary,department))
#       if cursor.rowcount > 0:
#           print("Employee successfully added!")
#       con.commit()
#     except Error as e:
#         if con and con.is_connected():
#             con.rollback()
#         print(e)
#     finally:
#         if cursor is not None:
#             cursor.close()
#         if con is not None:
#             con.close()

#insert()

# fetch_all_data()
insert_employee()
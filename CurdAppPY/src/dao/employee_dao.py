from itertools import count

from mysql.connector import Error
from src.config.db import pool
class EmployeeDao:
    @staticmethod
    def save_employee(employee):
        try:
            with pool.get_connection() as con:
                with con.cursor() as cursor:
                    sql = "insert into employee(name,salary,age,skill,department) values(%s,%s,%s,%s,%s)"
                    cursor.execute(sql,employee.name,employee.salary,employee.age,employee.skill,employee.department)
                    con.commit()
                    return True
        except Error as e:
            print(e)
            if con and con.is_connected():
                con.rollback()
                return False
    @staticmethod
    def get_employee():
        try:
            with pool.get_connection() as con:
                with con.cursor() as cursor:
                    sql = "select * from employee"
                    cursor.execute(sql)
                    row = cursor.fetchall()
                    for row in row:
                        id,name,salary,age,skill,department = row
                        print(f"{id} : {name} : {salary} : {age} : {skill} : {department}")
        except Error as e:
            print(e)
    @staticmethod
    def update_employee(employee):
        try:
            with pool.get_connection() as con:
                with con.cursor() as cursor:
                    sql = "update employee set salary = %s,age = %s,skill = %s,department = %s where id = %s"
                    cursor.execute(sql,employee.salary,employee.age,employee.skill,employee.department)
                    con.commit()
                    return cursor.rowcount >0
        except Error as e:
            if con and con.is_connected():
                con.rollback()
            print(e)
            return False

    @staticmethod
    def delete_employee(employee):
        try:
            with pool.get_connection() as con:
                with con.cursor() as cursor:
                    sql = "delete from employee where id = %s"
                    cursor.execute(sql,employee.id)
                    con.commit()
                    print(cursor.rowcount)
                    con.commit()
                    return cursor.rowcount >0
        except Error as e:
            if con and con.is_connected():
                con.rollback()
                print(e)
                return False
    @staticmethod
    def find_employee_by_id(employee_id):
        try:
            with pool.get_connection() as con:
                with con.cursor() as cursor:
                    sql = "select * from employee where id = %s"
                    cursor.execute(sql,employee_id)
                    row = cursor.fetchone()
                    print(f"{employee_id} : {row}")

        except Error as e:
            print(e)





from db import get_connection
con = None
cursor = None
try:
    con = get_connection()
    if con is not None:
        cursor = con.cursor()
        sql = "insert into employee(name,salary,age,skill,department) values(%s,%s,%s,%s,%s)"
        list = [
            ("Nishi",60000,23,"Java","IT"),
            ("Aman",79000,20,"Html","Sales"),
            ("Arpt",90000,22,"CSS","IT"),
            ("Satya",40000,30,"Calling","Marketing")
        ]
        cursor.executemany(sql,list)
        con.commit()
        print("Record inserted successfully")
except Exception as e:
    if con is not None:
        con.rollback()
    print(e)
finally:
    if cursor is not None:
        cursor.close()
    if con is not None:
        con.close()
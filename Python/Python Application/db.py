import mysql.connector
def get_connection():
    con = None
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="school"
        )
    except mysql.connector.Error as err:
        print("Connection error: {}".format(err))
    return con
from mysql.connector import pooling
from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

try:
    pool = pooling.MySQLConnectionPool(
        pool_name="learntrack_pool",
        pool_size=10,
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PS"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT"))
    )

    # Test Connection
    conn = pool.get_connection()

    if conn.is_connected():
        print(" Database Connected Successfully!")

    conn.close()

except mysql.connector.Error as e:
    print(f" Database Connection Failed: {e}")


def get_connection():
    return pool.get_connection()
from mysql.connector import pooling
from dotenv import load_dotenv
import os
load_dotenv()
pool = pooling.MySQLConnectionPool(
    host=os.getenv("DATABASE_HOST"),
    user=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
    database=os.getenv("DATABASE_NAME"),
    pool_size=10,
)
import os
from dotenv import load_dotenv
from mysql.connector import pooling

load_dotenv()

db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

pool = pooling.MySQLConnectionPool(
    pool_name="learntrack_pool",
    pool_size=int(os.getenv("DB_POOL_SIZE", 5)),
    **db_config
)
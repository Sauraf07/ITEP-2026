from mysql.connector import Error, pooling
from dotenv import load_dotenv
import os
load_dotenv()
print(f"Database Name: {os.getenv('DATABASE_NAME')}")
pool = pooling.MySQLConnectionPool(host=os.getenv('DATABASE_HOST'),
                                   user=os.getenv('DATABASE_USER'),
                                   password=os.getenv('DATABASE_PASSWORD'),
                                   database=os.getenv('DATABASE_NAME'),
                                   pool_size=10)
import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv

# Connect to PostgreSQL database

# Load environment variables from .env file
load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

cur = conn.cursor()


# Function to retrieve data from the database
def get_households_by_username(username):
    query = """
        SELECT h.*
        FROM households h
        JOIN users u ON h.user_id = u.user_id
        WHERE u.username = %s
    """
    cur.execute(query, (username,))
    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    return pd.DataFrame(rows, columns=columns)

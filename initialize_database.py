import psycopg2
from faker import Faker
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

# Create tables with indexes and partitioning
cur.execute("""
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(50)
)
""")

cur.execute("""
CREATE TABLE households (
    household_id SERIAL,
    user_id INTEGER,
    income INTEGER,
    num_people INTEGER,
    address VARCHAR(100),
    PRIMARY KEY (household_id, user_id)
) PARTITION BY HASH (user_id)
""")

# Create partitions
cur.execute("""
CREATE TABLE households_part1 PARTITION OF households
    FOR VALUES WITH (MODULUS 4, REMAINDER 0)
""")

cur.execute("""
CREATE TABLE households_part2 PARTITION OF households
    FOR VALUES WITH (MODULUS 4, REMAINDER 1)
""")

cur.execute("""
CREATE TABLE households_part3 PARTITION OF households
    FOR VALUES WITH (MODULUS 4, REMAINDER 2)
""")

cur.execute("""
CREATE TABLE households_part4 PARTITION OF households
    FOR VALUES WITH (MODULUS 4, REMAINDER 3)
""")

# Create indexes
cur.execute("CREATE INDEX idx_user_id ON households(user_id)")
cur.execute("CREATE INDEX idx_user_income ON households(user_id, income)")

# Generate fake data
fake = Faker()

# Insert ~10 fake users
for _ in range(10):
    cur.execute("""
    INSERT INTO users (username, email)
    VALUES (%s, %s)
    """, (fake.user_name(), fake.email()))

# Insert ~300,000 fake entries per user in households table
cur.execute("SELECT user_id FROM users")
user_ids = cur.fetchall()

for user_id in user_ids:
    for _ in range(300000):
        cur.execute("""
        INSERT INTO households (user_id, income, num_people, address)
        VALUES (%s, %s, %s, %s)
        """, (user_id[0], fake.random_int(min=20000, max=200000), fake.random_int(min=1, max=10), fake.address()))

# Commit changes and close connection
conn.commit()
cur.close()
conn.close()

print("Tables created and data inserted successfully.")

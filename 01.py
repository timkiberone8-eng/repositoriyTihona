import psycopg2
from datetime import date

# 1) создаём БД из postgres
conn = psycopg2.connect(dbname="postgres", user="postgres",
                        password="postgres", host="127.0.0.1", port="5432")
conn.autocommit = True
cur = conn.cursor()
cur.execute("DROP DATABASE IF EXISTS sales_data")
cur.execute("CREATE DATABASE sales_data")
cur.close(); conn.close()
print("база создана")

# 2) подключаемся к новой БД
conn = psycopg2.connect(dbname="sales_data", user="postgres",
                        password="postgres", host="127.0.0.1", port="5432")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    quantity INT,
    price DECIMAL(10,2),
    sales_date DATE
)
""")
print("таблица создана")

sales_data = [
    ("Laptop",     10, 700, date(2024, 1, 10)),
    ("Smartphone", 25, 300, date(2024, 1, 11)),
    ("Tablet",     15, 250, date(2024, 1, 12)),
    ("Headphones", 50,  50, date(2024, 1, 13)),
    ("Smartwatch", 30, 150, date(2024, 1, 14)),
]

cur.executemany(
    "INSERT INTO sales (product_name, quantity, price, sales_date) VALUES (%s,%s,%s,%s)",
    sales_data
)
conn.commit()
print("данные добавлены")

cur.close(); conn.close()
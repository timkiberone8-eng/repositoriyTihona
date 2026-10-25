import psycopg2
from datetime import date

conn = psycopg2.connect(dbname="sales_data", user="postgres",
                        password="postgres", host="127.0.0.1", port="5432")
cur = conn.cursor()

cur.execute("DELETE FROM sales")

sales_data = [
    ("Laptop",     10, 700, date(2024, 1, 10)),
    ("Smartphone", 25, 300, date(2024, 1, 11)),
    ("Tablet",     15, 250, date(2024, 1, 12)),
    ("Headphones", 50,  50, date(2024, 1, 13)),
    ("Smartwatch", 30, 150, date(2024, 1, 14)),
]

cur.executemany(
    "INSERT INTO sales (product_name, quantity, price, sale_date) VALUES (%s,%s,%s,%s)",
    sales_data
)
conn.commit()
print("данные добавлены")

cur.close(); conn.close()

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

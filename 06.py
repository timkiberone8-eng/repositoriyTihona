import psycopg2


connection = psycopg2.connect(dbname="sales_data", user="postgres",
                        password="postgres", host="127.0.0.1", port="5432")

cursor = connection.cursor()

cursor.execute("""
SELECT sales_date, SUM(quantity)AS total_quantity
FROM sales
GROUP BY sales_date
ORDER BY sales_date
""")
daily_sales_data = cursor.fetchall()
for row in daily_sales_data:
    print(f"дата: {row[0]}, продано: {row[1]}")

cursor.close()
connection.close()

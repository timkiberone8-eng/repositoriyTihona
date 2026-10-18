import psycopg2
import matplotlib.pyplot as plt

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
cursor.close()
connection.close()
dates=[row[0] for row in daily_sales_data]
quantities = [row[1]for row in daily_sales_data]

plt.figure(figsize=(10,6))
plt.plot(dates,quantities,color='blue',marker="o")
plt.title("количсетво проданных продуктов по дате")
plt.xlabel("дата")
plt.ylabel("количество")
plt.xticks(rotation=45)
plt.show()
import psycopg2

conn = psycopg2.connect(dbname="postgres", user="postgres",
                        password="postgres", host="127.0.0.1", port="5432")
conn.autocommit = True
cur = conn.cursor()

cur.execute("DROP DATABASE IF EXISTS sales_data")
cur.execute("CREATE DATABASE sales_data")
cur.close(); conn.close()
print("база создана")

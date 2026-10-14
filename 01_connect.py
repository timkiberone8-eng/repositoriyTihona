import psycopg2

# 1) создаём БД из postgres
conn = psycopg2.connect(dbname="postgres", user="postgres",
                        password="postgres", host="127.0.0.1", port="5432")
conn.autocommit = True
cur = conn.cursor()

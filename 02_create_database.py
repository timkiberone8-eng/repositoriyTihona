cur.execute("DROP DATABASE IF EXISTS sales_data")
cur.execute("CREATE DATABASE sales_data")
cur.close(); conn.close()
print("база создана")

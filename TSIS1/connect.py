import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="tsis1",
    user="postgres",
    password="12345678"
)

cur = conn.cursor()
cur.execute("SELECT * FROM students")

rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()
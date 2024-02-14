import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="",
    user="",
    password="")
cur = conn.cursor()
print('PostgreSQL database version')
cur.execute('Select * from student;')
db_version = cur.fetchone()
print(db_version)


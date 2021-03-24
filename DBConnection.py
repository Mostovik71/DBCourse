import psycopg2
con = psycopg2.connect(
  database="TestDB",
  user="postgres",
  password="12345",
  host="127.0.0.1",
  port="5432"
)
cur = con.cursor()

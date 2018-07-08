import psycopg2

try:
    conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='abc123'")
except:
    print("I am unable to connect to the database")

cur = conn.cursor()

# gets all the databases on this host
cur.execute("""SELECT datname from pg_database""")

rows = cur.fetchall()

print("\nShow me the databases:\n")
for row in rows:
    print("   ", row[0])
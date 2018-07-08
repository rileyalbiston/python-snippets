# Python PostgreSQL Connection

# import psycopg2 module
import psycopg2

# create a Connection object that represents the database
conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='abc123'")

# create a Cursor object
cur = conn.cursor()

# gets all the databases on this host
cur.execute("""SELECT datname from pg_database""")

rows = cur.fetchall()

print("\nShow me the databases:\n")
for row in rows:
    print("   ", row[0])

# close the connection if you are done with it.
# be sure any changes have been committed or they will be lost.
conn.close()
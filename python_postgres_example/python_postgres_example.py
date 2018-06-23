import psycopg2
import sys
import csv

# https://wiki.postgresql.org/wiki/Using_psycopg2_with_PostgreSQL
# http://www.postgresqltutorial.com/postgresql-python/connect/
# https://wiki.postgresql.org/wiki/Psycopg2_Tutorial
# https://www.dataquest.io/blog/loading-data-into-postgres/
# http://initd.org/psycopg/docs/cursor.html


def connection():
	try:
	    conn = psycopg2.connect("dbname='mydb' user='postgres' host='localhost' password='abc123'")
	    print("Connecting to database\n	->%s" % (conn))
	    return conn
	except:
	    print("Unable to connect to the database")


def test():
	try:
		# connect to the PostgreSQL server
		conn = connection()
		# create a cursor
		cursor = conn.cursor()
		print("Connected!\n")
	except:
		print("No connection")


def basic_query():
	try:
		# connect to the PostgreSQL server
		conn = connection()
		# create a cursor
		cursor = conn.cursor()
		print("Connected!\n")
		# execute a statement
		cursor.execute('SELECT * FROM persons')
		# fetch all rows
		all = cursor.fetchall()
		for p in all:
			print(p)
		# close the communication with the PostgreSQL
		cursor.close()
	except:
		print("No connection")
	finally:
		if conn is not None:
			conn.close()
			print('Database connection closed.')



def create_table():
	try:
		# connect to the PostgreSQL server
		conn = connection()
		# create a cursor
		cursor = conn.cursor()
		print("Connected!\n")
		# execute a statement
		cursor.execute("""
		CREATE TABLE users(
			id integer PRIMARY KEY,
			email text,
			name text,
			address text
		)
		""")
		# commit the transaction
		conn.commit()
		# close the communication with the PostgreSQL
		cursor.close()
	except:
		print("No connection")
	finally:
		if conn is not None:
			conn.close()
			print('Database connection closed.')


def insert_data():
	try:
		# connect to the PostgreSQL server
		conn = connection()
		# create a cursor
		cursor = conn.cursor()
		print("Connected!\n")
		# execute a statement
		cursor.execute("INSERT INTO users VALUES (%s, %s, %s, %s)", (10, 'hello@dataquest.io', 'Some Name', '123 Fake St.'))
		# commit the transaction
		conn.commit()
		# close the communication with the PostgreSQL
		cursor.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
			print('Database connection closed.')


def csv_insert_by_row():
	try:
		# connect to the PostgreSQL server
		conn = connection()
		# create a cursor
		cursor = conn.cursor()
		print("Connected!\n")
		# open and read the csv then insert values
		with open('C:\\Users\\Riley\\Desktop\\persons.csv', 'r') as f:
			reader = csv.reader(f)
			next(reader)  # Skip the header row.
			for row in reader:
				cursor.execute("INSERT INTO persons (first_name, last_name, dob, email) VALUES (%s, %s, %s, %s)", row)
		# commit the transaction
		conn.commit()
		# close the communication with the PostgreSQL
		cursor.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
			print('Database connection closed.')


def copy_csv():
	try:
		# connect to the PostgreSQL server
		conn = connection()
		# create a cursor
		cursor = conn.cursor()
		print("Connected!\n")
		# open csv and use copy_from to import the CSV
		with open('C:\\Users\\Riley\\Desktop\\persons.csv', 'r') as f:
			# Notice that we don't need the `csv` module.
			next(f)  # Skip the header row.
			cursor.copy_from(f, 'persons', sep=',', columns=('first_name', 'last_name', 'dob', 'email')) # use 'columns' because csv doesn't contain an ID column. MUST match database column NAMES, not csv headers!!!
		# commit the transaction
		conn.commit()
		# close the communication with the PostgreSQL
		cursor.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
			print('Database connection closed.')	


#test()
#create_table()
#insert_data()
#csv_insert_by_row()
#copy_csv()

basic_query()


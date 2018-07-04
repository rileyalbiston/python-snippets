import psycopg2
import sys
import json

def connection():
	try:
	    conn = psycopg2.connect("dbname='mydb' user='postgres' host='localhost' password='abc123'")
	    print("Connecting to database\n	->%s" % (conn))
	    return conn
	except:
	    print("Unable to connect to the database")


def basic_query():
	try:
		# connect to the PostgreSQL server
		conn = connection()
		# create a cursor
		cursor = conn.cursor()
		print("Connected!\n")
		# execute a statement
		cursor.execute('SELECT first_name, last_name FROM persons')
		# fetch all rows
		keys = [desc[0] for desc in cursor.description]
		print(type(keys))
		print(keys, '\n')

		values = cursor.fetchall()
		print(type(values))
		print(values, '\n')

		dictionary = dict(zip(keys, values))
		print(type(dictionary))
		print(dictionary, '\n')

		# close the communication with the PostgreSQL
		cursor.close()

	except:
		print("Query no go")
	finally:
		if conn is not None:
			conn.close()
			print('Database connection closed.')


basic_query()
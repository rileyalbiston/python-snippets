

# the query result must take the form:
'''
persons = [
    {
        'first_name': u'Bob',
        'last_name' : u'East'
    },
    {
        'first_name': u'Harry',
        'last_name' : u'West'    
    }
]
'''
'''
import psycopg2
import sys
import json




def connection():
    try:
        conn = psycopg2.connect("dbname='mydb' user='postgres' host='localhost' password='abc123'")
        print("Connecting to database\n ->%s" % (conn))
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
        
#        keys = [desc[0] for desc in cursor.description]
#        print(type(keys))
#        print(keys, '\n')
#
        values = cursor.fetchall()
#        print(type(values))
#        print(values, '\n')

        #things = [dict(zip(keys, row)) for row in cursor.fetchall()]
        #things = [dict(zip(['thing_id', 'thing_name'], row)) for row in cursor.fetchall()]

        keys = [desc.name for desc in cursor.description]
        data = [dict(zip(keys, value)) for value in values]

#        print(json.dumps(data, indent=4))

        # close the communication with the PostgreSQL
        cursor.close()
        conn.close()
        print('Database connection closed.')
    except:
        print("No connection")

    return json.dumps(data, indent=4)


print(basic_query())
'''
person = {
    'first_name': 'fi',
    'last_name': 'la',
}

print(type(person))
print(person)
print(person['first_name'])
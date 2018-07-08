#Python SQL Server connection

#import pypyodbc module
import pypyodbc

# create connection to database
# This connection uses a trusted connection. It is used when sql server is configured to use windows authenification.
conn = pypyodbc.connect(
    'Driver={SQL Server};' 
    'Server=SERVERNAME;' 
    'Database=test_db;' 
    'Trusted_connection=yes;'
    )

# create connection with user id and password
'''
db_host = 'serverhost'
db_name = 'database'
db_user = 'username'
db_password = 'password'
connection_string = 'Driver={SQL Server};Server=' + db_host + ';Database=' + db_name + ';UID=' + db_user + ';
conn = pypyodbc.connect(connection_string)
'''

# create a Cursor object
cur = conn.cursor()

# query the database
cur.execute('SELECT * FROM dbo.customers')

# for each row in the query result print the id and name
for row in cur:
    #print('ID = %r' % (row[0]), 'Name = %r' % (row[1]))
    cust_id = row[0]
    cust_name =  row[1]
    print(cust_id, cust_name)

    
# close the connection if you are done with it.
# be sure any changes have been committed or they will be lost.
conn.close()
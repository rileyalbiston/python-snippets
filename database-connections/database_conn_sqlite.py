# Python SQLite connection

# import sqlite3 module
import sqlite3

# create a Connection object that represents the database
conn = sqlite3.connect('python_sqlite_demo.db')

# create a Cursor object
cur = conn.cursor()

# create table
cur.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)
        ''')

# example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]

cur.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

# Save (commit) the changes
conn.commit()

# query the database
for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)    
'''
('2017-05-05', 'BUY', 'CBA', 100.0, 12.34)
('2017-05-05', 'BUY', 'XYZ', 100.0, 12.34)
('2006-03-28', 'BUY', 'IBM', 1000.0, 45.0)
('2006-04-06', 'SELL', 'IBM', 500.0, 53.0)
('2006-04-05', 'BUY', 'MSFT', 1000.0, 72.0)
'''

# close the connection if you are done with it.
# be sure any changes have been committed or they will be lost.
conn.close()
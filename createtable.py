import sqlite3


conn = sqlite3.connect('test.db')

print "Opened database successfully";



conn.execute('''CREATE TABLE RESULTS

		(ID INT PRIMARY KEY    NOT NULL,
		UUID           TEXT    NOT NULL,
		DATA           TEXT    NOT NULL);''')

print "Table created successfully";

conn.close()
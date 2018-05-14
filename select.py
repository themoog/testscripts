import sqlite3



conn = sqlite3.connect('test.db')

print "Opened database successfully";



cursor = conn.execute("SELECT ID, UUID, DATA from RESULTS")

for row in cursor:
	print "ID = ", row[0]
	print "UUID = ", row[1]
	print "DATA = ", row[2],"\n"

print "Operation done successfully";
conn.close()
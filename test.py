from easysnmp import Session
import uuid
import sqlite3
import sys

def printTest():
	print "testprinttest"

def getSnmpTrap():

	#Create an SNMP session to be used for all our requests
	session = Session(hostname='127.0.0.1', community='public', version=2)

	snmpTag1 = ".1.3.6.1.2.1.1.1.0"
	
	result = str(session.get(snmpTag1)).split("'")

	return result[1]


def insertIntoDatabase():

	import sqlite3
	conn = sqlite3.connect('test.db')
	print "Opened database successfully";


	conn.execute("INSERT INTO RESULTS (ID,UUID,DATA) \
		VALUES (?,?,?);", (str(uuid.uuid4()),getSnmpTrap(),"14"))

	conn.commit()
	print "Records created successfully";
	conn.close()


def main():


	
	#conn = sqlite3.connect('test.db')
	#print "Opened database successfully";


	print getSnmpTrap()
	insertIntoDatabase()


if __name__ == "__main__":
	main()









	
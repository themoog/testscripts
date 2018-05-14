from easysnmp import Session
import uuid
import sqlite3




def main():


	
	#conn = sqlite3.connect('test.db')
	#print "Opened database successfully";

	print "Main Function"

	#getSnmpTrap()
	#insertIntoDatabase()
	printTest()


if __name__ == "__main__":
	main()





def getSnmpTrap():

	#Create an SNMP session to be used for all our requests
	session = Session(hostname='127.0.0.1', community='public', version=2)

	snmpTag1 = ".1.3.6.1.2.1.1.1.0"
	description = session.get(snmpTag1)
	result = str(description)
	description2 = result.split("'")
	print description2[1]	



def insertIntoDatabase():

	import sqlite3
	conn = sqlite3.connect('test.db')
	print "Opened database successfully";


	conn.execute("INSERT INTO RESULTS (ID,UUID,DATA) \
		VALUES (?,?,?);", (str(uuid.uuid4()),"23","14"))

	conn.commit()
	print "Records created successfully";
	conn.close()

def printTest():
	print "testprinttest"
	
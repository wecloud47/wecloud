import MySQLdb

# Methods for opening database for all and returning db and cur
def db_open():
#	Change host , username , password and db to suit
#	db = MySQLdb.connect(host="10.4.1.245",user="dg417",passwd="dg",db='prodrptdb')
#	db = MySQLdb.connect(host="mysql.server",user="dragontour",passwd="benny",db='dragontour$default')
	db = MySQLdb.connect(host="localhost",user="root",passwd="benny6868",db='wecloud')
	cursor = db.cursor()
	return db, cursor
def db_set(request):
#	Change host , username , password and db to suit
#	db = MySQLdb.connect(host="10.4.1.245",user="dg417",passwd="dg",db='prodrptdb')
#	db = MySQLdb.connect(host="mysql.server",user="dragontour",passwd="benny",db='dragontour$default')
	db = MySQLdb.connect(host="localhost",user="root",passwd="benny6868",db='wecloud')
	cursor = db.cursor()
	return db, cursor

	

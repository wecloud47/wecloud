from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import os, sys
import MySQLdb

def image_setup(request):
	db = MySQLdb.connect(host="localhost", user="weclouduser", passwd="benny6868", db='wecloud')
	cursor = db.cursor()
	cursor.execute ("""CREATE TABLE IF NOT EXISTS test(Id INT PRIMARY KEY AUTO_INCREMENT, number INT(10))""")
	db.commit()
	db.close()
	return render(request,'thankyou.html')

def read_image():
	a = "man.jpeg"
	fin = open(a)
	img = fin.read()
	
	return img

def image_write(request):
	
	dpic = read_image()
#	os.mkdir("jackpotbrandon")
#	os.remove("woman.jpeg")
	a = "onetimeman.jpeg"
	fin = open(a,"w")
	
	
	
	
	fin.write(dpic)
	fin.close()
	# increment page test counter
#	x = request.session["p_test"] 
#	x = x + 1
#	request.session["p_test"] = x
#	y=int(x)
	
#	db = MySQLdb.connect(host="localhost", user="weclouduser", passwd="benny6868", db='wecloud')
#	cursor = db.cursor()
##	cursor.execute ("""insert into images(Data) values("%s")""" % (dpic))
#	sqD =( 'insert into test(number) values("%d")' % (y) )
#	sqD = "INSERT INTO images(Data) VALUES(%s)"
#	cursor.execute(sqD,(dpic))

	
#	**********Example from Stack overflow about insert BLOB ********************	
#	thedata = open('thefile', 'rb').read()
#	sql = "INSERT INTO sometable (theblobcolumn) VALUES (%s)"
#	cursor.execute(sql, (thedata,))
#	****************************************************************************

#	db.commit()
#	db.close()
	
	
	return render(request,'thankyou.html')


#******************************************************************************************************************
#***************  View on Various DB Modifications    ********************************************************
#******************************************************************************************************************

from django.shortcuts import render_to_response
from django.shortcuts import render
from firstsite.wec.views_db import db_open


# *****************************************************************************
# Modify a Table to add a column              								         
# *****************************************************************************
def create_column(request):
	colName = "app"
	db, cursor = db_open()
	# Add a column in table wec_main
	query = "ALTER TABLE wec_main ADD %s varchar(200) NULL" % (colName)
	cursor.execute(query)
	db.commit()
	db.close()
	request.session["test"] = "Added Column " + colName
	return render(request, 'done2.html')

# *****************************************************************************
# Delete a column in a table 
# *****************************************************************************
def delete_column(request):
	colName = "app"
	db, cursor = db_open()
	try:
		query = "ALTER TABLE wec_main DROP %s" % (colName)
		cursor.execute(query)
		db.commit()
	except:
		dummy = 1
	db.close()
	request.session["test"] = "Deleted Column " + colName
	return render(request, 'done2.html')

# *****************************************************************************
# Modify the structure of a column	
# *****************************************************************************
def change_column(request):
	colName = "status"
	db, cursor =db_open()
	try:
		query = "ALTER TABLE wec_members MODIFY %s INT(11) NULL" % (colName)
		cursor.execute(query)
		db.commit()
	except:
		colName = colName + " FAILED !!!!"
		dummy = 1
	db.close()
	request.session["test"] = "Altered Structure of column " + colName
	return render(request, 'done2.html')
	
def change_column2(request):
	colName = "address"
	info = ["" for x in range(7)]
	info[0] = "password_v"
	info[1] = "email"
	info[2] = "address"
	info[3] = "city"
	info[4] = "country"
	info[5] = "code"
	info[6] = "phone"
	
	
	db, cursor =db_open()
	for y in range(0,7):
		colName = info[y]
		try:
			query = "ALTER TABLE wec_members MODIFY %s VARCHAR(70) NULL" % (colName)
			cursor.execute(query)
			db.commit()
		except:
			colName = colName + " FAILED !!!!"
			dummy = 1
			
			
	db.close()
	request.session["test"] = "Altered Structure of column " + colName
	return render(request, 'done2.html')	

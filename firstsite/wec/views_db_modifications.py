#******************************************************************************************************************
#***************  View on Various DB Modifications    ********************************************************
#******************************************************************************************************************

from django.shortcuts import render_to_response
from django.shortcuts import render
from firstsite.wec.views_db import db_open


# ***********************************************************************************
# Modify a Table to add a column              								         *
#                                           										*
# ***********************************************************************************

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
	

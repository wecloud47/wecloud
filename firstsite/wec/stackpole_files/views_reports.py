from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from time import strftime
from datetime import datetime
import MySQLdb
import time


# Updated August 20,2015
# Module to retrieve report information

def production_report_date(request):

	# Assign machine names.  Later this can be input as a table for now it 
	# will be hardcoded
	machine_list = [677,748,749,750]
#	total = [0,0,0,0]
#	part = [0,0,0,0]

	# inintialze for 12 now but should be table value based on number of machines x 3 shifts
	total = [0 for x in range(12)] 
	part = [0 for x in range(12)] 
	machine = [0 for x in range(12)]
	stamp = [0 for x in range(12)]
	tctr = [0 for x in range(12)]
	part_total = ["50-3632","50-0786","50-4916"]
	shift = [0 for x in range(12)]
	# Number of Machines
	num_machines = 4
	
	start_date = request.session["s_date"]
	
	
	try:
		temp = datetime.strptime(start_date,"%Y-%m-%d")
		start_stamp = int(time.mktime(temp.timetuple()))
		start_tuple = time.localtime(start_stamp)
	except:
		start_stamp=""
		start_tuple=""

		
	db = MySQLdb.connect(host="10.4.1.245",user="dg417",passwd="dg",db='prodrptdb')
	cursor = db.cursor()
	ctr = 0
	ctr2 = 0
	# Loop to respective number of machines, this will be tabled later on
	for i in range(0, 3):
		st = start_stamp - 3600
		fi = start_stamp + 25200
		
		for ii in range(0, num_machines):
		
			try:
				sql = "SELECT SUM(qty) FROM tkb_prodtrak where machine = '%s' AND part_timestamp > '%d' AND part_timestamp < '%d'" %(machine_list[ii], st, fi)
				cursor.execute(sql)
				tmp = cursor.fetchall()
				tmp2 = tmp[0]
				total[ctr] = tmp2[0]
			
		
				sqm = "SELECT (part_number) FROM tkb_prodtrak where machine = '%s' AND part_timestamp > '%d' AND part_timestamp < '%d'" %(machine_list[ii], st, fi)
				cursor.execute(sqm)
				tmp = cursor.fetchall()
				tmp2 = tmp[0]
				part[ctr] = tmp2[0]
			except:
				total[ctr] = 0
				part[ctr] = 0

				
			
			machine[ctr] = machine_list[ii]
			stamp[ctr] = start_stamp
			tctr[ctr] = ctr2

			if ctr == 0:
				shift[ctr] = ctr2+1
			elif ctr == 4:
				shift[ctr] = ctr2+1
			elif ctr == 8:
				shift[ctr] = ctr2+1
			elif ctr == 3:
				shift[ctr] = 99	
			elif ctr == 7:
				shift[ctr] = 99

			try:
				if tctr[ctr-1] == tctr[ctr]:
					tctr[ctr] = -1
			except:
				tctr[ctr] = ctr2
			ctr = ctr + 1
			
		start_stamp = start_stamp + 28800
		ctr2 = ctr2 + 1
		
	list = zip(machine,total,part,shift)
	return render(request, "report_page_day.html", {'List':list, 'S':start_tuple})

def production_report(request):

	machine_list = [677,748,749,750]
	total = [0,0,0,0]
	part = [0,0,0,0]
	
	start_date = request.session["s_date"]
	end_date = request.session["e_date"]
	
#	temp = datetime.strptime(start_date,"%Y-%m-%dT%H:%M")
	temp = datetime.strptime(start_date,"%Y-%m-%d")
	start_stamp = int(time.mktime(temp.timetuple()))
	start_tuple = time.localtime(start_stamp)

#	temp = datetime.strptime(end_date,"%Y-%m-%dT%H:%M")
	temp = datetime.strptime(end_date,"%Y-%m-%d")
	end_stamp = int(time.mktime(temp.timetuple()))
	end_tuple = time.localtime(end_stamp)	

	db = MySQLdb.connect(host="10.4.1.245",user="dg417",passwd="dg",db='prodrptdb')
	cursor = db.cursor()
	
	for i in range(0, 4):
	
		sql = "SELECT SUM(qty) FROM tkb_prodtrak where machine = '%s' AND part_timestamp > '%d' AND part_timestamp < '%d'" %(machine_list[i], start_stamp, end_stamp)
		cursor.execute(sql)
		tmp = cursor.fetchall()
		tmp2 = tmp[0]
		total[i] = tmp2[0]
		
		sqm = "SELECT (part_number) FROM tkb_prodtrak where machine = '%s' AND part_timestamp > '%d' AND part_timestamp < '%d'" %(machine_list[i], start_stamp, end_stamp)
		cursor.execute(sqm)
		tmp = cursor.fetchall()
		tmp2 = tmp[0]
		part[i] = tmp2[0]
	
	list = zip(machine_list,total,part)
	return render(request, "report_page.html", {'List':list , 'S':start_tuple, 'E':end_tuple})
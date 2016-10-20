from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from django.http import QueryDict
import MySQLdb
import json
import time
from time import mktime
import datetime


# ********Imports for Stackpole Locals**********

#from trakberry.forms import sup_downForm, sup_dispForm
#from trakberry.views import done
# from trakberry.db import db_open
# ----------------------------------------------


# ********Imports for Testing Locals  **********

from firstsite.wec.db import db_open
from firstsite.wec.forms import sup_downForm, sup_dispForm
from firstsite.wec.views import done
# ----------------------------------------------

from django.core.context_processors import csrf


def supervisor_display(request):
	try:
		request.session["login_supervisor"] 
	except:
		request.session["login_supervisor"] = "none"
			
  # initialize current time and set 'u' to shift start time
	t=int(time.time())
	tm = time.localtime(t)
	c = []
	date = []
	prob = []
	job = []
	priority = []
	id = []
	machine = []
	count = []
	tmp2=[]
	smp2=[]
	mach_cnt = []
	whos = []
	box_colour = []
  
  # Select prodrptdb from db
	db, cursor = db_open()
	
  # Select prodrptdb db old style (uncomment if above one doesn't work)
#	db = MySQLdb.connect(host="10.4.1.245",user="dg417",passwd="dg",db='prodrptdb')

	cursor = db.cursor()

	#sqlA = "SELECT SUM(qty) FROM tkb_prodtrak where machine = '%s' AND time >= '%d'" %(machine_list[i], u)
	  # Select the Qty of entries for selected machine table from the current shift only 
	  # and assign it to 'count'
	
	
	c = ["tech","Jim Barker"]

	
	d1 = '2015-05-01'
	d2 = '2015-07-01'
	SQ_Sup = "SELECT * FROM pr_downtime1 where closed IS NULL" 

	cursor.execute(SQ_Sup)
	tmp = cursor.fetchall()
	
	ctr = 0
	for x in tmp:
	
		
		clr = "blue"
		if ctr > 3:
			clr = "red"
		tmp2 = (tmp[ctr])
		# assign job date and time to dt
		dt = tmp2[2]
		dt_t = time.mktime(dt.timetuple())
		# assign current date and time to dtemp
		dtemp = datetime.datetime.now()
		dtemp_t = time.mktime(dtemp.timetuple())
		# assign d_diff to difference in unix
		d_diff = dtemp_t - dt_t
		
		if d_diff < 1801:
			clr = "green"
		elif d_diff < 3601:
			clr = "yellow"
		elif d_diff < 10801:
			clr = "red"
		elif d_diff < 86400:
			clr = "black"
		else:
			clr = "#DB2602"
			
		temp1_job = tmp2[0]
		temp2_job = temp1_job[:15]
		job.append(temp2_job)
		prob.append(tmp2[1])
		
		priority.append(tmp2[3])
		id.append(tmp2[11])
		whos.append(tmp2[4])
		box_colour.append(clr)
		ctr = ctr + 1
		
	for i in range(0, ctr-1):
		for ii in range(i+1, ctr):
			if (priority[ii]) < (priority[i]):
				jjob = job[i]
				job[i] = job[ii]
				job[ii] = jjob
				pprob = prob[i]
				prob[i] = prob[ii]
				prob[ii] = pprob
				pprior = priority[i]
				priority[i] = priority[ii]
				priority[ii] = pprior
				iid = id[i]
				id[i] = id[ii]
				id[ii]= iid
				wwhos = whos[i]
				whos[i] = whos[ii]
				whos[ii] = wwhos
				bbox_colour = box_colour[i]
				box_colour[i] = box_colour[ii]
				box_colour[ii] = bbox_colour
	
	list = zip(job,prob,id,whos,priority,box_colour)	
	db.close()
	n = "none"
	
	# Set Form Variables 
	if request.POST:
		request.session["test"] = 999
		a = request.POST
		b=int(a.get("one"))
		if b == -1:
			return done(request)
		if b == -2:
			return done_tech(request)
		if b == -3:
			return done_elec(request)	
		request.session["index"] = b
		#request.session["test"] = request.POST
		return done_edit(request)
	else:
		form = sup_dispForm()
	args = {}
	args.update(csrf(request))
	args['form'] = form
	
		
		
  # call up 'display.html' template and transfer appropriate variables.  
	return render(request,"supervisor.html",{'L':list,'N':n,'args':args})
def sup_d(request):
	return supervisor_display(request)
	
def supervisor_tech_call(request):
	request.session["whoisonit"] = 'tech'
	return supervisor_down(request)

def supervisor_elec_call(request):
	request.session["whoisonit"] = 'maintenance'
	return supervisor_down(request)

def supervisor_main_call(request):
	request.session["whoisonit"] = 'maintenance'
	return supervisor_down(request)	
	
def supervisor_down(request):	

	if request.POST:
        			
		machinenum = request.POST.get("machine")
		problem = request.POST.get("reason")
		priority = request.POST.get("priority")
		whoisonit = request.session["whoisonit"]
		t = datetime.datetime.now()
		
		db = MySQLdb.connect(host="10.4.1.245",user="dg417",passwd="dg",db='prodrptdb')
		cur = db.cursor()
		cur.execute('''INSERT INTO pr_downtime1(machinenum,problem,priority,whoisonit,called4helptime) VALUES(%s,%s,%s,%s,%s)''', (machinenum,problem,priority,whoisonit,t))
		db.commit()
		db.close()
		
		return done(request)
		
	else:
		request.session["machinenum"] = "692"
		form = sup_downForm()
	args = {}
	args.update(csrf(request))
	args['form'] = form
	#request.session["login_tech"] = "none"
	return render(request,'supervisor_down.html', args)	

# Module to edit entry	
def supervisor_edit(request):	
	index = request.session["index"]
	db = MySQLdb.connect(host="10.4.1.245",user="dg417",passwd="dg",db='prodrptdb')
	cursor = db.cursor()
	SQ_Sup = "SELECT * FROM pr_downtime1 where idnumber='%s'" %(index)
	cursor.execute(SQ_Sup)
	tmp = cursor.fetchall()
	tmp2=tmp[0]
	request.session["machinenum"] = tmp2[0]
	request.session["problem"] = tmp2[1]
	request.session["priority"] = tmp2[3]
	db.close()	
	
	if request.POST:
        			
		machinenum = request.POST.get("machine")
		problem = request.POST.get("reason")
		priority = request.POST.get("priority")
		whoisonit = 'tech'
		
		db = MySQLdb.connect(host="10.4.1.245",user="dg417",passwd="dg",db='prodrptdb')
		cur = db.cursor()
		mql =( 'update pr_downtime1 SET machinenum="%s" WHERE idnumber="%s"' % (machinenum,index))
		cur.execute(mql)
		db.commit()
		tql =( 'update pr_downtime1 SET problem="%s" WHERE idnumber="%s"' % (problem,index))
		cur.execute(tql)
		db.commit()
		uql =( 'update pr_downtime1 SET priority="%s" WHERE idnumber="%s"' % (priority,index))
		cur.execute(uql)
		db.commit()
		db.close
		#db = MySQLdb.connect(host="10.4.1.245",user="dg417",passwd="dg",db='prodrptdb')
		#cur = db.cursor()
		#cur.execute('''INSERT INTO pr_downtime1(machinenum,problem,priority,whoisonit) VALUES(%s,%s,%s,%s)''', (machinenum,problem,priority,whoisonit))
		#db.commit()
		#db.close()
		
		return done(request)
		#return render(request, "test.html", {'machine':machinenum , 'index':index})
		
	else:	
		form = sup_downForm()
	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render(request,'supervisor_edit.html', args)		

def done_tech(request):
	#request.session["test"] = 78
	return render(request, "done_tech.html")
def done_elec(request):
	#request.session["test"] = 78
	return render(request, "done_elec.html")	
def done_edit(request):
	#request.session["test"] = 78
	return render(request, "done_edit.html")		
	
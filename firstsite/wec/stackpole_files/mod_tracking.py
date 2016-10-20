from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from views import display, test
from views_reports import production_report, production_report_date
from trakberry.forms import part_number, report_dateForm
import MySQLdb
import time
from django.core.context_processors import csrf

# Updated June 10,2015

# Module to simulate Machine Inputs for M/C  677 , 748 , 749 , 750

# Module to Take entry simulate Pi 
# Eventually this module will link create and enter data into MySQL from button presses to simulate machine operation
# so we can run the view on another terminal to test.
def edit_part(request):
	request.session["details_track"] = 1
	p = 101
	
	mc = ""
	prt = ""
	try:
		request.session["prt"]
	except:
		request.session["prt"] = "" 
	try:
		request.session["mc"]
	except:
		request.session["mc"] = ""
		
	if request.POST:

		mc = request.POST.get("mc")
		request.session["mc"] = mc
		prt = request.POST.get("part")
		request.session["prt"] = prt	
		t = int(time.time())
		db = MySQLdb.connect(host="10.4.1.245",user="dg417",passwd="dg",db='prodrptdb')
		cur = db.cursor()
		sql =( 'insert into tkb_prodtrak(pi_id,machine,part_timestamp,part_number) values("%s","%s","%s","%s")' % (p,mc,t,prt) )
		
		cur.execute(sql)
		db.commit()
		db.close()		

		request.session["details_track"] = 0	
		return display(request)
		
	else:
		form = part_number()
	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render(request,'tb_edit_partnumber.html', args)
	
def select_date(request):
	
	try:
		request.session["s_date"]
	except:
		request.session["s_date"] = ""
	try:
		request.session["e_date"]
	except:
		request.session["e_date"] = ""		
	try:
		request.session["machine"]
	except:
		request.session["machine"] = ""				

		
	if request.POST:

		request.session["s_date"] = request.POST.get("start_date")
		request.session["e_date"] = request.POST.get("end_date")
		request.session["machine"] = request.POST.get("machine")

		return production_report(request)
		
	else:
		form = report_dateForm()
	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render(request,'report_form.html', args)	

def select_day(request):
	
	try:
		request.session["s_date"]
	except:
		request.session["s_date"] = ""
	try:
		request.session["e_date"]
	except:
		request.session["e_date"] = ""		
	try:
		request.session["machine"]
	except:
		request.session["machine"] = ""				

		
	if request.POST:

		request.session["s_date"] = request.POST.get("start_date")
		#request.session["e_date"] = request.POST.get("end_date")
		request.session["e_date"] = ""
		request.session["machine"] = request.POST.get("machine")

		return production_report_date(request)
		
	else:
		form = report_dateForm()
	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render(request,'report_form_date.html', args)		


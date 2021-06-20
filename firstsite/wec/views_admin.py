from django.shortcuts import render_to_response
from django.template import loader
from django.template import RequestContext
from django.shortcuts import render
from firstsite.wec.models import Members, Members_Features
from firstsite.wec.db import db_open
from django.http import HttpResponse
from firstsite.wec.forms import admin_addUsers, admin_addWebpage


from firstsite.wec.mod2 import create_directory, copy_directory, delete_directory, path_local, path_local2
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from smtplib import SMTP
import MySQLdb
import datetime

def update_database(request):
	page_set(request)
	return
	
def admin_debug(request):
	return render(request,'debug.html')
	
def pages(request):
	current_db = request.session["active_db"]
	db, cur = db_open()
	sql = "SELECT DISTINCT webpage FROM webpages_manager where DB = '%s'" %(current_db)
	cur.execute(sql)
	webpages = cur.fetchall()
	db.close()
	return webpages
		
def users(request):
	current_db = request.session["active_db"]
	db, cur = db_open()
	sql = "SELECT * FROM wec_members where DB = '%s'" %(current_db)
	cur.execute(sql)
	members_db = cur.fetchall()
	db.close()
	return members_db

# Method to display the users in the current db
def display_users(request):
	members_db = users(request)
	return render(request,'display_users.html',{'Members':members_db})

# Method to display the users in the current db
def display_webpages(request):
	webpages = pages(request)
	return render(request,'display_webpages.html',{'Webpages':webpages})
	
# Method to add the new user name to the required database    
def admin_users(request):   
	new_name = request.session["admin_new_user"]
	current_db = request.session["active_db"]
	tpe = "user"
	new_user = "---"
	new_pwd = "password"

	dt = datetime.datetime.now()
	db, cur = db_open()  
	cur.execute('''INSERT INTO wec_members(name, user, type, signup, DB, password) VALUES(%s, %s, %s, %s, %s, %s)''', (new_user, new_name, tpe, dt, current_db, new_pwd))
	db.commit()
	db.close()
	return 

# Method to produce form and add new user 
def admin_add_users(request):	
	if request.POST:
		
		# utilize the database request variable 'active_db' 
		tec = request.POST.get("user")       
		request.session["admin_new_user"] = tec
		admin_users(request)
		return display_users(request)
		
	else:
		form = admin_addUsers()
	args = {}
	args.update(csrf(request))
	args['form'] = form
	request.session["admin_new_user"] = "none"
	member_list = users(request)
	args['Members'] = member_list
	return render(request,'admin_add_users.html', args)	

# Method to produce form and add generate and initialize new webpage
def admin_add_webpage(request):	
	#request.session["testt"] = '<img src="/static/template_1.jpg"  height="160" width="300">'
	if request.POST:
		
		# utilize the database request variable 'active_db' 
		web = request.POST.get("web")       
		request.session["admin_new_webpage"] = web
		if request.POST.get("A"):
			request.session["admin_new_template"] = 'A'
		if request.POST.get("B"):
			request.session["admin_new_template"] = 'B'	
		
		check = request.session["admin_new_webpage"]
		if len(check)<3:
			return admin_add_webpage_error(request)
			
		# Below is the direction taken to confirm webpage name has not
		# been taken and then redirect to Template Choices
		# maybe call admin_webname(request) to check name
		
		
		#admin_webname(request)
		
		
		# Then redirect to another Method to choose Template
		
		
		page_initialize(request)
		request.session["error_message_1"] = 'none'
		return render(request,'dashboard_main.html')
		
	else:
		form = admin_addWebpage()
	args = {}
	args.update(csrf(request))
	args['form'] = form
	request.session["admin_switch"] = 0
	return render(request,'admin_add_webpage.html', args)	

def admin_delete_webpage(request,web):
	
	# Below to stop mid program and view variables
	#test1_v = 'Web Address : '
	#path1 = path_local()
	#test2_v = 'Full Path is :'
	#path1 = path_local() + 'wec_company/' + web
	#return render(request,'mid_stop_info_1.html',{'test1':web,'test1_v':test1_v,'test2':path1,'test2_v':test2_v})
	
	db, cursor = db_open()
	try:
		cursor.execute("DELETE FROM webpages_manager WHERE webpage = '%s'" % (web))
		db.commit()
	except:
		dum = 0	
	db.close()
	# Below we add delete code for directory and pictures.
	dpath = path_local2() + 'wec_company/' + web
	delete_directory(dpath)
	#                                                     
	#return render(request,'done.html')
	return display_webpages(request)
	
def admin_webname(request):
	request.session["admin_switch1"] = 1
	return 

	# Error in webpage setup.   Return to submission form
def admin_add_webpage_error(request):
	request.session["error_message_1"] = 'no name'
	return render(request,'admin_add_webpage_error.html')

def page_initialize(request):

	current_db = request.session["active_db"]
	template = request.session["admin_new_template"]
	web = request.session["admin_new_webpage"]
	request.session["active_website"] = web
	
	# delete old page if there is one of same name
	#page_delete(request)
	
	db, cursor = db_open()
	sql = "SELECT info,type,hook FROM WC_Templates where template = '%s'" %(template)
	cursor.execute(sql)
	tmp = cursor.fetchall()
	
	# Code Below to send template data to initialize table in webpages_manager
	for row in tmp:
		info = row[0]
		info_type = row[1]
		info_hook = row[2]
		cursor.execute('''INSERT INTO webpages_manager(db,webpage,template,info,type,hook) VALUES(%s,%s,%s,%s,%s,%s)''', (current_db,web,template,info,info_type,info_hook))
		db.commit()
		
	db.close()
	# Code below to send pictures from appropriate template directory to starting folder
	# 	web is incoming variable for webpage name
	#	template is incoming variable for template to use	
	
	#dpath = 'wec/wec_company/' + web
	dpath = path_local() + 'wec_company/' + web
	dpath2 = path_local2() + 'wec_company/' + web
	create_directory(dpath2)
	copy_directory(dpath,template)
	
	#return render(request, 'done.html')	
	return
# **********************************************************************************
def testlink(request):
	return render(request, 'web_templates/A/A_1.html')

def webpage_test_1(request):
	return render(request, 'page_test/index.html')


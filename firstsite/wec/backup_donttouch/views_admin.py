from django.shortcuts import render_to_response
from django.template import loader
from django.template import RequestContext
from django.shortcuts import render
from firstsite.wec.models import Members, Members_Features
from firstsite.wec.db import db_open
from django.http import HttpResponse
from firstsite.wec.forms import admin_addUsers
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from smtplib import SMTP
import MySQLdb
import datetime

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









from django.shortcuts import render_to_response
#from math import trunc
from django.template import loader
from django.template import RequestContext
from django.shortcuts import render
from firstsite.wec.models import Members, Members_Features
from django.http import HttpResponse
from firstsite.wec.forms import MembersForm, Members_Start_Form, Members_Login_Form, Members_Features_Form
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from smtplib import SMTP
from firstsite.wec.views_db import db_open

def kodi_live(request):
    return render(request,'kodi/dashboard_kodi_live.html')

def kodi_remote(request):
    return render(request,'kodi/dashboard_kodi_remote.html')	
	
def kodi_main(request):
    
	yp = get_client_ip(request)
	#ip = str(kp)
	db, cursor = db_open()
	cursor.execute('''INSERT INTO kodi(ip) VALUES(%s)''', (yp))
	db.commit()
	db.close()
	return render(request,'dashboard_main_kodi.html')	


def kodi_addons(request):
    return render(request,'kodi/dashboard_kodi_addons.html')	  

def kodi_install(request):
    return render(request,'kodi/dashboard_kodi_install.html')
    
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip    	  	


def create_koditable(request):
    db, cursor = db_open()
    cursor.execute('''DROP TABLE IF EXISTS kodi''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS kodi(Id INT PRIMARY KEY AUTO_INCREMENT,ip VARCHAR(30))''')
    db.commit()
    db.close
    return render(request, 'done.html')
	
def create_webtable(request):
    db, cur = db_open()
    cursor.execute('''DROP TABLE IF EXISTS webpages_manager''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS webpagesmanager(Id INT PRIMARY KEY AUTO_INCREMENT,db CHAR(30), webpage CHAR(30), template CHAR(30), link char(50), link_number INT(10))''')
    db.commit()
    db.close
    return render(request, 'done.html')	




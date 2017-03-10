from django.shortcuts import render_to_response
#from math import trunc
from django.template import loader
from django.template import RequestContext
from django.shortcuts import render
from firstsite.wec.models import Members, Members_Features
from django.http import HttpResponse
from firstsite.wec.forms import admin_addUsers
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from smtplib import SMTP
import MySQLdb

# Method for opening database for all and returning db and cur
def db_open():
    db = MySQLdb.connect(host="localhost",user="root",passwd="benny6868",db='wecloud')
    cur = db.cursor()
    return db, cur

def create_webtable(request):
    db, cur = db_open()
    cur.execute('''DROP TABLE IF EXISTS webpages_manager''')
    
    #cursor.execute("""CREATE TABLE IF NOT EXISTS tkb_prodtrak(Id INT PRIMARY KEY AUTO_INCREMENT,pi_id INT(10), machine CHAR(30), part_timestamp INT(20), qty INT(2), pcount INT(20), downtime INT(20), cycletime INT(10), status VARCHAR(25))""")

    cur.execute('''CREATE TABLE IF NOT EXISTS webpages_manager(Id INT PRIMARY KEY AUTO_INCREMENT,db CHAR(30), webpage CHAR(30), template CHAR(30), link char(50), link_number INT(10))''')
    db.commit()
    db.close
    return render(request, 'done.html')

def page_set(request):   
    
    current_db = "home"
    template = "A"
    link = "http://wecloud/ca/static/webimages/one.jpg"
    link_number = 1
    web = "stackpole"
  
    
    db, cur = db_open()  
    cur.execute('''INSERT INTO webpages_manager(db,webpage,template,link,link_number) VALUES(%s, %s, %s, %s, %s)''', (current_db,web,template,link,link_number))
    db.commit()
    db.close()
    return render(request, 'done.html')

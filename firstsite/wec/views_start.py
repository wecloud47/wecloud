from django.shortcuts import render_to_response
from django.template import loader
from django.template import RequestContext
from django.shortcuts import render
from firstsite.wec.db import db_open
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from smtplib import SMTP
import MySQLdb
import datetime

	
def start(request):

  db, cursor = db_open()
  cursor.execute("""DROP TABLE IF EXISTS pr_downtime1""")
  cursor.execute("""CREATE TABLE IF NOT EXISTS pr_downtime1(Id INT PRIMARY KEY AUTO_INCREMENT,mid INT(10), machinenum CHAR(30), problem CHAR(30), priority CHAR(30), whoisonit CHAR(30), called4helptime DATETIME DEFAULT NULL)""")
  db.commit()
  db.close()
  return render(request,'done.html')
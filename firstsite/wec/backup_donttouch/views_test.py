from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
import MySQLdb
import time





def create_table(request):
  # Construct tkb_prodtrak format
  # Select prodrptdbtest db 
  
  db = MySQLdb.connect(host="192.168.0.111",user="root",passwd="benny6868",db='wecloud')
  cursor = db.cursor()
  cursor.execute("""DROP TABLE IF EXISTS tkb_prodtrak""")
  cursor.execute("""CREATE TABLE IF NOT EXISTS tkb_prodtrak(Id INT PRIMARY KEY AUTO_INCREMENT,pi_id INT(10), machine CHAR(30), time INT(20), qty INT(2), pcount INT(20), downtime INT(20), cycletime INT(10), status VARCHAR(25))""")
  db.commit()
  t = int(time.time())
  m1 = '750'
  m2 = '749'
  m3 = '677'
  m4 = '748'
  tb = 101
  qty = 0
  perp = 0
  db.commit()
  sqA =( 'insert into tkb_prodtrak(pi_id,machine,time,qty,pcount) values("%d","%s","%d","%d","%d")' % (tb,m1,t,qty,perp) )
  sqB =( 'insert into tkb_prodtrak(pi_id,machine,time,qty,pcount) values("%d","%s","%d","%d","%d")' % (tb,m2,t,qty,perp) )
  sqC =( 'insert into tkb_prodtrak(pi_id,machine,time,qty,pcount) values("%d","%s","%d","%d","%d")' % (tb,m3,t,qty,perp) )
  sqD =( 'insert into tkb_prodtrak(pi_id,machine,time,qty,pcount) values("%d","%s","%d","%d","%d")' % (tb,m4,t,qty,perp) )
  cursor.execute(sqA)
  cursor.execute(sqB)
  cursor.execute(sqC)
  cursor.execute(sqD)
  db.commit()
  db.close()
  return render(request,'thankyou.html')

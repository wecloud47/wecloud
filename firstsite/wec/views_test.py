from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
import MySQLdb
import time
import struct
import imghdr

def modal_form(request):
    return render(request,'modal_form_test.html')
    
def ptest1(request):
    return render(request,'test1/test1.html')    



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

def poptest(request):
  return render(request,'test_pop.html')
  
def pop_link(request):
  return render(request)

def testing(request):
  return render(request,'testing.html')

def test2(request):
  return render(request,'test2.html')
  
def get_image_size(fname):
    '''Determine the image type of fhandle and return its size.
    from draco'''
    with open(fname, 'rb') as fhandle:
        head = fhandle.read(24)
        if len(head) != 24:
            return
        if imghdr.what(fname) == 'png':
            check = struct.unpack('>i', head[4:8])[0]
            if check != 0x0d0a1a0a:
                return
            width, height = struct.unpack('>ii', head[16:24])
        elif imghdr.what(fname) == 'gif':
            width, height = struct.unpack('<HH', head[6:10])
        elif imghdr.what(fname) == 'jpeg':
            try:
                fhandle.seek(0) # Read 0xff next
                size = 2
                ftype = 0
                while not 0xc0 <= ftype <= 0xcf:
                    fhandle.seek(size, 1)
                    byte = fhandle.read(1)
                    while ord(byte) == 0xff:
                        byte = fhandle.read(1)
                    ftype = ord(byte)
                    size = struct.unpack('>H', fhandle.read(2))[0] - 2
                # We are at a SOFn block
                fhandle.seek(1, 1)  # Skip `precision' byte.
                height, width = struct.unpack('>HH', fhandle.read(4))
            except Exception: #IGNORE:W0703
                return
        else:
            return
        return width, height  

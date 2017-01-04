from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from firstsite.wec.models import Members
from django.views.generic import ListView
from firstsite.wec.views_db import db_open
from firstsite.wec.views_test import get_image_size
from firstsite.wec.mod2 import create_directory, copy_directory, delete_directory
from firstsite.wec.views_admin import display_webpages
from firstsite.wec.forms import edit1_Form
from firstsite.wec.forms import ImageForm, entry
from firstsite.wec.mod2 import path_local
from django.template import RequestContext
from django.views.generic.edit import UpdateView
from django.core.context_processors import csrf
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from PIL import Image

import os, sys
import MySQLdb

# Module to filter tuple
def eup(x):
		global st, nt, mt, ut, lt, ht
		# template
		mt.append(str(x[3]))
		# info
		nt.append(str(x[4]))
		# webpage
		ut.append(str(x[2]))
		# id
		it.append(str(x[0]))
		# type
		lt.append(str(x[5]))
		# hook
		ht.append(str(x[6]))
		

# ***********************************************************************************
# Initializes WebPage Folder with Images from requested Template                    *
#                                                                                   *
# ***********************************************************************************
def web_template_initialize(request):

# 	webpage is incoming variable for webpage name
	webpage = 'premco'
#	from_Template is incoming variable for template to use	
	from_Template = 'A'
	
	dpath = 'wec/webpages/'+webpage
	create_directory(dpath)
	copy_directory(dpath,from_Template)
	
	return render(request, 'done.html')

# Module to run website request for viewing
def home_link(request,hook):
	# take in hook(hook_call) # from A_home.html and call up webpages_manager
	# and choose type where hook = hook_call , and webpage = request.session["addy"]
	# then 
	request.session["active_link"] = hook
	addy = request.session["addy"]
	return home(request,addy)
	#return render(request, 'web_templates/A/A_1.html')
	
def home_initial(request,addy):
	request.session["active_link"] = 0
	return home(request,addy)

		
def home(request,addy):
	try:
		request.session["active_link"]
	except:
		request.session["active_link"] = 0	
	tmp = addy
	active_link = int(request.session["active_link"])
	request.session["addy"] = addy
	#try:
	db, cursor = db_open()
	sql = "SELECT * FROM webpages_manager where webpage = '%s'" %(tmp)
	cursor.execute(sql)
	tmp = cursor.fetchall()
	tmp2 = tmp[0]
	global  mt, nt, ut, it, lt, ht
	nt = [] # info (description or label of link)
	mt = [] # template
	ut = [] # webpage
	it = [] # id
	lt = [] # variable for type (which could be a link or empty)
	ht = [] # variable for hook
	[eup(x) for x in tmp]
	
	# Calculate size of box based on line length
	tst = len(nt[7])   # length of that field for test
	lns = tst
	tst = (tst /float(100))+1
	# number of lines
	l = 200+(tst * 35)

	# if request.session["active_link"]  <--  use this to see if it's Null or not
	if active_link != 0:
		template = "web_templates/"+ max(mt) + "/"+ max(mt)+"_main_"+str(active_link)+".html"
	else:
		template = "web_templates/"+ max(mt) + "/"+ max(mt)+"_main.html"
	active_website = max(ut)
		# Assign each nt value (link_number) as array number to info
		# 
		
	request.session["active_website"] = active_website
		#template = "web.html"
		
	# Zip all variables together into list	
	list = zip(mt,nt,it,lt,ht)
	#except:
	#	return render(request, 'web_fail.html')
	
	
	request.session["web_addy"] = template
	
	return render(request, template, {'list':list, 'Tmp2':tmp2,'lines':l})

def web_link(request):
	request.session["active_link"] = 1
	addy = request.session["addy"]
	return home(request,addy)
	#return render(request, 'web_templates/A/A_1.html')
	
# ***********************************************************************************
# Select db filtered with information from the required website only and redirect to*
# the appropriate template.	                                                        *
#                                                                                   *
# ***********************************************************************************
def web(request,addy):
	tmp = addy
	
	request.session["addy"] = addy
	if request.session["active_type"] != 'Administrator':
		return home(request,addy)
	#try:
	db, cursor = db_open()
	sql = "SELECT * FROM webpages_manager where webpage = '%s'" %(tmp)
	cursor.execute(sql)
	tmp = cursor.fetchall()
	tmp2 = tmp[0]
	global  mt, nt, ut, it, lt, ht
	nt = []
	mt = []
	ut = []
	it = []
	lt = []
	ht = []
	[eup(x) for x in tmp]
	template = "web_templates/"+ max(mt) + "/"+ max(mt)+".html"
	active_website = max(ut)
		# Assign each nt value (link_number) as array number to info
		# 
		
	request.session["active_website"] = active_website
		#template = "web.html"
	list = zip(mt,nt,it,lt,ht)
	
	
	
	# use below to test link editing....TEMPORARY
	xt = []
	yt = []
	for ab in range(0,4):
		xt.append(nt[ab])
		yt.append(it[ab])
	list2 = zip(xt,yt)
	# ********************************************
	
	
		
	#except:
	#	return render(request, 'web_fail.html')
	
	
	request.session["web_addy"] = template
	
	#                                                                                                                          
	#                                                    TESTING                                                               
	# Set up Form for link renames and image changes
	if request.POST:
		# Determine if image or link rename
		# this one is for image upload
		ftype = request.POST.get("form_type") 
		if ftype == "image_change":
			request.session["change"] = 'logo'
			form = ImageForm(request.POST, request.FILES)
#			request.session["active_db"] = request.session["addy"]
#			db = request.session["active_db"]
			web_site = request.session["addy"]			
			im = Image.open(request.FILES['image'])
			width, height = im.size			
			save_file2(request,request.FILES['image'], web_site)
			request.session["width"] = width
			request.session["height"] = height
			
			ratio = width / float(height)
			multiplier = 40 * ratio
			request.session["width"] = multiplier
			return done_page_edit(request)
			#return render(request,'testhtml.html')
		elif ftype == "back_change":
			request.session["change"] = 'back'
			form = ImageForm(request.POST, request.FILES)
#			request.session["active_db"] = request.session["addy"]
#			db = request.session["active_db"]
			web_site = request.session["addy"]
			im = Image.open(request.FILES['image'])
			width, height = im.size			
			save_file2(request,request.FILES['image'], web_site)

			
			ratio = width / float(height)
			multiplier = 40 * ratio
			request.session["width"] = multiplier
			return done_page_edit(request)
			
		elif ftype == "page":
			tmp = request.POST
			edit1 = tmp.get("page_1_1")
			id1 = tmp.get("id1")
			request.session["link"] = edit1 
			request.session["id"] = id1
				
		else:	
			tmp = request.POST
			link1 = tmp.get("link1_name")
			link2 = tmp.get("link2_name")
			link3 = tmp.get("link3_name")
			link4 = tmp.get("link4_name")
			id1 = tmp.get("id1")
			id2 = tmp.get("id2")
			id3 = tmp.get("id3")
			id4 = tmp.get("id4")
			if id1 > 0:
				request.session["link"] = link1
				request.session["id"] = id1
			elif id2 > 0:
				request.session["link"] = link2
				request.session["id"] = id2
			elif id3 > 0:
				request.session["link"] = link3
				request.session["id"] = id3	
			else:
				request.session["link"] = link4
				request.session["id"] = id4		

		return done_page_edit(request)
		
	else:
		form = edit1_Form()
	args = {}
	args.update(csrf(request))
	args['form'] = form
#	return render(request,'done2.html', {'template':list2})
	return render(request, template, {'list':list,'list2':list2, 'Tmp2':tmp2,'args':args})
	# ***********************************************************************************************************************	
	
	
		# template is assigned template retrieved from DB.  list is links for pictures etc sent
		# .....uncomment below code for normal  ............
    	#return render(request, template,{'list':list,'Tmp2':tmp2})
		
def done_page_edit(request):
	# update webpages_manager where webpage = request.session.addy and lin1 name = request.session.link1
	# Use try because link and id rv may be empty if we are only updating a picture first
	try:
		ide = request.session["id"]
		link = request.session["link"]
		idx = int(ide)
		db, cur = db_open()
		mql =( 'update webpages_manager SET info = "%s" WHERE Id = "%s"' % (link,idx))
		cur.execute(mql)
		db.commit()
		db.close
	except:
		dumb = 1	
	return render(request,'done_page_edit.html')
		
		

# ***********************************************************************************
# Initializes webpages_manager for a new webpage.  Will put all Template info into  *
# the webpages_manager from the Template Table WC_Template                          *
# The Call is  page_initialize and it will request.session['active_website']        *
# ***********************************************************************************

	
# Update Link Name
def web_edit(request,addy):
	tmp = addy
	request.session["addy"] = addy
	#try:
	db, cursor = db_open()
	sql = "SELECT * FROM webpages_manager where webpage = '%s'" %(tmp)
	cursor.execute(sql)
	tmp = cursor.fetchall()
	tmp2 = tmp[0]
	global  mt, nt, ut, it
	nt = []
	mt = []
	ut = []
	it = []
	[eup(x) for x in tmp]
	template = "web_templates/"+ max(mt) + "/"+ max(mt)+"_edit.html"
	active_website = max(ut)
		# Assign each nt value (link_number) as array number to info
		# 
		
	request.session["active_website"] = active_website
		#template = "web.html"
	list = zip(mt,nt,it)
	#except:
	#	return render(request, 'web_fail.html')
	
	
	request.session["web_addy"] = template
	
	#                                                                                                                          
	#                                                    TESTING                                                               
	# Set up Form for link renames
	if request.POST:
		tmp = request.POST
		link1 = tmp.get("link1_name")
		link2 = tmp.get("link2_name")
		link3 = tmp.get("link3_name")
		id1 = tmp.get("id1")
		id2 = tmp.get("id2")
		id3 = tmp.get("id3")
		if id1 > 0:
			request.session["link"] = link1
			request.session["id"] = id1
		elif id2 > 0:
			request.session["link"] = link2
			request.session["id"] = id2
		else:
			request.session["link"] = link3
			request.session["id"] = id3 	

		return done_page_edit(request)
	else:
		form = edit1_Form()
	args = {}
	args.update(csrf(request))
	args['form'] = form
		
	return render(request, template, {'list':list, 'Tmp2':tmp2,'args':args})
	
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ UPDATE IMAGE @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def web_edit2(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid() and form.is_multipart():
            request.session["active_db"] = request.session["addy"]
            # Assign Database associated with entry to determine folder for images
            db = request.session["active_db"]
           
            save_file2(request.FILES['image'], db)
            request.session["refresh_1"] = 1
   
#            return render(request,'done_page_edit2.html')
            return web_page_reload(request)
        else:
#            return render(request,'done_page_edit2.html')
            return web_page_reload(request)
    else:
        form = ImageForm()
    args = {}
    args.update(csrf(request))
    args['form']=form
    
    return render(request,'up.html', args)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def web_page_reload(request):
	request.session["refresh_1"] = 0
	return render(request,'done_page_edit2.html')
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Delete Web Page@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def page_delete(request):
	#current_db = "stackpole"
	#template = "A"
	web = request.session["active_website"]
	#web = 'booboo'
	
	db, cursor = db_open()
	try:
		cursor.execute("DELETE FROM webpages_manager WHERE webpage = '%s'" % (web))
		db.commit()
	except:
		dum = 0	
	db.close()
	# Below we add delete code for directory and pictures.
	dpath = 'wec/wec_company/' + web
	delete_directory(dpath)
	
	return                                                    
	#return render(request,'done.html')
	#return display_webpages(request)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Save File for Image @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def save_file2(request,file, db):
    path = path_local() + 'wec_company'
    filename = file._get_name()
    # create directory to save images if one doesn't exist
    if not (os.path.exists('%s/%s' % (str(path), db))):
    	os.mkdir('%s/%s' % (str(path), db))
    # save image
    
    fd = open('%s/%s/%s' % (str(path), db, str(filename)), 'wb')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()
        
    # rename image to required name
    if request.session["change"] == 'logo':
		fn = "logoA.jpg"
    else:
		fn = "backA.jpg"	
	
    try:
		os.remove('%s/%s/%s'%(str(path),db,str(fn)))
    except:
		dummy_variable = 11		
	
	
    # write image to dirctory
    os.rename(('%s/%s/%s' % (str(path),db,str(filename))),('%s/%s/%s' % (str(path),db,str(fn))))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 



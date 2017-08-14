#******************************************************************************************************************
#***************  MODULE 3 CONTAINING db ALTERING MODS     ********************************************************
#******************************************************************************************************************

from django.shortcuts import render_to_response
from django.shortcuts import render
from firstsite.wec.views_db import db_open
def alter_database(request):
    page_set(request)
    return


    
# ***********************************************************************************
# Create a WebTable Quickly.    Just Modify Name and column                         *
# The Call is             create_webtable                                           *
# ***********************************************************************************
def repair_database(request):
    db, cursor = db_open()
    cursor.execute('''DROP TABLE IF EXISTS WC_Templates''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS WC_Templates(Id INT PRIMARY KEY AUTO_INCREMENT,template CHAR(10), info TEXT,type CHAR(20),hook INT(10))''')
    db.commit()
    cursor.execute('''DROP TABLE IF EXISTS webpages_manager''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS webpages_manager(Id INT PRIMARY KEY AUTO_INCREMENT, db CHAR(30), webpage CHAR(30),template CHAR(10), info TEXT,type CHAR(20),hook INT(10))''')
    db.commit()
    db.close
    template = ["" for x in range(2)] 
    template[0] = "A"
    template[1] = "B"
    for x in range(0,2):
		page_set(request,template[x])
    request.session["test"] = "Complete"		
    return render(request, 'done2.html')

# ***********************************************************************************
# Testing Module to add information to various Tables on call                       *
# The Call is            page_set                                                   *
# ***********************************************************************************
def page_set(request):
	# make above line page_set(request,template) if you're utilizing repair database.
	# repair database changes, deletes or adds columns if you want to expand WC_Templates
	
	# make above line page_set(request): if you want to change values or add rows to a certain 
	# template.   You must specify template in line with template = 'X'
	
	# Use below line to specify template being modified. Comment out if not using it
	
	
	# Currently Updates B Default Template
	template = 'B'
	
	db, cursor = db_open()
	cursor.execute("DELETE FROM WC_Templates WHERE template = '%s'" % (template))
	db.commit()
	link_number = 1
	rn = 21
	info = ["" for x in range(rn)]
	info[0] = "About"
	info[1] = "Blog"
	info[2] = "Contact"
	info[3] = "Link 4"
	info[4] = "Casual Business"
	info[5] = "1234 SOMEWHERE PL  |  ENGLEWOOD, CA 90132  |  123.456.7890"
	info[6] = "A CASUAL APPROACH TO BUSINESS"
	info[7] = "BUILD A WEBSITE"
	info[8] = "WORTH VISITING"
	info[9] = "The boxes used in this template are nested inbetween the attractive layout you've designed.  The boxes will be take up 80% of the page and the first box can have a nice photo of your choosing in it. This first box can give a breif summary of your business along with some detailed information about your business if you choose.   A picture is not necessary but adds eye candy to the page."
	info[10] = "You can add a second paragraph of description in this box and as you add information it will wrap around the picture.  Small limitations in editing only allow you to have two paragraphs in this box but you can however just have one long one if you choose.   Just edit this one and leave it blank."
	info[11] = "EXPAND ON YOUR WEBSITE"
	info[12] = "TO SHOWCASE YOUR BUSINESS"
	info[13] = "Use this box to further explain or summarize your business.  You can go into a little more detail or possible explain other features of your company.  It's a great tool to use as a secondary form of information."
	info[14] = "You can even add a second paragraph here as well.  It's amazing how much information you can fit into two small paragraphs that can greatly sell your business.  "
	info[15] = "This line can be used to give some Footer information such as Company and contact information."
	info[16] = "Link 2 Summary:  In this section you will write a detailed summary of what information you want to hold in this link.  It can be up to 256 characters."
	info[17] = "Link 3 Information"
	info[18] = "Link 3 Summary:  In this section you will write a detailed summary of what information you want to hold in this link.  It can be up to 256 characters."
	info[19] = "Link 4 Information"
	info[20] = "Link 4 Summary:  In this section you will write a detailed summary of what information you want to hold in this link.  It can be up to 256 characters."	
		
	
	info_note = ["" for x in range(rn)]
	info_note[0] = "_1.html"
	info_note[1] = "_2.html"
	info_note[2] = "_3.html"
	info_note[3] = "_4.html"
	info_note[4] = ""
	info_note[5] = ""
	info_note[6] = ""
	info_note[7] = ""
	info_note[8] = ""
	info_note[9] = ""
	info_note[10] = ""
	info_note[11] = ""
	info_note[12] = ""
	info_note[13] = ""
	info_note[14] = ""
	info_note[15] = ""
	info_note[16] = ""
	info_note[17] = ""
	info_note[18] = ""
	info_note[19] = ""
	info_note[20] = ""
	
	hook = ["" for x in range(rn)]
	for y in range(0,rn):
		hook[y] = (y+1)
		
	for x in range(0,rn):
		cursor.execute('''INSERT INTO WC_Templates(template,info,type,hook) VALUES(%s, %s, %s, %s)''', (template,info[x],info_note[x], hook[x]))
		db.commit()
	db.close()
	
	# Use below line if page_set is being used directly to alter one specific template
	return render(request, 'done2.html')
	
	# Use below line if page_set is being used indirectly to alter WC_Template structure
	#return
		
    


		

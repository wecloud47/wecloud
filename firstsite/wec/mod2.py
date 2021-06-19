#******************************************************************************************************************
#***************  MODULE 2 CONTAINING TESTING ALGORITHMS ********************************************************
#******************************************************************************************************************

from django.shortcuts import render_to_response
from django.shortcuts import render
from distutils.dir_util import copy_tree



import os
import errno
import shutil


def dir_test(request):
    mode = 0777
    path = r'firstsite/wec/static/wec/testrun2'
    os.makedirs(path)
    os.chmod(path,mode)
    x = 'Done'
    return render(request, 'done3.html', {'x':x})

# ***  Creates a directory npath and gives full permissions ****
def create_directory(dpath):
    mode = 0777
#    if dpath == 'firstsite/wec/static/wec/':
#	npath = r'firstsite/wec/static/wec/wec_company'
#    else:
#	npath = r'static/wec/'

    npath = dpath
    os.makedirs(npath)
    os.chmod(npath,mode)
    return 

def delete_directory(dpath):

    #npath = r'firstsite/' + dpath
    #npath = r+dpath

    npath = dpath
    try:
        shutil.rmtree(npath)
    except:
        dum = 1
    return
	
# *** Will copy files from one directory to another ***	
def copy_directory(to_Directory,from_Template):

	# **** Copies selected file to destination directory **
	#f='static/images/button_adduser.gif'
	#d='static/BRANDON_TEST'
	#shutil.copy(f,d)
	
	
	# ***  Copy entire directory to another *****
#	to_Directory = 'static/' + to_Directory
	path = path_local()

	from_Directory = path + "template_files/" + from_Template 
	copy_tree(from_Directory, to_Directory)

	return	

def path_local():

#	path_local = 'static/wec/'  # Uncomment for server

	path_local = 'firstsite/wec/static/wec/'   # Uncomment for local
	
	return path_local
	
def path_local2():
	
#	path_local = r'static/wec/'  # Uncomment for Server
	path_local = r'firstsite/wec/static/wec/'  # Uncomment for local
	return path_local
	
	
		

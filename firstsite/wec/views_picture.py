from django.shortcuts import render_to_response
from math import trunc
from django.template import loader
from django.template import RequestContext
from django.shortcuts import render
from firstsite.wec.models import Members
from django.http import HttpResponse
from firstsite.wec.forms import ImageForm, entry
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from smtplib import SMTP
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os, sys

# Use form and upload image/file
def image_upload(request):
    request.session["active_db"] = "test_pumpkin"
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid() and form.is_multipart():
            request.session["active_db"] = request.session["addy"]
            # Assign Database associated with entry to determine folder for images
            db = request.session["active_db"]
           
            save_file2(request.FILES['image'], db)
            return render(request,'done_page_edit2.html')
        else:
            return render(request,'done_page_edit2.html')
    else:
        form = ImageForm()
    args = {}
    args.update(csrf(request))
    args['form']=form
    
    return render(request,'up.html', args)

def save_file2(file, db, path='static/wec/wec_company'):
        
    filename = file._get_name()
    
    # create directory to save images if one doesn't exist
    if not (os.path.exists('%s/%s' % (str(path), db))):
        os.mkdir('%s/%s' % (str(path), db))
    # save image
    
    fd = open('%s/%s/%s' % (str(path), db, str(filename)), 'wb')
    
    # rename image to required name
    fn = "logoA.jpg"
    # write image to dirctory
    os.rename(('%s/%s/%s' % (str(path),db,str(filename))),('%s/%s/%s' % (str(path),db,str(fn))))
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()
    
def save_file(file, db, path='static'):
        
    filename = file._get_name()
    
    # create directory to save images if one doesn't exist
    if not (os.path.exists('%s/%s' % (str(path), db))):
        os.mkdir('%s/%s' % (str(path), db))
    # save image
    
    fd = open('%s/%s/%s' % (str(path), db, str(filename)), 'wb')
    
    # rename image to required name
    fn = "backA.gif"
    # write image to dirctory
    os.rename(('%s/%s/%s' % (str(path),db,str(filename))),('%s/%s/%s' % (str(path),db,str(fn))))
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()




from django.db import models
from django.forms import ModelForm
from django.core.urlresolvers import reverse
from django import forms
from datetime import datetime

#from mysite.myapp.views_picture import db_var

#import MySQLdb

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)

class main(models.Model):
    name = models.CharField("Employee",max_length=200)
    clock = models.CharField("Clock",max_length=10, default="0")
    tpe = models.CharField("tpe",default='',max_length=200, blank = True)
    db = models.CharField("db",default='',max_length=200, blank = True)
    entry = models.CharField("entry",default='',max_length=200, blank = True)

    def __unicode__(self):
        return self.name

class temp1(models.Model):
    name = models.CharField(max_length=200)
    clock = models.IntegerField(default=0)
    tpe = models.CharField(max_length=200)
    db = models.CharField(max_length=200)
    entry = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class membership(models.Model):
    db = models.CharField(max_length=200)
    app = models.CharField(max_length=200)
    app_date = models.DateField("")

    def __unicode__(self):
        return self.db


class Members(models.Model):
    name = models.CharField("Name", max_length=70)
    user = models.CharField("User Name",default='', max_length=30)
    type = models.CharField(default='admin',max_length=30)
    password = models.CharField("Password", default='', max_length=30)
    password_v = models.CharField("Password Again", default='', max_length=30)
    email = models.EmailField(max_length=70,blank=True)
    address = models.CharField("Address", default='', max_length=70)
    city = models.CharField("City", default='',max_length=70)
    country = models.CharField("Country", default='',max_length=70)
    code = models.CharField("Zip", default='',max_length=70)
    phone = models.CharField("Phone", default='',max_length=70)
    signup = models.DateField(default=datetime.now, editable=False)
    status = models.IntegerField(default=0)
    DB = models.CharField("Business",max_length=50)


    def __unicode__(self):
        return self.user

class Members_Features(models.Model):
    feature = models.CharField("Feature", max_length=70)
    feature_name = models.CharField("Feature Name",default='', max_length=50)
    DB = models.CharField("Business",max_length=50)

    def __unicode__(self):
        return self.user

class temp(models.Model):
    user = models.CharField("User Id",default='', max_length=30)
    password = models.CharField("Password", default='', max_length=30)
    DB = models.CharField("Business",max_length=50)

    def __unicode__(self):
        return self.user

def image_name(name, filename):
    #db_var = request.session["active_db"]
    #db=filename[:1]+" "+'pumpkin'
    #db = request.session["active_db"]
    h = name
    filename = 'ymuu.jpg'
    return 'web_pictures/image_{0}/{1}'.format(h, filename)

def content_file_name(instance, filename):
    return '/'.join(['content', instance, filename])



class Images(models.Model):
    pic = models.ImageField(upload_to='pic_folder/', null=True, blank=True)

    def __unicode__(self):
        return self.pic.name












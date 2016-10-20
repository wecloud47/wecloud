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

def send_email (message_subject, message_text, user, db, toaddrs):
    fromaddr = 'WeCloud.ca@gmail.com'
    frname = 'WeCloud'
    server = SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('wecloud.ca@gmail.com', 'tounces6868')
    message = "From: %s\r\n" % frname + "To: %s\r\n" % toaddrs + "Subject: %s\r\n" % message_subject + message_text + "\r\n"
    server.sendmail(fromaddr, toaddrs, message)
    server.quit()




def emailtest(request):
    x ='Registration for WeCloud'
    send_email('Signup',x)
    return HttpResponseRedirect('/members_db')


def upload(request):
    if request.POST:
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            return render(request,'thanks.html')
    else:
        form = ImageUploadForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request,'up.html',args)

def picture(request):
    d=ExampleModel.objects.all()
    return render_to_response('picture.html',{'dad':d})



# **** Register new Member ****
def register(request):
    if request.POST:
        form = MembersForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['name']
            db = form.cleaned_data['DB']
            email = form.cleaned_data['email']
            if Members.objects.filter(DB = db).filter(type = 'admin').count()<1:
                form.save()
                try:
                    mid = Members.objects.get(name = user, DB = db, email = email)
                except:
                    UID = '0'
                else:
                    UID = str(mid.id)
                request.session["active_name"] = user
                request.session["active_db"] = db
                request.session["active_email"] = email
                addy = 'www.wecloud.ca/registration/get/'+UID +"/"
                sb = 'WeCloud Welcomes you ' + user
                by = 'Welcome to WeCloud Registration '+user+ '.  Nice to have you aboard!  Please click on the link to create a user name and password. '+ addy
                send_email(sb, by, user, db, email)
                # Send information vial email to new register and welcome page
                msg="Welcome to WeCloud " + user+"!"
                msg2="Please follow the link in your email to continue."
            else:
                msg="Oops !  "
                msg2=" An administrator has already registered for that Company. Please contact us if you require any further assistance."

            return render(request,'dash.html', {'User':user, 'Db':db, 'Email':email, 'Msg':msg, 'Msg2':msg2})
    else:
        form = MembersForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request,'register.html', args)


#******************************************************************
#*** Verification and password enter on Registration **************
#*** For Admin Users of Database                     **************
#******************************************************************
def registration(request,db_id):
    members = Members.objects.get(pk=db_id)
    if members.user =="":
        if request.POST:
            form = Members_Start_Form(request.POST)
            if form.is_valid():
                pass1 = form.cleaned_data['password']
                pass2 = form.cleaned_data['password_v']
                members = Members.objects.get(pk=db_id)
                form = Members_Start_Form(request.POST, instance = members)
                if pass1 == pass2:
                    form.save()
                    request.session["active_name"] = members.name
                    request.session["active_db"] = members.DB
                    request.session["active_email"] = members.email
                    request.session["active_user"] = members.user
                    user = members.user
                    name = members.name
                    db = members.DB
                    return render(request,'dashboard_main.html', {'User':user, 'db':db, 'Name':name})
                else:
                    addy = '/registration/get/'+db_id
                    return HttpResponseRedirect(addy)
        else:
            form = Members_Start_Form()
        args = {}
        args.update(csrf(request))
        args['form'] = form
        return render(request,'registration.html', args)
    else:
        return render_to_response('registration_fail.html', db_id)

# **** Register new Member ****
def members_features(request):
    if request.POST:
        form = Members_Features_Form(request.POST)
        if form.is_valid():
            #user = form.cleaned_data['name']
            #db = form.cleaned_data['DB']
            #email = form.cleaned_data['email']
            #if Members.objects.filter(DB = db).filter(type = 'admin').count()<1:
            form.save()
            return render(request,'members.html')
    else:
        form = Members_Features_Form()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request,'mem_feat.html', args)

def members_features_list(db):
    a=''
    w=''
    if Members_Features.objects.filter(DB = db).filter(feature="webpage").count() > 0:
        w=Members_Features.objects.filter(DB = db).filter(feature="webpage")
    if Members_Features.objects.filter(DB = db).filter(feature="webapp").count() > 0:
        a=Members_Features.objects.filter(DB = db).filter(feature="webapp")

    return a, w

def members_db(request):
    d=Members.objects.all()
    #request.session["active_user"] = 'Monkey Time!'
    #.order_by
    #d=Members.objects.filter()[:1].get().order_by(id)
    return render_to_response('members.html',{'dad':d})

def membersdel(request, db_id=1):
    y=Members.objects.get(pk=db_id)
    y.delete()
    return HttpResponseRedirect('/members_db')

def thanks(request):
    request.session["fill"] = 0


    return render(request,'thanks.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')


def language(request, language='en-gb'):
    response = HttpResponse("setting language to %s" % language)
    response.set_cookie('lang', language)
    request.session['lang'] = language
    return response


# **** Log in ****
def login(request):
    if request.POST:
        form = Members_Login_Form(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            db = form.cleaned_data['DB']
            pwd = form.cleaned_data['password']
            #form.save()
            if Members.objects.filter(DB = db).filter(user = user).filter(password = pwd).count()<>1:
                return render(request,'/dashboard_fail.html')
            else:
                m = Members.objects.get(user = user, DB = db)
                if m.type == 'admin':
                    tp = "Administrator"
                else:
                    tp = 'User'
                if user == 'kodi':
                    request.session["active_type"] = "Guest"
                    request.session["active_user"] = user
                    request.session["active_admin"] = "Guest"
                    
                    
                    return render(request,'dashboard_main_kodi.html')
					
		else:	
		    request.session["active_type"] = tp
		    request.session["active_user"] = user
		    request.session["active_db"] = db
		    request.session["active_admin"] = "Administrator"
		    a, w = members_features_list(db)
                
		    return render(request,'dashboard_main.html',{'A':a, 'W':w})
    else:
        form = Members_Login_Form()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request,'login.html', args)

def ddx(request):
    return render(request, 'login.html')
def pc(request):
    return render(request, 'pc.html')
def mobile(request):
    return render(request, 'mobile.html')

def fade(request):
    return render(request, 'fade.html')

def ssize(request,wid,hei):
    wid = float(wid)
    h = float(hei)
    hei = float(hei)
    x = wid
    y = hei
    (n1 ,n2,n3)= 1680 * 1050,800*600, x*y
    w = round((x-800)/880,2)
    w= round(w*150+250,2)
    h = round((y-600)/450,2)
    h = round(h*75+125,2)
    sm = round((n3-n2)/(n1-n2),2)
    ym = round((y-600)/350,2)
    y1 = round(ym*60+90,2)
    y2 = round(ym*48+72,2)
    y3 = round(ym*92+138,2)
    wr = w + 80
    # m1=round((82*x*y)/(1680*1050),2)
    request.session["active_y"] = y
    request.session["active_y1"] = y1
    request.session["active_y2"] = y2
    request.session["active_y3"] = y3


    request.session["active_h2"] = y * .1905

    request.session["active_wr"] = wr
    f = round(sm*30+55,2)
    fh = round(sm*15+95,2)
    ft = round(sm*30+60,2)
    s1 = round(sm*50+95,2)

    if x==1280 and y==768:
        (f,fh,ft,s1)=(78,110,90,130)
    elif x==1280 and y==1024:
        (ft,s1)=(93,170)
    elif x==1152 and y==864:
        (f,ft,s1)=(75,87,135)
    elif x==1024 and y==768:
        (f,ft,s1)=(70,84,130)
    elif x==800 and y==600:
        (f,ft,s1)=(65,82,100)
    elif x==1024 and y==600:
        (ft,h,w)=(90,100,300)
    else:
        f = round(sm*30+55,2)

    request.session["active_f"] = f
    request.session["active_fh"] = fh
    request.session["active_ft"] = ft
    request.session["active_s1"] = s1
    request.session["active_h"] = h
    request.session["active_w"] = w
    # Set Banner dimension
    bw = 0.154761905 * wid
    bh = bw / 0.766666667
    bs = 0.389730769 * bw
    bl1 = wid * .1
    bl2 = bl1 + bw + bs
    bl3 = bl2 + bw + bs
    bl4 = bl3 + bw + bs
    hei1 = ((.3*hei))
    wid1 = ((.8*wid)*.20833)
    px2 = wid1 / 1.25
    hei = .75 * hei
    xcloud = wid * 0.1484375
    ycloud = xcloud * .75
    xtitle = wid * 0.2015625
    ytitle = xtitle * 0.2727272727272727
    x_pos_cloud = wid * 0.09765625
    x_pos_title = wid * 0.17578125
    request.session["active_x"] = wid
    request.session["active_y"]=y

    if wid < 850 and wid < hei:
        return render(request,'mmain.html')
    else:
        return render(request,'pmain.html')
        #return render(request,'pmain.html', {'X':wid, 'Y':hei,'YY':h, 'PX':wid1, 'PYY':hei1, 'Bw':bw,'Bh':bh,'Bl1':bl1,'Bl2':bl2,'Bl3':bl3,'Bl4':bl4,'PX2':px2,'Xcloud':xcloud,'Ycloud':ycloud,'Xtitle':xtitle,'Ytitle':ytitle,'X_pos_cloud':x_pos_cloud,'X_pos_title':x_pos_title})










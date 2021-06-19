from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from firstsite.wec.models import Members
from django.views.generic import ListView
from firstsite.wec.forms import MembersForm, MembershipForm
from django.template import RequestContext
from django.views.generic.edit import UpdateView
from django.core.context_processors import csrf
from smtplib import SMTP
from time import strftime
import time

def email_test8(request):
	b="\r\n"
	message_subject = 'Next One'
	message3 ="This is the body of the message"
	toaddrs=["dclark@stackpole.com"]
	fromaddr='wecloud47@gmail.com'
	frname='Dave'
	server=SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('wecloud47@gmail.com','Tounces0909')
	# server.login('StackpolePMDS@gmail.com','stacktest6060')
	message="From: %s\r\n" % frname + "To: %s\r\n" % ','.join(toaddrs)+"Subject: %s\r\n" % message_subject + "\r\n"
	message=message+"\r\n\r\n"+message3+"\r\n\r\n"+"\r\n\r\n"
	server.sendmail(fromaddr,toaddrs,message)
	server.quit()
	return render(request,"email_test8.html") 
	
def test3(request):
	return render(request, 'test3.html')
	  
def fill(request):
	#ctr = int(request.session["fill"])
	ctr = request.session["fill"]
	x = int(ctr)
	x=x+1
	ctr=str(x)
	request.session["fill"] = ctr
	v1=5
	v2=10
	v3=15
	v4=20
	

	return render(request,'fill.html',{'var1':v1,'var2':v2,'var3':v3,'var4':v4,'ctr':x})

#from django.http import HttpResponse
#import datetime

def registration(request):
	if request.POST:
		form = MembershipForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/matrix')
	else:
		form = MembershipForm()
	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render_to_response('create_main.html', args)

#import datetime

class ListMemberView(ListView):
	model = Members
	template_name = 'member_list.html'


class MembersUpdate(UpdateView):
	model = Members
	fields = ['user','password','signup','status','DB']
	template_name = 'Members_update_form.html'

	def get_object(self):
		return Members.objects.get(pk=self.request.GET.get('pk')) # or request.POST

# *************MAIN CDS PAGE************************
def main(request):
	return render(request, 'main.html')


# Blog Main Site
def blog(request):
	return render(request, 'blog.html')	
def blog_4(request):
	return render(request, 'blog_4.html')			
  #return render(request, 'main.html')

def layout(request):
	return render(request, 'layout.html')
def login_error(request):
	return render(request, 'login_error.html')

# *******  Main Dashboard for Member *******************
def dashboard(request):
	return render(request, 'dashboard.html')
def pmain(request):
	return render(request, 'pmain.html')
def test(request):
	return render(request, 'test.html')
def mmain(request):
	return render(request, 'mmain.html')
def graph(request):
	return render(request, 'graph.html')	
	
def done(request):
	tm = time.localtime()
	xm = time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", tm)
	request.session['test'] = xm
	return render(request, 'done2.html')	
	  

 #html='<html> {% extends '"dashboard.html" %} </html>'
 #It Worked
 #{% endblock %}"
# return render(request, 'testhtml.html',{'user':U, 'form':form})




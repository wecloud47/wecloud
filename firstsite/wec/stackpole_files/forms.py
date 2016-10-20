from django import forms


#from django.forms import form_for_model



class entry(forms.Form):
	Mach = forms.CharField()
	
class part_number(forms.Form):
	PartNumber = forms.CharField()
	
class tech_closeForm(forms.Form):
	comment = forms.CharField()	

class tech_passForm(forms.Form):
	comment = forms.CharField()	
	whos = forms.CharField()	
	
class tech_loginForm(forms.Form):
	user = forms.CharField()
	pwd = forms.CharField()		
	
class tech_searchForm(forms.Form):
	machine = forms.CharField()		
	
class report_dateForm(forms.Form):
	start_date = forms.CharField()
	end_date = forms.CharField()
	
class sup_downForm(forms.Form):
	machine = forms.CharField()	
	reason = forms.CharField()	
	priority = forms.CharField()	
	
class sup_dispForm(forms.Form):
	machine = forms.CharField()	
	reason = forms.CharField()	
	priority = forms.CharField()
	


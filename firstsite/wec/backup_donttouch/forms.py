from django import forms
from django.forms import ModelForm
from firstsite.wec.models import Members, main, membership, temp, Members_Features, Images


class Members_Start_Form(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_v = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Members
        fields=('user','password','password_v')

class Members_Login_Form(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Members
        fields=('user','DB','password')

class MembersForm(ModelForm):

    class Meta:
        model = Members
        fields=('name','email','DB')
        #widgets = {'name': forms.TextInput(attrs={'class': 'name_class'}),}

class Members_Features_Form(ModelForm):

    class Meta:
        model = Members_Features
        fields=('feature','feature_name','DB')

class Main_Add_Form(ModelForm):

    class Meta:
        model = main
        fields=('name','clock')

class MainForm(forms.ModelForm):

    class Meta:
        model = main
        fields = ('name', 'tpe', 'db','entry')

class MembershipForm(forms.ModelForm):

    class Meta:
        model = membership
        fields = ('db', 'app', 'app_date')

class tempForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = temp
        fields=('user','password')


class entry(forms.Form):
    pic = forms.CharField()

    
class ImageForm(forms.Form):
    image = forms.FileField()

class admin_addUsers(forms.Form):
	user = forms.CharField()
	pwd = forms.CharField()		
	



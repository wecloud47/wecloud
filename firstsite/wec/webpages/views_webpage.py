from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from firstsite.wec.models import Members
from django.views.generic import ListView
from firstsite.wec.forms import MembersForm, MembershipForm
from django.template import RequestContext
from django.views.generic.edit import UpdateView
from django.core.context_processors import csrf


def web_1(request):
    return render(request, 'web_templates/web_1.html')



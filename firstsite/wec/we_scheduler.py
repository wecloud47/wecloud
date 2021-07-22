from firstsite.wec.mods1 import matrix_set
from django.shortcuts import render_to_response
from math import trunc
from django.shortcuts import render
from firstsite.wec.models import main
from django.http import HttpResponse
from firstsite.wec.forms import MainForm, Main_Add_Form
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

# Action on Matrix Render
def matrix(request):
    ty = request.session["active_type"]
    user = request.session["active_user"]
    db = request.session["active_db"]
    job, emj, emp, res, a, b, d, mach = matrix_set(db)

    return render(request,'matrix.html',{'Jobs':job, 'Empl':emp, 'EmJo':emj, 'Result':res, 'YY':a, 'YX':b, 'NX':d, 'Db':db, 'User':user, 'Type':ty})

# Action for Matrix Click
def matrice(request, index):
    #request.session["active_index"] = str(index)
    db = request.session["active_db"]
    #i = int(ii)
    job, emj, emp, res, a, b, d, mach = matrix_set(db)
    index = int(index)-1
    jnum = len (job)
    n_start = (index/(jnum+2))
    n_start = trunc(n_start)*(jnum+2)
    j_start = (index % (jnum+2))-1
    nm_start = res[n_start]
    jn_start = mach[j_start]
    if res[index] == a:
     #   i = i + 1
        upd = main.objects.get(tpe='row', name = nm_start, entry = jn_start)
        upd.delete()
    else:
     #   i =i + 1
        upd = main(tpe = 'row', db = db, name = nm_start, entry = jn_start)
        upd.save()
    #request.session["active_ctr"] = str(i)
    return HttpResponseRedirect('/matrix')


def mainadd(request):
    if request.POST:
        form = MainForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/matrix')
    else:
        form = MainForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('create_main.html', args)


def maindel(request, db_id=1):
    y=main.objects.get(pk=db_id)
    y.delete()
    return HttpResponseRedirect('/db')

def db(request):
    d=main.objects.all()
    return render_to_response('db.html',{'dab':d})

# ********************************************************
# *** Example of saving multiple data based on a  ********
# *** certain filter                              ********
# ********************************************************
def imain(request):
    n='Dave'
    c=5555
    main.objects.filter(name=n).update(clock=c)
    return render(request,'/thanks.html')
# ********************************************************
# *** Process New Entry for Matrix                ********
# ********************************************************
def main_new(request):
    if request.POST:
        form = Main_Add_Form(request.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            form.save()
            db = request.session["active_db"]
            main.objects.filter(name=n).update(db=db, tpe='row')
            return HttpResponseRedirect('/matrix')
    else:
        form = Main_Add_Form()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    ty = request.session["active_type"]
    user = request.session["active_user"]
    db = request.session["active_db"]
    Jobs, emj, emp, res, a, b, d, mach = matrix_set(db)

    #return render_to_response('matrix_new.html', args, {'Jobs':job, 'Empl':emp, 'EmJo':emj, 'Result':res, 'YY':a, 'YX':b, 'NX':d, 'Db':db, 'User':user, 'Type':ty})
    return render_to_response('matrix_new.html', args)
    #return render_to_response('matrix_new.html', args)


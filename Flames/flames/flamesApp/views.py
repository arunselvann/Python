from django.shortcuts import render, HttpResponse, Http404
import datetime
from .flames import flames

def home(request):
    now = datetime.datetime.now()
    error = False
    if 'name1' in request.GET:
        if request.GET['name1'] and request.GET['name2']:
            if request.GET['name1'].isdigit() or request.GET['name2'].isdigit():
                error = True
                return render(request, 'HomePage.html', {'MyName': '', 'Now': now, 'error': error})
            elif request.GET['name1'] == request.GET['name2']:
                error = True
                return render(request, 'HomePage.html', {'MyName': '', 'Now': now, 'error': error})
            c = flames(request.GET['name1'], request.GET['name2'])
            return render(request, 'HomePage.html', {'MyName': str(c), 'Now': now, 'error': error})
        else:
            error = True
            return render(request, 'HomePage.html', {'MyName': '', 'Now': now, 'error': error})
    return render(request, 'HomePage.html', {'MyName': '', 'Now': now, 'error': error})




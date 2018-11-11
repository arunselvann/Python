from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .XMLParsing import parse
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import os


def upload(request):
    file = False
    if request.method == 'POST' and request.FILES['file']:
        file = True
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        out_file = parse(fs.path(filename))
        with open(out_file, 'rb') as fh:
            response = HttpResponse(fh)
            response["Content-disposition"] = "attachment; filename={}".format(os.path.basename(out_file))
            #return render(request, 'index.html', {'OUTPUT': response, 'file': file})
            return response
    return render(request, 'index.html', {'file': file})


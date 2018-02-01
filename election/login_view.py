
from django.http import *
from django.shortcuts import render

# def home(request):
    # return  HttpResponse(u'<h1>Merhaba Dünya</h1>')
def login(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        data= "%s %s" % (name,email)
        return render(request, 'index.html', {"name": name, "email": email})
    else:
        return render(request,'index.html')


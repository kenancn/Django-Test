
from django.http import *
from django.shortcuts import render

# def home(request):
    # return  HttpResponse(u'<h1>Merhaba Dünya</h1>')
def home(request):
    return  render(request,'index.html', locals())
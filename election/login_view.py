
from django.http import *
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login


def loginview(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            return render(request,'login_view.html',{'message':'Email veya Parolanız yanlış.'})


    else:
        return render(request,'login_view.html')


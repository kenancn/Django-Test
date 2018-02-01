
from django.http import *
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from election.profile.models import UserProfile
from election.models import Survey,Question

# def home(request):
    # return  HttpResponse(u'<h1>Merhaba Dünya</h1>')
def home(request):
        surves=Survey.objects.all();
        questiona=Question.objects.all();

        return render(request,'index.html',{'surveys':surves,'questions':questiona})

def signup(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            user =UserProfile.objects.filter(email=email)
            if user not in user:
                user=UserProfile(name=name,email=email,is_active=True)
                user.set_password(password)
                user.save()
                return render(request,'signup_view.html',{'message':'Kayıt Başarılı!'})
            else:
                return render(request,'login_view.html',{'message':'Giriş Yapınız.'})
        else:
            return render(request,'signup_view.html',{'message':'Parolalar Eşleşmedi!!'})
    else:
        return render(request,"signup_view.html",{'message':"Kayıt ekranına Hoşgeldiniz."})

    return render(request, 'signup_view.html')


def logoutview(request):
    logout(request)
    return redirect('/')
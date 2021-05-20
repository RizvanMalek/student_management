from django.contrib.auth import authenticate, logout
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import AdminModel
from .forms import AdminForm
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def login(request):
    return render(request,'login.html')

def home(request):
    if request.user.is_authenticated:
        user = request.user.username
        return render(request,'index.html',{"user":user})
    else:
        return redirect('/login')

def login_model(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        # user = User.objects.create_user(email='rizwan@gmail.com',username='rizwan@gmail',password='12345')
        # user.save()
        user = authenticate(username=email,password=password) 
        if user is not None:
            if user.is_active:
                auth_login(request,user)
            # request.session['email'] = email
            return redirect('/home')
        else:
            return redirect('/login')
    else:
        return HttpResponse('wrong redirect')

def logout_model(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/login')
    else:
        return redirect('/login')
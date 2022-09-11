from multiprocessing import context
from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def Login(request):
    form = LoginForm
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('about')
        else:
            messages.error(request,'No valid login or password')
    


    context = {
        'form':form
    }
    return render(request,'Authenticate/login.html',context)

def Logout(request):
    logout(request)
    return redirect('/')


def Registration(request):
    form = RegistrationForm
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request,'User already have')
            print('error')

    context = {
        'form':form
    }
    return render(request,'Authenticate/registration.html',context)
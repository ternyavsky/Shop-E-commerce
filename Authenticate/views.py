from multiprocessing import context
from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from django.urls import reverse_lazy


def Login(request):
    form = LoginForm
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('account',user.id)
        else:
            messages.error(request,'No valid login or password')
    


    context = {
        'form':form
    }
    return render(request,'registration/login.html',context)

def Logout(request):
    logout(request)
    return redirect('/')


class Passwordresetview(PasswordResetView):
    form_class = ResetPasswordForm
    template_name: str = 'registration/password_reset_form.html'


class Passwordchangeview(PasswordResetConfirmView):
    form_class = ConfirmPasswordForm
    template_name: str = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('lin')

def Registration(request):
    form = RegistrationForm
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lin')
        else:
            messages.error(request,'User already have')
            print('error')

    context = {
        'form':form
    }
    return render(request,'registration/register.html',context)
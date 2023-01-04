from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import SendForm
from .models import *
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def home(request):
    products = Product.objects.all()[:3]
    
    products_main = Product.objects.all()
    context = {
        'preview_objects':products,
        'products':products_main
    }
    return render(request,'Main/index.html',context)


def contact(request):
    if request.method == 'POST':

        subject = request.POST.get('subject')
        text = request.POST.get('message')
        email = request.user.email
        send_mail(subject,text,'ternyavsky2016@yandex.ru',['ternyavsky2016@yandex.ru'])
        return redirect('about')


    context = {}
    return render(request,'Main/contact.html',context)


def service(request):
    return render(request,'Main/services.html')

def cart(request):
    return render(request,'Main/cart.html')


def about(request):
    return render(request,'Main/about.html')

def product(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,'Main/product.html',context)

def single(request,id):
    feedb = Feedback()
    product = Product.objects.get(id=id)
    feedback = Feedback.objects.filter(feedback = id)

    context = {
        'product':product,
        'feedback':feedback
    }
    if request.method == 'POST':
        author = request.user
        text = request.POST.get('text')
        Feedback.objects.create(author = author,text=text,feedback=product) 
        return redirect('single',id)
    
    

    return render(request,'Main/single.html',context)
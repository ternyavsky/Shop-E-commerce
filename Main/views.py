from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    products = Product.objects.all()[:3]
    context = {
        'preview_objects':products
    }
    return render(request,'Main/index.html',context)


def contact(request):
    return render(request,'Main/contact.html')


def service(request):
    return render(request,'Main/services.html')


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
    
    

    return render(request,'Main/single.html',context)
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views.generic import CreateView, TemplateView
# Create your views here.

def home(request):
    products_3 = Product.objects.all()[:3]
    products = Product.objects.all()

    context = {
        'preview_objects':products_3,
        'products':products
       
    }
    return render(request,'Main/index.html',context)


def contact(request):
    return render(request,'Main/contact.html')


def service(request):
    return render(request,'Main/services.html')

class CartView(TemplateView):
    template_name: str = 'Main/cart.html'

def about(request):
    return render(request,'Main/about.html')

def product(request):
    test = Product()
    products = Product.objects.all()
    context = {
        'products':products,
        'test':test
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
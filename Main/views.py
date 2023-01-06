from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import SendForm
from .models import *
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

#Home view, products - products for carousel, products_main - preview products in main, lower carousel
def home(request):
    products = Product.objects.all()[:3]
    products_main = Product.objects.all()
    if request.user.is_authenticated:
        cart_objects = Cart.objects.filter(user_id=request.user)
        quantity_objects = len(cart_objects)
    
        context = {
        'preview_objects':products,
        'products':products_main,
        'quant':quantity_objects,
        }
    else:
        context = {
        'preview_objects':products,
        'products':products_main,
       
        }

    return render(request,'Main/index.html',context)


def account(request,id):
    user = User.objects.get(id=id)
    if request.user.is_authenticated:
        cart_objects = Cart.objects.filter(user_id=request.user)
        quantity_objects = len(cart_objects)
    
        context = {
        'quant':quantity_objects,
        'user':user
        }
    else:

        context = {
        'user':user
    }
    return render(request,'registration/account.html',context)


def cart(request):
    cart_objects = Cart.objects.filter(user_id=request.user)
    quantity_objects = len(cart_objects)
    total_price = 0
    for i in cart_objects:
        product = Product.objects.get(title=i.item)
        total_price += product.price


    


    context = {
        
        'total_price':total_price,
        'objects':cart_objects,
        'quant':quantity_objects}
    return render(request,'Main/cart.html',context)

def cart_add(request,product_id):
    user = request.user
    product = Product.objects.get(id=product_id)
    Cart.objects.create(user=user,item=product)

    return redirect('product')


def contact(request):
    if request.method == 'POST':

        subject = request.POST.get('subject')
        text = request.POST.get('message')
        email = request.user.email
        send_mail(subject,text,'ternyavsky2016@yandex.ru',['ternyavsky2016@yandex.ru'])
        return redirect('about')

    if request.user.is_authenticated:
        cart_objects = Cart.objects.filter(user_id=request.user)
        quantity_objects = len(cart_objects)
    
        context = {
        'quant':quantity_objects,
    
        }
    else:
        context = {}

    return render(request,'Main/contact.html',context)


def service(request):
    if request.user.is_authenticated:
        cart_objects = Cart.objects.filter(user_id=request.user)
        quantity_objects = len(cart_objects)
    
        context = {
        'quant':quantity_objects,
    
        }
    else:
        context = {}
    
    return render(request,'Main/services.html',context)



def about(request):
    if request.user.is_authenticated:
        cart_objects = Cart.objects.filter(user_id=request.user)
        quantity_objects = len(cart_objects)
    
        context = {
        'quant':quantity_objects,
    
        }
    else:
        context = {}
    return render(request,'Main/about.html',context)


#Product View, all products 
def product(request):
    
    products = Product.objects.all()
    if request.user.is_authenticated:
        cart_objects = Cart.objects.filter(user_id=request.user)
        quantity_objects = len(cart_objects)
    
        context = {
        'quant':quantity_objects,
         'products':products,
    
        }
    

    else:
        context = {
        'products':products,
    }
    return render(request,'Main/product.html',context)


#Unique product and his feedbacks in 
def single(request,id):
    product = Product.objects.get(id=id)
    feedback = Feedback.objects.filter(feedback = id)
    if request.user.is_authenticated:
        cart_objects = Cart.objects.filter(user_id=request.user)
        quantity_objects = len(cart_objects)
    
        context = {
        'quant':quantity_objects,
        'product':product,
        'feedback':feedback
    
        }
    else:

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
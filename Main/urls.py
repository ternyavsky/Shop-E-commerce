from django.urls import path
from . import views
from .models import Product



urlpatterns = [
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('products',views.product,name='product'),
    path('services',views.service,name='service'),
    path('single<int:id>/',views.single,name='single'),
    path('cart',views.cart,name='cart'),
    path('cart_add<int:product_id>',views.cart_add,name='cart_add'),
    path('account<int:id>/',views.account,name='account'),
    
]

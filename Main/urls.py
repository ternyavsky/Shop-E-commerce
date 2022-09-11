from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('products',views.product,name='product'),
    path('services',views.service,name='service'),
    
]

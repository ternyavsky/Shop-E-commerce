from django.urls import path
from . import views
from .views import CartView

urlpatterns = [
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('products',views.product,name='product'),
    path('services',views.service,name='service'),
    path('single<int:id>/',views.single,name='single'),
    path('cart/',CartView.as_view(),name='cart' )
    
]

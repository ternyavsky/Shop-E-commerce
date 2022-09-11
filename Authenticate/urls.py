from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.Login,name='login'),
    path('registration/',views.Registration,name='registration'),
    path('logout/',views.Logout,name='logout')
]

from django.urls import path, re_path, include
from . import views
from django.contrib.auth.views import PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView,PasswordChangeView,PasswordResetView, PasswordChangeDoneView

urlpatterns = [
    path('login/',views.Login,name='lin'),
    path('registration/',views.Registration,name='registration'),
    path('logout/',views.Logout,name='lout'),
    
]

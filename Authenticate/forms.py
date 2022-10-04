from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField, PasswordResetForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "autofocus": True,
        'class':'form-control',
        'type': "text",
        'id': "username",
        'placeholder':"Username",
        'name':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "autocomplete": "current-password",
        'class':'form-control',
        'type': "password",
        'id': "password",
        'placeholder':"Password",
        'name':'password'}),
    ) 


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(
        
        max_length=254,
        widget=forms.EmailInput(attrs={
            "autocomplete": "email",
            'class':'form-control',
            'id':'email',
            'placeholder':'Email',
            'name':'email',
            'type':'email'})
    )

class ConfirmPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
       
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
            'class':'form-control',
            'id':'password',
            'placeholder':'Password',
            'name':'password',
            'type':'password'})
       
    )
    new_password2 = forms.CharField(
      
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
        'class':'form-control',
            'id':'password',
            'placeholder':'Password again',
            'name':'password',
            'type':'password'}))
    
    


class RegistrationForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "autofocus": True,
        'class':'form-control',
        'type': "email",
        'id': "floatingInput",
        'placeholder':"Email",
        'name':'email'}))
    username = UsernameField(widget=forms.TextInput(attrs={
        "autofocus": True,
        'class':'form-control',
        'type': "text",
        'id': "floatingInput",
        'placeholder':"Username",
        'name':'username'}))
    firstname = forms.CharField(widget=forms.TextInput(attrs={
        "autofocus": True,
        'class':'form-control',
        'type': "text",
        'id': "fname",
        'placeholder':"Firstname",
        'name':'email'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={
        "autofocus": True,
        'class':'form-control',
        'type': "text",
        'id': "lname",
        'placeholder':"Lastname",
        'name':'username'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "autocomplete": "new-password",
        'class':'form-control',
        'type': "password",
        'id': "password",
        'placeholder':"Password",
        'name':'password1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "autocomplete": "new-password",
        'class':'form-control',
        'type': "password",
        'id': "password",
        'placeholder':"Password again",
        'name':'password2'
    }))


    def clean_password2(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 and password2 and password1 != password2:
            raise ValidationError(_("Passwords don't match"))
        return password2

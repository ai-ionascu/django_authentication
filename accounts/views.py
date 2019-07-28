from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm

# Create your views here.

def index(request):
    """return the index.html file"""
    return render(request,'index.html')
    
def logout(request):
    """log the user out"""
    auth.logout(request)
    messages.success(request,'You have been successfully logged out!')
    return redirect(reverse('index'))
    
def login(request):
    """return a user login page"""
    login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form' : login_form})

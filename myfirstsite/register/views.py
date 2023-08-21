from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':  
        form = UserCreationForm(request.POST)  
        if form.is_valid():  
            form.save()     
    else:
        form = UserCreationForm()
    
    return render(request,"register/register.html",{"form":form})

def user_logout(request):
    logout(request)
    return render(request, "registration/logout.html", {})
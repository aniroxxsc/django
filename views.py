# user created file
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

config = {
    'apiKey': "AIzaSyBY_xSEWqlVy4fMVuA2JoCmFYGSvQc01R8",
    'authDomain': "login-9fe7d.firebaseapp.com",
    'databaseURL': "https://login-9fe7d.firebaseio.com",
    'projectId': "login-9fe7d",
    'storageBucket': "login-9fe7d.appspot.com",
    'messagingSenderId': "884585872827",
    'appId': "1:884585872827:web:4b7fe4c84439dc49a1d89e",
    'measurementId': "G-P2CDKV2HTG"
}



def home(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


    
def registration(request):
    if request.method == 'POST':
        user=request.POST['registration_id']
        passw=request.POST['registration_password']
        if len(user)>5 and len(passw)>5 and User.objects.filter(username=user, password=passw).exists() is not True:
            userr=User.objects.create_user(username=user, password=passw)
            userr.save()
            return render(request, 'login.html')
        else:
            return render(request, 'registration.html')
    else:
        return render(request,'registration.html')
        
def after1(request):
    if request.method == 'POST':
        user_login=request.POST['login_id']
        passw_login=request.POST['password']
        user = authenticate(username=user_login , password= passw_login)
        if user is not None:
            return render(request,'after1.html')
        else:
            return render(request,'login.html')

    else:
        return render(request,'login.html')

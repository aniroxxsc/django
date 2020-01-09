# user created file
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    djlogin_id=request.GET.get('login_id')
    dj_login_password=request.GET.get('password')
#    for key in login:
#        if(key==djlogin_id):
#            if(dj_login_password==login[key]):
#                return HttpResponse("you are logged in")
#            else:
#                return render(request,'login.html')
#        else:
#            return render(request,'login.html')
    return render(request,'login.html')
def registration(request):
    dj_register_id= request.GET.get('registeration_id')
    dj_register_password= request.GET.get('registeration_password')
    if dj_register_id not in login:
        login.update({dj_register_password,dj_register_password})
        return render(request,'login.html')
    else:
        return render (request,'registeration.html')

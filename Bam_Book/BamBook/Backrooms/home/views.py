from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls.base import reverse
from django.contrib.auth import authenticate,login,logout
import json

def home(request):
    return render(request, 'home/index.html',)

def login(request):
    if not request.user.is_anonymous:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(User.objects.values_list("password",))

        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect('/')

        else:
            # No backend authenticated the credentials
            context= {'case':False}
            return render(request,'index.html',context)


    context= {'case':True}
    return render(request,'index_logined.html',context)

def logout_auth(request):
    logout(request)
    return redirect('/index')
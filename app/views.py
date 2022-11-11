from django.shortcuts import render
from django.http import HttpResponse
from .models import Input
from django.template import loader
from rest_framework.response import Response
from .serializers import InputSerializer
from django.contrib import messages
from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib import messages #import messages





# Create your views here.
# def register(request):
#     if request.method == "POST":
#         print(request.POST)
#         comp= InputSerializer(data=request.POST)
#         print(comp,"$$$$$$$$$$$$$$$$$4444")
#         if comp.is_valid():
#             print(comp,"!!!!!!!!!!!!!!!1111")
#             comp.save()
#             print(comp,"?????????????/")
#             return render(request,'register.html')
#         else:
#             print(comp.errors,"error is")
#             return render(request,'register.html',{"e":comp.errors})    
#     return render(request,'register.html')


def RegisterPage(request):
    if request.method == "POST":
        full_name = request.POST['full-name']
        middle_name = request.POST['middle-name']
        last_name = request.POST['last-name']
        mob_no = request.POST['mob_no']
        email = request.POST['email']
        user_name = request.POST['user-name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            try:
                register_data = Input(
                                    first_name=full_name,
                                    middle_name=middle_name,
                                    last_name=last_name,
                                    mob_no=mob_no,
                                    user_name=user_name,
                                    password=password1,
                                    confirm_password=password2,
                                    email =email,
                                    )
                register_data.save()
                messages.success(request,f"Create Account")
            except Exception as e:
                messages.error(request,f"{e}")
        else:
            messages.error(request,f"Password Does Not Match")
    return render(request,'register.html')
    

def home(request):
    data = Input.objects.all()
    print(Input.objects.all(),"???????")
    return render (request , "home.html")

    




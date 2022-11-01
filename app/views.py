from django.shortcuts import render
from django.http import HttpResponse
from .models import Input
from django.template import loader
from rest_framework.response import Response
from .serializers import InputSerializer
from django.contrib import messages
from rest_framework import serializers
from django.core.exceptions import ValidationError





# Create your views here.
def register(request):
    comp= InputSerializer(data=request.POST)
    if request.POST.get('confirm_password') != request.POST.get('password'):
        raise serializers.ValidationError("Password does not match")
    else:
        if comp.is_valid():
            comp.save() 
    return render(request,'register.html')
          



def home(request):
    data = Input.objects.all()
    # template = loader.get_template('register.html')
    # context={
    #     'myinput':data,
    #     }
    # return HttpResponse(template.render(context,request))        

    print(Input.objects.all(),"???????")
    return render (request , "home.html")

    




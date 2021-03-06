from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from orderndmisc.models import Temporder
import re
from .models import Customer

# Create your views here.

def login(request):
    if request.method == 'POST':
        username= request.POST['name']
        password = request.POST['password']

        user = auth.authenticate( username=username, password= password)

        if user is not None:
            auth.login(request,user)
            messages.success(request, 'You are successfully logged in')
            return redirect('index')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'customer/login.html')

def register(request):
    if request.method =='POST':
        userName= request.POST['name']
        password= request.POST['password']
        password2= request.POST['password2']
        email = request.POST['email']
        phno = request.POST['phno']
        adl1 =request.POST['adl1']
        adl2 = request.POST['adl2']
        locality =request.POST['locality']
        city = request.POST['city']
        zipcode = request.POST['zcode']

        if(password == password2):
            if len(userName)>0 or len(password)>0 or len(email)>0 or str(phno) == '' or len(adl1)>0 or len(locality)>0 or len(city)>0 or str(zipcode) == '':
                                    messages.error(request,'All the fields are essential')
                                    return redirect('register')
            else:
                if User.objects.filter(username=userName).exists():
                    messages.error(request, 'That username is already taken')
                    return redirect('register')
                else:
                    if User.objects.filter(email =email).exists():
                        messages.error(request,'That email is already exists')
                        return redirect('register')
                    else:                  
                        if (Customer.objects.filter(phno =phno).exists()) or len(str(phno)) >10:
                            messages.error(request,'The phone number already exists or is a invalid one')
                            return redirect('register')
                        else:
                            if not re.search(r'[\w.-]+@[\w.-]+.\w+', email):
                                messages.error(request,'The email is invalid')
                                return redirect('register')
                            else:
                                if not len(str(zipcode)) == 6:
                                    messages.error(request,'The zipcode is invalid')
                                    return redirect('register')
                                else:
                                    user= User.objects.create_user(username=userName, email=email, password=password)            
                                    user.save()
                                    cust = Customer(user=user,userName=userName , phno= phno, adl1= adl1, adl2=adl2, locality= locality, city=city, zipcode= zipcode)
                                    print(cust)
                                    cust.save()       
                                    messages.success(request,'The Customer is successfully registered')
                                    return render(request,'customer/login.html')
        else:
            messages.error(request,'Passwords do not match')
            return render(request,'customer/register.html')
    else:
        return render(request,'customer/register.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        Temporder.objects.all().delete()
        messages.success(request,'You are successfully logged out')
        return redirect('index')

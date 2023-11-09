from django.shortcuts import render,redirect
from .models import team,book
from  django.contrib import messages,auth
from django.contrib.auth.models import User
from django.db import connection
from django.db.models import Q
# Create your views here.
def home(request):
    
    return render(request,'home.html')
def group(request):
    obj = team.objects.all()
    
    
    return render(request,'team.html',{'obj':obj})


def booking(request):
    team1 = ['TEAM 1','kerala blasters','jamashadpur','Hydrabadh FC','FC goa','East bengal','Chennai FC','Odisha','Panjab','North east']
    team2 = ['TEAM 2','kerala blasters','jamashadpur','Hydrabadh FC','FC goa','East bengal','Chennai FC','Odisha','Panjab','North east' ]
    if request.method =='POST':
        if request.user.is_authenticated == False:
            messages.info(request,'must login for booking ticket')
            return redirect('login') 
        else:
            if request.POST['fn'] != "" :
                fn = request.POST['fn']
            else:
                messages.info(request,' First name must be entered')
                return   redirect('booking')      

            sn = request.POST['sn']
            phone = request.POST['phone']
            if phone < str(11) :
                messages.info(request,'Number must be ten digits')
                return   redirect('booking') 
            
            if request.POST['s1'] !='TEAM 1':
                s1 = request.POST['s1']
            else:
                messages.info(request,'ENTER your team name')
                return   redirect('booking') 
                
            if request.POST['s2'] !='TEAM 2' and  request.POST['s1'] != request.POST['s2']:  
                s2 = request.POST['s2']
            else:
                messages.info(request,'Your error must be that you should enter team2 or team1 might equls to team2 ')
                return   redirect('booking')
            if request.POST['date'] !='':
                date = request.POST['date']
            else:
                messages.info(request,'please give your match date')
                return   redirect('booking')      
        
        
            obj = book(F_name=fn,S_name=sn,phone=phone,team1=s1,team2=s2,date=date)
            obj.save()
            messages.info(request,f"your ticket as booked at {date}")
    return render(request,'booking.html',{'team1':team1,'team2':team2})

def login(request):
    
    if request.method == 'POST':
       username =request.POST['username']
       password =request.POST['password']
       user = auth.authenticate(username=username,password=password) # it check the user  with the given user name and pasword is exist
       
       if user is not None:
           auth.login(request, user)
           return redirect('home')
       else:
           
           messages.info(request,' invalid user ')       
           return redirect('login')
    if request.user.is_authenticated:
        return redirect('home')   
    
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('login')
def register(request):
    if request.method == 'POST':
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        username =request.POST['username']
        email =request.POST['email']
        password1 =request.POST['password1']
        password2 =request.POST['password2']
        if password1 == password2:
            if username =='':
                messages.info(request,'username not entered')
                return redirect('register')
            elif first_name=='':
                messages.info(request,'firstname not entered')
                return redirect('register')
            elif User.objects.filter(username=username).exists() :
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Try a different email')
                return redirect('register')
            elif password1 == '' or password2 =='' :
                messages.info(request,"Password  must be enter it can't be empty")
                return redirect('register')
            else:    
                user = User.objects.create_user(first_name=first_name,last_name=last_name,password=password1,email=email,username=username)
                user.save() # first we  creat the user and save it
                auth.login(request, user) # login to the user so seecion and cookies are creat automaticaly
        else:
            messages.info(request,'Both password must be correct')
            return redirect('register')    
        return redirect('home')
    else:
        return render(request,'register.html')
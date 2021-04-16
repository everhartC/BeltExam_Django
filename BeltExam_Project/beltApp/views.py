from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    request.session.flush()
    return render(request, 'index.html')

def register(request): 
    if request.method == "POST": 
        errors = User.objects.Registration_Validator(request.POST) 
        if len(errors) != 0: 
            for key, value in errors.items(): 
                messages.error(request, value) 
            return redirect('/') 
        else: 
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode() 
            new_user = User.objects.create(name=request.POST['name'], alias=request.POST['alias'], email = request.POST['email'], password = hashed_pw) 
            request.session['user_id'] = new_user.id
            # UNCOMMENT BELOW and CHANGE FOR EXAM
            #return redirect('/books') 
    return redirect('/')

def login(request): 
    if request.method == "POST": 
        errors = User.objects.Login_Validator(request.POST) 
    if len(errors) > 0: 
        for key, value in errors.items(): 
            messages.error(request, value) 
    return redirect('/') 
    this_user = User.objects.filter(email = request.POST['email']) 
    request.session['user_id'] = this_user[0].id 
    # UNCOMMENT BELOW and CHANGE FOR EXAM
    #return redirect('/books') 
    return redirect('/')

def logout(request): 
    request.session.flush() 
    return redirect('/')
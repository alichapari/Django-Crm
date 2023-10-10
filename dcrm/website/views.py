from django.shortcuts import render
from django.contrib.auth import authenticate , login , logout
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == "POST":
        username= request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request , username=username , password = password)
        
        if user is not None:
            login(request , user)
            messages.success(request , 'you have been logged in ')
            return redirect("home")
        else:
    
            messages.success(request ," you cant get in")
            return redirect('home')
            
    else:
        return render(request , 'home.html' , {})




def logout_user(request):
    logout(request)
    messages.success(request ,"you have logout")
    return redirect('home')

def register_user(request):
    
    
    return render(request , "register.html" ,{})

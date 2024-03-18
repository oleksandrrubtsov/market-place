from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from .forms import  SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required





# Create your views here.
def  index(request):
    return render(request, 'core/index.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid(): 
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request,username=username,password=password)     
            if user is not None:
                login(request,user)
                messages.success(request,f"You logged in as {username} ")
                return redirect('index')
            else:
                messages.error(request,"Invalid username or password")
                return redirect('login')           
        else:
            messages.error(request,f"Some problem encountered")
            return redirect('login')        
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html',context={"form":form})

    
def logout(request):
        logout(request)
        messages.success(request,f"You have logged out ")
        return  redirect('login') 

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login') 
    else:
        form=UserCreationForm()
        context = {'form': form}
    return render (request,"registration/register.html",context)















    



 


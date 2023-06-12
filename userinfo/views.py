from django.shortcuts import render,redirect
from userinfo.forms import UserRegister,UserChange
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

# Create your views here.


def home(request):
    return render(request,"home.html")


def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserRegister(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Registration successfull")
                print(form.cleaned_data)
        else : 
            form = UserRegister()
        res = {
            "form":form
        }
        return render(request,"signup.html",res)
    else : 
        return redirect("profile")
    


def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect("profile")
        else:
            form = AuthenticationForm()
        res={
            "form":form
        }
        return render(request,"login.html",res)
    else :
        return redirect("profile")




def profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form = UserChange(request.POST,instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request,"profile updated successfully")
            
        else : 
            form = UserChange(instance=request.user)
        res={
            "form":form
            }
        return render(request,"profile.html",res)
    else: 
        return redirect("login")
    



def userlogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("login")
        
    
    
        
        
def changepass(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            form = PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request,"your password has changed successfully")
                return redirect("profile")
        else :
            form = PasswordChangeForm(user=request.user)
        res={
            "form":form
            }
        return render(request,"changepass.html",res)
    else:
        return redirect("signup")
        
    
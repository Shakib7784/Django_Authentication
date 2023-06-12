from django.contrib import admin
from django.urls import path,include
from userinfo import views

urlpatterns = [
    path("",views.home,name = "home"),
    path("signup",views.signup,name="signup"),
    path("login",views.userlogin,name="login"),
    path("profile",views.profile,name="profile"),
    path("logout",views.userlogout,name="logout"),
    path("changepass",views.changepass,name="changepass"),
]
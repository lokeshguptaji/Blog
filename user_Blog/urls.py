from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.blogPage,name='blogPage'),
    path('home', views.home,name='home'),
    path('signup',views.handleSignUp,name='signup'),
    path('login',views.handleLogin,name='handleLogin'),
    path('<str:slug>/',views.blogPost,name='blogPost'),
    path('logout',views.handleLogout,name='handleLogout'),
    path('addPost',views.addPost,name='addPost'),
]

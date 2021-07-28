from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('review', views.review, name='review'),
    path('userlogin', views.userlogin, name='userlogin'),
    path('signup', views.signup, name='signup'),
    path('booktrip', views.booktrip, name='booktrip')

   

]
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from home.models import Contact, Review
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def review(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        rate = request.POST.get('rate')
        satisfied = request.POST.get('satisfied')
        prices = request.POST.get('prices')
        support = request.POST.get('support')
        post = Review(name=name, email=email, msg=msg, rate=rate, satisfied=satisfied, prices=prices, support=support)
        post.save()
    return render(request, 'review.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        post = Contact(name=name, email=email, subject=subject, message=message)
        post.save()
        send_mail(
                    subject,
                    message,
                    email,
                    ['jaspatel690@gmail.com'],
                    fail_silently=False,
                    )
        

    return render(request, 'contact.html')

def dashboard(request):
    if request.user.is_anonymous:
        return render(request, 'adminlogin.html')
    else:
        return render(request, 'dashboard.html')

def adminlogin(request):

    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
       
        else: 
            return redirect('/adminlogin')
    return render(request, 'adminlogin.html')

       
def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/booktrip')
       
        else: 
            return redirect('/userlogin')
    
    return render(request, 'userlogin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            user = User.objects.create_user(username=username, password=password1)
            user.save()
            return redirect('/userlogin')
        else:
            return render(request, 'signup.html')
            
    else:
        return render(request, 'signup.html')

def booktrip(request):
    if request.user.is_anonymous:
        return render(request, 'userlogin.html')
    else:
        return render(request, 'booktrip.html')
    
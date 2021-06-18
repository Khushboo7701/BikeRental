from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Account
from django.contrib.auth.models import User, auth


def register(request):

    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_no = request.POST['phone_no']
        password = request.POST['password']
        re_password = request.POST['re_password']

        if password == re_password:
            if Account.objects.filter(email=email).exists():
                messages.info(request,"Email already registered")
                return redirect('register')
            else:
                user = Account.objects.create_user(email=email, password=password, phone_no=phone_no,first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')

    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:       
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')



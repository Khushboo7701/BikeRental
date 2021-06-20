from BikeRenting.settings import EMAIL_HOST_USER
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Account, Profile
from django.contrib.auth.models import User, auth
from email.mime import text
from django.http import request
from django.contrib import messages

from django.contrib.auth import get_user_model
# from django_email_verification import sendConfirm
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
import uuid


def register(request):

    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_no = request.POST['phone_no']
        password = request.POST['password']
        re_password = request.POST['re_password']

        if password == re_password:
            try:
                if Account.objects.filter(email=email).exists():
                    messages.info(request,"Email already registered")
                    return redirect('/accounts/register')
                else:
                    user1 = Account.objects.create_user(email=email, password=password, phone_no=phone_no,first_name=first_name, last_name=last_name)
                    user1.save()
                    auth_token1 = str(uuid.uuid4())
                    profile = Profile.objects.create(user = user1, auth_token = auth_token1 )
                    profile.save()
                    send_mail_after_reg(email, auth_token1)
                    return redirect('/accounts/token_send')

            except Exception as e:
                print(e)

        else:
            messages.info(request, 'Password not matching')
            return redirect('/accounts/register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user1 = auth.authenticate(email=email, password=password)

        if user1 is not None:
            profile = Profile.objects.filter(user=user1).first()
            if profile:
                if not profile.is_verified:
                    messages.info(request,'Kindly check your email to verify your account')
                    auth_token1 = str(uuid.uuid4())
                    send_mail_after_reg(email, auth_token1)
                    return redirect('/accounts/login')
                auth.login(request, user1)
                return redirect('/')
            else:
                messages.info(request, 'Profile not found')
                return redirect('/accounts/login')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('/accounts/login')
    else:       
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def token_send(request):
    return render(request,'token_send.html')


def success(request):
    return render(request,'success.html')

def send_mail_after_reg(email, token):
    subject = 'Verify your RentIt account'
    message = f'Please click the link to verify your account https://127.0.0.1:8000/accounts/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    mail1 = EmailMessage(subject, message, email_from, recipient_list)
    print(email_from)
    mail1.send(fail_silently=False)


def verify(request,token):
    profile_obj = Profile.objects.filter(auth_token = token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.info('Your account has been verified.')
            return redirect('/accounts/login')
        
        profile_obj.is_verified = True
        fname = profile_obj.user.first_name
        profile_obj.save()
        messages.info(request,'Your account has been successfully verified')
        text = f'Hey {fname}! Your account has been successfully verified!'

        email2 = EmailMessage(
            "Verification Succesful",
            text,
            settings.EMAIL_HOST_USER,
            [profile_obj.user.email],
        )
        email2.send(fail_silently=False)
        return redirect('/accounts/login')
    else:
        messages.info(request, 'Verification successful')
        return redirect('/accounts/register')
  
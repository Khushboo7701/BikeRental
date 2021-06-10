from django.shortcuts import render, redirect
from .models import Bike, Rent
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')


def bikes(request):
    bks = Bike.objects.all()
    return render(request, 'bikes.html', {'bks':bks})


@login_required(login_url='/accounts/login/')
def book(request, b_id):
    if request.method == 'POST':
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        location = request.POST.get('location')
        total = request.POST.get('amount')
        hours= request.POST.get('hours')
        bike=Bike.objects.get(id=b_id)
        uname = request.user
        rented = Rent.objects.create(uname = uname, location=location, starttime=start_time, endtime=end_time, hours=hours, amount=total, bike=bike)
        rented.save()
        return redirect('confirm',rented.id)
    
    
    else:
        obj= Bike.objects.get(id=b_id)
        context = {
            'obj': obj
        }
        return render(request, 'book2.html', context)


@login_required(login_url='/accounts/login/')
def confirm(request, b_id):
    queryset= Rent.objects.get(id = b_id)
    context = {
            "rent_list":queryset
        }
    return render(request, 'confirm.html', context)


@login_required(login_url='/accounts/login/')
def history(request):
    queryset = Rent.objects.filter(uname = request.user)
    context = {
        "rent_list": queryset
    }
    return render(request, 'history.html', context)
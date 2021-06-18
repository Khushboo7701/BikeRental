from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Bike, Rent
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def home(request):
    return render(request, 'home.html')


def bikes(request):
    bks = Bike.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(bks, 9)
    try:
        pageno = paginator.page(page)
    except Exception:
        pageno = paginator.page(paginator.num_pages)
    except:
        pageno = paginator.page(1)
    return render(request, 'bikes.html', {'bks': pageno})


@login_required(login_url='/accounts/login/')
def book(request, slug_text):
    if request.method == 'POST':
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        location = request.POST.get('location')
        total = request.POST.get('amount')
        hours = request.POST.get('hours')
        bike = Bike.objects.filter(slug=slug_text)
        if bike.exists():
            bike = bike.first()
        else:
            return HttpResponse("<h1>Page not found</h1>")
        uname = request.user
        rented = Rent.objects.create(uname=uname, location=location, starttime=start_time,
                                     endtime=end_time, hours=hours, amount=total, bike=bike)
        rented.save()
        return redirect('confirm', rented.slug)

    else:
        obj = Bike.objects.filter(slug=slug_text)
        if obj.exists():
            obj = obj.first()
            context = {
                'obj': obj
            }
            return render(request, 'book.html', context)
        else:
            return HttpResponse("<h1>Page not found</h1>")


@login_required(login_url='/accounts/login/')
def confirm(request, slug_text):
    obj = Rent.objects.filter(slug=slug_text)
    if obj.exists():
        obj = obj.first()
        context = {
            "rent_list": obj
        }
        return render(request, 'confirm.html', context)
    else:
        return HttpResponse("<h1>Page not found</h1>")


@login_required(login_url='/accounts/login/')
def history(request):
    queryset = Rent.objects.filter(uname=request.user).order_by("-id")
    context = {
        "rent_list": queryset
    }
    return render(request, 'history.html', context)


@login_required(login_url='/accounts/login/')
def search(request):
    bike_name = request.GET.get('search')
    bikes = Bike.objects.all().filter(name__icontains=bike_name)
    if bikes.exists():
        context = {
            "bikes": bikes
        }
    else:
        context = {
            "bikes": None
        }
        messages.info(request, 'Bike Not Found')
    return render(request, 'search.html', context)

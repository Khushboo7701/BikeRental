from django.contrib import admin
from .models import Bike, Rent

class BikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price','slug')


class RentAdmin(admin.ModelAdmin):
    list_display = ['bike','uname', 'location','starttime','endtime', 'hours', 'amount']

admin.site.register(Bike, BikeAdmin)
admin.site.register(Rent, RentAdmin)

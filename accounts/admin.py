from django.contrib import admin
from accounts.models import Account, Profile
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_no')
    search_fields = ('email',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('email',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','is_verified')

admin.site.register(Account, AccountAdmin)
admin.site.register(Profile,ProfileAdmin)


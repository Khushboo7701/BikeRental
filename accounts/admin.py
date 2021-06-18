from django.contrib import admin
from accounts.models import Account
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_no')
    search_fields = ('email',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('email',)

admin.site.register(Account, AccountAdmin)

from django.contrib import admin
from accounts.models import User
# Register your models here.

class UserModelAdmin(admin.ModelAdmin):
  list_display = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'gender' ]

admin.site.register(User, UserModelAdmin)
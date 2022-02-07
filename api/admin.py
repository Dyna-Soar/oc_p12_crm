from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, SalesEmployee, SupportEmployee, Prospect, Client, Contract, Event

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(SalesEmployee)
admin.site.register(SupportEmployee)
admin.site.register(Prospect)
admin.site.register(Client)
admin.site.register(Contract)
admin.site.register(Event)

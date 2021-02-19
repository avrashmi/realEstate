from django.contrib import admin
from .models import User,ClientType,UserType
# Register your models here.

admin.site.register(User)
admin.site.register(ClientType)
admin.site.register(UserType)
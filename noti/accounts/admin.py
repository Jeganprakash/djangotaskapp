from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

UserAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ( 'username','email', 'password1', 'password2',)
    }),
)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


# Register your models here.

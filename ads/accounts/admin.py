from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','first_name', 'last_name',
                    'region', 'phone', 'email', ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone', 'region', 'avatar', 'birth_date')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone', 'region', 'avatar', 'birth_date')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)

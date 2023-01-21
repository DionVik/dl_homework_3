from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Region
from bulletin_board.admin import AdvertisementInLine

# Register your models here.


class CustomUserAdmin(UserAdmin):
    #add_form = CustomUserCreationForm
    #form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','first_name', 'last_name',
                    'region', 'phone', 'email', ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone', 'region', 'avatar')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone', 'region', 'avatar')}),
    )
    inlines = [AdvertisementInLine,]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Region)
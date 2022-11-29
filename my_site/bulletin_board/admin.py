from django.contrib import admin
from .models import User_profile
from .models import Category
from .models import Advertisment
# Register your models here.
admin.site.register(User_profile)
admin.site.register(Category)
admin.site.register(Advertisment)


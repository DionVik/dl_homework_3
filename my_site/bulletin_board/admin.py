from django.contrib import admin
from .models import UserProfile
from .models import Category
from .models import Advertisment
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Advertisment)

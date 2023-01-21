from django.contrib import admin
from .models import Category, Advertisement

class AdvertisementInLine(admin.TabularInline):
    model = Advertisement
    fields = [ 'category', 'title', 'publication_date','content', 'picture', 'price']
    readonly_fields = ['publication_date']
    extra = 0

class AdvertisementAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['author', 'category', 'title', 'content', 'picture', 'price']}),
        ('Date information', {'fields':['publication_date',]})
    ]
    readonly_fields = ['publication_date']

    list_display = ['author', 'category', 'title', 'publication_date']


# Register your models here.
admin.site.register(Category)
admin.site.register(Advertisement, AdvertisementAdmin)


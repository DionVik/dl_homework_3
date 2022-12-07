from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^/category/(?P<category_id>\d+)', views.get_ad_list),
    re_path(r'^/category', views.get_ad_list)
    ]
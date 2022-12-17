from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^category/(?P<category_id>\d+)', views.get_ad_list, name='category'),
    path('<int:ad_id>', views.get_ad, name='ad'),
    re_path(r'^filter/(?P<category_id>\d+)', views.get_filter, name='filter')
    ]
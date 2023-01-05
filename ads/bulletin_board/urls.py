from django.urls import path, re_path
from .views import IndexView, AdDetailView
from . import views

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),
    re_path(r'^category/(?P<category_id>\d+)', views.get_ad_list, name='category'),
    path('<int:pk>', AdDetailView.as_view(), name='ad'),
]

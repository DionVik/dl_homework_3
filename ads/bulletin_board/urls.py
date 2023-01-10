from django.urls import path, re_path
from .views import IndexView, AdDetailView, AdEditView, AdDeleteView
from . import views

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),
    re_path(r'^category/(?P<category_id>\d+)$', views.get_ad_list, name='category'),
    re_path(r'^(?P<pk>\d+)/?$', AdDetailView.as_view(), name='ad'),
    re_path(r'^create/?$', views.ad_create, name='ad_create'),
    re_path(r'^(?P<pk>\d+)/edit/?$',AdEditView.as_view(), name='ad_edit'),
    re_path(r'^(?P<pk>\d+)/delete/?$', AdDeleteView.as_view(), name='ad_delete'),
    re_path(r'^(?P<ad_id>\d+)/message$', views.message_create, name='message_create')
]

from django.urls import path, re_path
from . import views as accounts_views
from .views import ProfileDetailView

urlpatterns = [
    path('signup/', accounts_views.signup, name='signup'),
    re_path(r'^(?P<pk>\d+)/*$', ProfileDetailView.as_view(), name='profile'),
    re_path(r'^(?P<pk>\d+)/ad_list/*$', accounts_views.user_ad_list, name='ad_list')

]

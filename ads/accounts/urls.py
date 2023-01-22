from django.urls import path, re_path
from . import views as accounts_views
from .views import ProfileDetailView, ProfileEditView

app_name = 'accounts'

urlpatterns = [
    path('signup/', accounts_views.signup, name='signup'),
    re_path(r'^(?P<pk>\d+)/*$', ProfileDetailView.as_view(), name='profile'),
    re_path(r'^(?P<pk>\d+)/edit/*$', ProfileEditView.as_view(), name='profile_edit')


]

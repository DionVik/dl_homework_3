from django.urls import path
from . import views as accounts_views

urlpatterns = [
    path('signup/', accounts_views.signup, name='signup'),
    #path('signup/', SignUpView.as_view(), name='signup'),
]

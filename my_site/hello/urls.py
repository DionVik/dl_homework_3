from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.say_hello, name='hello'),
    path('good_bye', views.say_goodbye, name='good_bye'),
    ]

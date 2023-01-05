from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView
# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

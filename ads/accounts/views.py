from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.views.generic import  DetailView, UpdateView, ListView
from .forms import CustomUserCreationForm
from .models import CustomUser

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "profile.html"


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomUser
    template_name = 'profile_edit.html'
    fields = ['first_name', 'last_name', 'email','region', 'phone',
               'avatar' ]

    def test_func(self):
        obj = self.get_object()
        return obj == self.request.user










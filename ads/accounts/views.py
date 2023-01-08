from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .forms import CustomUserCreationForm
from .models import CustomUser
from bulletin_board.models import Advertisement

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


class ProfileDetailView(DetailView):
    model = CustomUser
    template_name = "profile.html"


def user_ad_list(request, pk):
    current_user = CustomUser.objects.get(id=pk)
    ad_list_user = current_user.author.all()
    context = {'ad_list': ad_list_user}
    return render(request, 'user_ad.html', context)


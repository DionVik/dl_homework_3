from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from ads import settings


class CustomUserCreationForm(UserCreationForm):
    #birth_date = forms.DateField(required=False,
                                 #help_text="dd.mm.yyyy",
                                 #widget=forms.DateInput(format = '%d/%m/%Y'),
                                 #input_formats=settings.DATE_INPUT_FORMATS)
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'region', 'email', 'avatar')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


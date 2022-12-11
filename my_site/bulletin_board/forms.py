from django import forms
class FilterForm(forms.Form):
    date = forms.NullBooleanField(label="Date", widget=forms.RadioSelect)
    price = forms.NullBooleanField(label="Price", widget=forms.RadioSelect)

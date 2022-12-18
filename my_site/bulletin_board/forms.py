from django import forms
from .models import UserProfile



class FilterForm(forms.Form):
    CHOICES = [('date', 'date'), ('price', 'price')]
    CITIES = [
        ('all', 'All'),
        ('msc', 'Moscow'),
        ('tlt', 'Togliatti'),
        ('spb', 'Sankt Petersburg'),
        ('eka', 'Ekaterinburg')
    ]
    sort_type_choice = forms.ChoiceField(label="Sort by",
                                 widget=forms.RadioSelect,
                                 choices=CHOICES,
                                 initial='date')

    max_price_choice = forms.DecimalField(label='Price no more than',
                                          initial=10000000)
    region_choice = forms.ChoiceField(label='Search in region',
                                      choices=CITIES)

from django import forms
from django.core.exceptions import ValidationError
from .models import Advertisement

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

    def clean_max_price_choice(self):
        price = self.cleaned_data['max_price_choice']
        if price < 0:
            raise ValidationError('Invalid price')
        return price

class AdCreationForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['category', 'title', 'content', 'picture', 'price']
        labels = {
            'category': 'Category',
            'title': 'Title',
            'content': 'Content',
            'picture': 'Picture',
            'price': 'Price, rub'
        }
        widgets = {
            'content': forms.Textarea()
        }
        def clean_price(self):
            data = self.cleaned_data['price']
            if data < 0:
                raise ValidationError('Invalid price')
            return data
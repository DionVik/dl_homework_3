from django import forms


class FilterForm(forms.Form):
    CHOICES = [('date', '-date'), ('price', '-price')]
    my_radio = forms.ChoiceField(label="Sort by",
                                 widget=forms.RadioSelect,
                                 choices=CHOICES,
                                 initial='date')

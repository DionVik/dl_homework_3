from django.shortcuts import render
from .models import Category, Advertisement
from django.http import Http404
from .forms import FilterForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
# Create your views here.


class IndexView(ListView):
    model = Category
    template_name = 'index.html'


def get_ad_list(request, category_id=1):
    try:

        category_item = Category.objects.get(id=category_id) #объект категории с id=category_id
        ad_list = Advertisement.objects.filter(category=category_item).order_by('publication_date')
        if request.GET:
            filter_form = FilterForm(request.GET)
            if filter_form.is_valid():
                sort_type = filter_form.cleaned_data['sort_type_choice'] #выбранный тип сортировки
                max_price = filter_form.cleaned_data['max_price_choice'] #выбранная макс.цена
                region = filter_form.cleaned_data['region_choice']  #выбранный регион
                ad_list = ad_list.filter(price__lte=max_price)  # не больше макс.цены
                if region != 'all':  #если не по всем регионам
                    ad_list = ad_list.filter(user__region=region) #выдать объявления в регионе
                if sort_type == 'date':
                    ad_list = ad_list.order_by('publication_date')
                elif sort_type == 'price':
                    ad_list = ad_list.order_by('price')
                choice_data = {'sort_type_choice': sort_type, 'max_price_choice': max_price, 'region_choice': region}
                filter_form = FilterForm(choice_data)
        else:
            filter_form = FilterForm()
        context = {'filter_form': filter_form, 'category_item': category_item, 'ad_list': ad_list}
    except Category.DoesNotExist:
        raise Http404(f'Category {category_id} does not exist')
    return render(request, 'category.html', context)


class AdDetailView(DetailView):
    model = Advertisement
    template_name = 'ad.html'

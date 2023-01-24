from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from .models import Category, Advertisement
from accounts.models import Region
from django.http import Http404, HttpResponseRedirect
from .forms import FilterForm, AdCreateForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


class IndexView(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = "category_list"
    # в шаблоне можно получить список object_list ИЛИ category_list (если обобщить, то "the_model_name_list


# строковое представление строки запроса
def get_request_string(request):
    request_dic = request.GET
    request_string = ''
    for i in request_dic.items():
        #если  параметр = page, пропускаем, чтобы не ломать пагинацию0
        if i[0]=='page':
            continue
        request_string=''.join([request_string, '&', str(i[0]), '=', str(i[1])])
    return request_string

#пагинация
def pagination(request, ad_list):
    page = request.GET.get('page', 1)
    paginator = Paginator(ad_list, 3)
    try:
        ads = paginator.page(page)
    except PageNotAnInteger:
        ads = paginator.page(1)
    except EmptyPage:
        ads = paginator.page(paginator.num_pages)
    return ads

def get_ad_list(request, category_id=1):
    try:
        category_item = Category.objects.get(id=category_id) #объект категории с id=category_id
        print(f'category_item={category_item}')
        ad_list = Advertisement.objects.filter(category=category_item).order_by('publication_date')
        print(f'ad_list={ad_list}')
        if request.user.is_authenticated:
            region = request.user.region
        else:
             region = None
        request_string = get_request_string(request)
        if request.GET.get('sort_type_choice'):
            filter_form = FilterForm(request.GET)
            if filter_form.is_valid():
                sort_type = filter_form.cleaned_data['sort_type_choice'] #выбранный тип сортировки
                max_price = filter_form.cleaned_data['max_price_choice'] #выбранная макс.цена
                region = filter_form.cleaned_data['region_choice']  #выбранный регион
                ad_list = ad_list.filter(price__lte=max_price)  # не больше макс.цены
                if region != 'All':  #если не по всем регионам
                    region_object = Region.objects.get(name=region)
                    ad_list = ad_list.filter(author__region=region_object) #выдать объявления в регионе
                if sort_type == 'date':
                    ad_list = ad_list.order_by('publication_date')
                elif sort_type == 'price':
                    ad_list = ad_list.order_by('price')
                choice_data = {'sort_type_choice': sort_type, 'max_price_choice': max_price, 'region_choice': region}
                filter_form = FilterForm(choice_data)
            else:
                print ("filter_form is not valid")
        else:
            if region:  # если не по всем регионам
                ad_list = ad_list.filter(author__region=region)  # выдать объявления в регионе
            else:
                ad_list = Advertisement.objects.filter(category=category_item).order_by('publication_date')
            choice_data = {'sort_type_choice': 'date', 'max_price_choice': 10000000, 'region_choice': region}
            filter_form = FilterForm(choice_data)
            ads = pagination(request, ad_list)
            context = {'filter_form': filter_form, 'category_item': category_item, 'ad_list': ads,  'region': region}
            return render(request, 'category.html', context)
        ads = pagination(request, ad_list)
        context = {'filter_form': filter_form, 'category_item': category_item, 'ad_list': ads, 'region': region,
                   'request_string':request_string}
    except Category.DoesNotExist:
        raise Http404(f'Category {category_id} does not exist')
    return render(request, 'category.html', context)


class AdDetailView(DetailView):
    model = Advertisement
    template_name = 'ad.html'
    # внутри шаблона можно получить доступ к полям модели
    # при помощи переменной с именем object или advertisement (обобщённо "the_model_name")


@login_required
def ad_create(request):
    if request.method == 'POST':
        creation_form = AdCreateForm(request.POST, request.FILES)
        if creation_form.is_valid():
            ad = creation_form.save(commit=False)
            ad.author = request.user
            ad.publication_date = timezone.now()
            ad.save()
            pk = ad.id
            return HttpResponseRedirect(reverse("ad", args=(pk,)))
    else:
        creation_form = AdCreateForm()
    context = {'form': creation_form}
    return render(request, 'ad_creation.html', context)


class AdEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Advertisement
    template_name = 'ad_edit.html'
    fields = ['category', 'title', 'content', 'picture', 'price']

    # Проверка, что пользователь - владелец объявления
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class AdDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Advertisement
    template_name = 'ad_delete.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


def user_ad_list(request):
    if request.user.is_authenticated:
        current_user = request.user
        ad_list = current_user.ads.all()
        context = {'ad_list': ad_list}
        return render(request, 'user_ad.html', context)
    else:
        raise PermissionDenied()





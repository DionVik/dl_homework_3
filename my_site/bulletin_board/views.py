from django.shortcuts import render
from .models import Category, Advertisment, UserProfile
from django.http import Http404
from .forms import FilterForm

# Create your views here.


def index(request):
    category_list = Category.objects.all()
    context = {'category_list': category_list}
    return render(request, 'bulletin_board/index.html', context)


def get_ad_list(request, category_id=1):
    try:
        category_item = Category.objects.get(id=category_id) #объект категории с id=category_id
        ad_list = Advertisment.objects.filter(category=category_item).order_by('publication_date')
        context = {'category_item': category_item, 'ad_list': ad_list}
    except Category.DoesNotExist:
        raise Http404(f'Category {category_id} does not exist')
    return render(request, 'bulletin_board/category.html', context)


def get_ad(request, ad_id):
    ad_item = Advertisment.objects.get(id=ad_id) #объект объявления с id=ad_id
    context = {'ad_item': ad_item}
    return render(request, 'bulletin_board/ad.html', context)


def get_filter(request, category_id):
    filter_form = FilterForm()
    if request.GET:
        sort_type = request.GET['sort_type_choice'] #выбранный тип сортировки
        max_price = request.GET['max_price_choice'] #выбранная макс.цена
        region = request.GET['region_choice']  #выбранный регион

        category_item = Category.objects.get(id=category_id)

        ad_list = Advertisment.objects.filter(category=category_item)
        if region != 'all':   #если не по всем регионам
            ad_list = ad_list.filter(user__region=region) #выдать объявления в регион
        ad_list = ad_list.filter(price__lte=max_price) #не больше макс.цены
        if sort_type == 'date':
            ad_list = ad_list.order_by('publication_date')
        elif sort_type == 'price':
            ad_list = ad_list.order_by('price')

        context = {'category_item': category_item, 'ad_list': ad_list}
        return render(request, 'bulletin_board/category.html', context)

    else:
        return render(request, 'bulletin_board/filter.html',
                      {'filter_form': filter_form})


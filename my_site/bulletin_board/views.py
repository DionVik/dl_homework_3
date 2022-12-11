from django.shortcuts import render
from .models import Category, Advertisment
from django.http import Http404
from django.http import HttpResponse
from .forms import FilterForm

# Create your views here.

def index(request):
    category_list = Category.objects.all()
    context = {'category_list':category_list}
    return render(request, 'bulletin_board/index.html', context)

def get_ad_list(request, category_id=1):
    try:
        category_item = Category.objects.get(id=category_id) #объект категории с id=category_id
        ad_list = Advertisment.objects.filter(category=category_item)
        context = {'category_item':category_item, 'ad_list':ad_list}
    except Category.DoesNotExist:
        raise Http404(f'Category {category_id} does not exist')
    return render(request, 'bulletin_board/category.html', context)

def get_ad(request, ad_id):
    ad_item = Advertisment.objects.get(id=ad_id) #объект объявления с id=ad_id
    context = {'ad_item':ad_item}
    return render(request, 'bulletin_board/ad.html', context)

def get_filter(request):
    if request.method == "POST":
        is_date = request.POST.get("date")
        is_price = request.POST.get("price")
        price_value = request.POST.get("price_value", 10000)
        output = f"date = {is_date}, price = {is_price}, price value={price_value}"
        return HttpResponse(output)
    else:
        filter_form = FilterForm()
        return render(request, 'bulletin_board/filter.html',
                      {'filter_form':filter_form})


from django.shortcuts import render
from .models import Category, Advertisment
from django.http import Http404

# Create your views here.

def index(request):
    category_list = Category.objects.all()
    context = {'category_list':category_list}
    return render(request, 'bulletin_board/index.html', context)

def get_ad_list(request, category_id=1):
    try:
        category_item = Category.objects.get(id=category_id) #получаем категорию с заданным id
        ad_list = Advertisment.objects.filter(category=category_item)
        context = {'category_item':category_item, 'ad_list':ad_list}
    except Category.DoesNotExist:
        raise Http404(f'Category {category_id} does not exist')
    return render(request, 'bulletin_board/category.html', context) 
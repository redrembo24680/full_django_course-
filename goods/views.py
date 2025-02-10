from unicodedata import category
from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render

from goods.models import Products


def catalog(request, category_slag):

    page = request.GET.get('page', 1)

    if category_slag == 'all':
        goods = Products.objects.all()
    else:
        goods= get_list_or_404(Products.objects.filter(category__slag=category_slag))

    paginator  = Paginator(goods, 3)
        
    current_page = paginator.page(int(page))
    
    context = {
        "title": "Home - Каталог",
        "goods": current_page,
        "slag_url": category_slag
    }

    return render(request, "goods/catalog.html", context)


def product(request, product_slag):

    product = Products.objects.get(slag=product_slag)

    context   = {
        'product': product

    }
    return render(request, "goods/product.html", context)

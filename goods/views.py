from django.shortcuts import render

from goods.models import Products


def catalog(request):
    
    goods = Products.objects.all()
    context = {
        "title": "Home - Каталог",
        "goods": goods
    }

    return render(request, "goods/catalog.html", context)


def product(request, product_slag):

    product = Products.objects.get(slag=product_slag)

    context   = {
        'product': product


    }
    return render(request, "goods/product.html", context)

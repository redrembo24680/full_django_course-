from django.shortcuts import redirect, render

from carts.models import Cart
from goods.models import Products

def cart_add(request, product_slag):

    product = Products.objects.get(slag=product_slag)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)

        return redirect(request.META['HTTP_REFERER'])
    

def cart_change(request, product_slag):
    pass

def cart_remove(request, product_slag):
    pass


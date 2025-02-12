from itertools import product
from django.urls import path
from goods import views

app_name = 'catalog'

urlpatterns = [
    path('search/', views.catalog, name='search'),
    path('<slug:category_slag>/', views.catalog, name='index'),
    path('product/<slug:product_slag>/', views.product, name='product'),

]

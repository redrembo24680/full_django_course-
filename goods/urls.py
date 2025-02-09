from itertools import product
from django.urls import path
from goods import views

app_name = 'goods'

urlpatterns = [
    path('<slug:category_slag>/', views.catalog, name='index'),
    path('<slug:category_slag>/<int:page>/', views.catalog, name='index'),
    path('product/<slug:product_slag>/', views.product, name='product'),

]

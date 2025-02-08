from itertools import product
from django.urls import path
from goods import views

app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('product/<slug:product_slag>/', views.product, name='product'),

]

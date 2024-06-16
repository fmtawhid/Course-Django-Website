from django.urls import path
from .views import *

urlpatterns = [
    path('', shop_page, name='shop'),
    path('product/', product_page, name='product'),
]
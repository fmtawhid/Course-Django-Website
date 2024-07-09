from django.urls import path
from .views import *

urlpatterns = [
    path('', shop_page, name='books'),
    path('product/<id>', product_page, name='book'),
    path('checkout/<slug:slug>', ChackOut_Function, name='checkout'),
    path('orderDone/', shop_completed, name='orderDone'),
]
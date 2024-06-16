from django.urls import path
from .views import *

urlpatterns = [
    path('', blog_page, name='blog'),
    path('<int:id>/', blog_single_page, name='bsp'),
]
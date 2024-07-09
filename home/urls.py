from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('faq/', faq_page, name='faq'),
    path('terms/', terms_condition, name='terms'),
]


from django.urls import path
from .views import *

urlpatterns = [
    path('', course_page, name='course'),
    path('csp/<str:slug>', course_single_page, name='csp'),
    path('topic/<str:id>', topic, name='topic'),

]
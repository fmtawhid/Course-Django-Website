from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', getLogout, name='logout'),
    path('profile/', Profile, name='profile'),
    path('profile/update', Profile_Update, name='profile_update'),
    path('mainProfile/<int:id>', mainProfile, name='mainProfile'),
]
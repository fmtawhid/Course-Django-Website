from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager
from django.utils import timezone



class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50,unique=True)
    mobile_number = models.IntegerField(unique=True,null=True, blank=True)

    # personal info

    name = models.CharField(max_length=100, blank=True)
    passion = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=250, blank=True)
    profile_picture = models.ImageField(upload_to='profile', blank=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    # Date Join
    dateJoin = models.DateTimeField(default=timezone.now)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    

    
    


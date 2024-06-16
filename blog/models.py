from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    cat_name = models.CharField(max_length=50, unique=True)

    def get_url(self):
        return reverse('Category', args=[self.pk])
                                       
    def __str__(self):
        return self.cat_name

class News(models.Model):
    title = models.CharField(max_length=150, unique=True)
    description = models.TextField(max_length=700)
    images = models.ImageField(upload_to='news_images/')
    post_date = models.DateTimeField()
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('bsp', args=[self.id])
    
    def __str__(self):
        return self.title



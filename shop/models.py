from django.db import models

# Create your models here.

class Bookcategory(models.Model):
    name=models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
    

class BookModel(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(max_length=500)
    cover = models.FileField(upload_to='book_cover')
    pdf = models.FileField(upload_to='book_pdf')
    def __str__(self):
        return self.name

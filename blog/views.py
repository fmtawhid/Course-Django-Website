from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.
def blog_page(request):
    news = News.objects.all()
    category = Category.objects.all()
    Context = {
        'news':news,
        'category':category
    }
    return render(request, 'blog.html', Context)


def blog_single_page(request, id):
    news_singel = get_object_or_404(News, pk=id)
    Context = {
        'news_singel':news_singel
    }
    return render(request, 'blog-single.html', Context)

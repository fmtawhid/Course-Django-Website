from django.shortcuts import render,get_object_or_404
from .models import *
from django.db.models import Q 
from django.core.paginator import Paginator
# Create your views here.
def blog_page(request):
    news = News.objects.all()
    category = Category.objects.all()
    lat_blog = News.objects.order_by('-post_date')[:3]

    #search function
    search = request.GET.get('q')
    if search:
        news = news.filter(
            Q(title__icontains=search)
            
        )

    #Blog post pageanation Logic
    paginator = Paginator(news, 1)
    page_number = request.GET.get('page')
    paginat_course = paginator.get_page(page_number)

    Context = {
        'news':paginat_course,
        'category':category,
        'lat_blog':lat_blog
    }
    return render(request, 'blog.html', Context)


def blog_single_page(request, id):
    news_singel = get_object_or_404(News, pk=id)
    lat_blog = News.objects.order_by('-post_date')[:3]
    Context = {
        'news_singel':news_singel,
        'lat_blog':lat_blog
    }
    return render(request, 'blog-single.html', Context)

from django.shortcuts import render
from course.models import *
# Create your views here.
def home_page(request):
    course_cat = Categories.objects.all().order_by('id')[0:5]
    course = Course.objects.filter(status = 'PUBLISH').order_by('-id')
    author = Author.objects.all()

    for x in course:
        x.final_price =x.price - x.price * x.discount / 100
        
    CONTEXT = {
        'course_cat':course_cat,
        'course':course,
        'author':author,
    }
    return render(request, 'index.html', CONTEXT)

def about_page(request):
    return render(request, 'about.html')

def contact_page(request):
    return render(request, 'contact.html')

def faq_page(request):
    return render(request, 'faq.html')

def terms_condition(request):
    return render(request, 'terms-of-service.html')

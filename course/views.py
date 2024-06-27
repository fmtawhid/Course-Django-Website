from django.forms import SlugField
from django.shortcuts import render, get_object_or_404, redirect
from . models import *
from django.db.models import Q 
from django.db.models import Sum

# Create your views here.
def course_page(request):
    course_cat = Categories.objects.all().order_by('id')[0:5]
    course = Course.objects.filter(status = 'PUBLISH').order_by('-id')

    for x in course:
        x.final_price =x.price - x.price * x.discount / 100
    course_count = course.count()

    #search function
    search = request.GET.get('q')
    if search:
        course = course.filter(
            Q(title__icontains=search)
            
        )
    
    #time_duration = Video.objects.filter(course__slug = slug).aaggregate(sum = Sum('time_duration'))


    Context = {
        'course':course,
        'course_cat':course_cat,
        'course_count':course_count,
        'search':search,
    }


    return render(request, 'course.html', Context)
def course_single_page(request, slug):
    course = get_object_or_404(Course, slug=slug)
    course_cat = Categories.objects.all()

    course_id = Course.objects.get(slug = slug)
    try:
        enrolled_course = UserCourse.objects.get(user=request.user, course = course_id)
    except UserCourse.DoesNotExist:
        enrolled_course=None
    #courses = Course.objects.filter(slug=slug)

    course.final_price =course.price - course.price * course.discount / 100
    Context = {
        'course':course,
        'course_cat':course_cat,
        'enrolled_course':enrolled_course
    }
    return render(request, 'course-single.html', Context)

# Catagory Function

def topic(request, id):
    category_cat = get_object_or_404(Categories, id = id)
    course = Course.objects.filter(catagory= category_cat.id)
    
    context = {
        'course':course
    }
    return render(request, 'course.html', context)


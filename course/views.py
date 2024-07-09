from django.forms import SlugField
from django.shortcuts import render, get_object_or_404, redirect
from . models import *
from django.db.models import Q 
from django.db.models import Sum
from django.core.paginator import Paginator

# Create your views here.
def course_page(request):
    course_cat = Categories.objects.all().order_by('id')[0:5]                       #Course Category Filtering
    course = Course.objects.filter(status = 'PUBLISH').order_by('-id')              #Course Filtering by id

    for x in course:                                                                #course final price calculate
        x.final_price =x.price - x.price * x.discount / 100
    course_count = course.count()

    #search function
    search = request.GET.get('q')
    if search:
        course = course.filter(
            Q(title__icontains=search)
            
        )
    # pageanation Logic
    paginator = Paginator(course, 4)
    page_number = request.GET.get('page')
    paginat_course = paginator.get_page(page_number)

    #time_duration = Video.objects.filter(course__slug = slug).aaggregate(sum = Sum('time_duration'))


    Context = {
        'course':paginat_course,
        'course_cat':course_cat,
        'course_count':course_count,
        'search':search,
    }


    return render(request, 'product/course.html', Context)
def course_single_page(request, slug):

    course = get_object_or_404(Course, slug=slug)
    course_cat = Categories.objects.all()
    course_id = Course.objects.get(slug=slug)
    
    # enrolled course function
    enrolled_course = None

    if request.user.is_authenticated:
        try:
            enrolled_course = UserCourse.objects.get(user=request.user, course=course_id)

        except UserCourse.DoesNotExist:
            enrolled_course = None

    course.final_price = course.price - course.price * course.discount / 100

    context = {
        'course': course,
        'course_cat': course_cat,
        'enrolled_course': enrolled_course,
    }
    
    return render(request, 'product/course-single.html', context)


                                                                                # Catagory Function
def topic(request, id):
    category_cat = get_object_or_404(Categories, id=id)                         #Category single page function
    course = Course.objects.filter(category=category_cat.id)                    #Course filter by category
    course_cat = Categories.objects.all()
    course_count = course.count()
    context = {
        'course': course,
        'course_cat': course_cat,
        'course_count':course_count
    }
    return render(request, 'product/course_cat.html', context)

def shop_completed(request):
    return render(request, 'shop-order-completed.html')

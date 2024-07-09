from django.shortcuts import redirect, render, get_object_or_404
from course.models import * 
from .models import*


# Create your views here.
def shop_page(request):
    book = BookModel.objects.all()
    book_count = book.count()
    Context = {
        'book':book,
        'book_count':book_count,
    }
    return render(request, 'product/book.html', Context)
def product_page(request, id):
    book = get_object_or_404(BookModel, id=id)
    Context = {
        'book':book,
    }
    return render(request, 'product/single-book.html', Context)

def ChackOut_Function(request, slug):
    course = Course.objects.get(slug=slug)
    if course.price == 0:
        user_course = UserCourse(
            user=request.user,
            course=course,
        )
        user_course.save()
        return redirect('mainProfile', id=request.user.id)  # Pass the user ID here
    tax = (course.price / 100)*2
    total = course.price + tax
    context = {
        'course':course,
        'tax':tax,
        'total':total,
    }
    return render(request, 'checkout.html', context)

def shop_completed(request):
    return render(request, 'shop-order-completed.html')
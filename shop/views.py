from django.shortcuts import redirect, render
from course.models import * # Create your views here.
def shop_page(request):
    return render(request, 'shop.html')
def product_page(request):
    return render(request, 'product.html')

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

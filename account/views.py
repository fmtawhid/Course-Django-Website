from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from course.models import *


from django.contrib.auth import authenticate,login,logout
from .EmailBackEnd import EmailBackEnd
# Create your views here.

def login_page(request):                                                    #Login Function Function
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
		
        user = EmailBackEnd.authenticate(request, username=email, password=password)

        if user!=None:
           login(request,user)
           return redirect('home')
        else:
           messages.error(request,'Email and Password Are Invalid !')
           return redirect('login')
    
    return render(request, 'account/login.html')

def register_page(request):                                                 #Register Function
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():                       #chack email in database
            messages.warning(request, 'Email Alrady exists')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username Alrady exists')
            return redirect('register')
        
        user = User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        return redirect('login')

    return render(request, 'account/register.html')


def getLogout(request):
    logout(request)
    return redirect('home')

def Profile(request):

    return render(request, 'account/profile.html')

def Profile_Update(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = request.user.id

        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        user.save()
        messages.success(request,'Profile Are Successfully Updated. ')
        return redirect('profile')

def mainProfile(request, id):
    user = get_object_or_404(User, pk=id)
    courses = UserCourse.objects.filter(user = request.user)
    CONTEXT = {
        'user':user,
        'courses':courses,
    }
    return render(request, 'account/main_profile.html', CONTEXT)
    

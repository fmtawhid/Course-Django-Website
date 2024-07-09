from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from course.models import *


from django.contrib.auth import get_user_model                      
User = get_user_model
from .models import CustomUser as User                                  #Convert Default user to custom user

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
           return redirect('/')
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


def getLogout(request):                                                     #Logut Function
    logout(request)
    return redirect('home')

def Profile(request):

    return render(request, 'account/profile.html')

def Profile_Update(request):                                                #Profile Update Function
    if request.method == "POST":
        username = request.POST.get('username')
        name = request.POST.get('name')
        profession = request.POST.get('profession')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        profile_picture = request.POST.get('profile')
        number = request.POST.get('number')

        password = request.POST.get('password')
        user_id = request.user.id

        user = User.objects.get(id=user_id)
        user.name = name
        user.passion = profession
        user.username = username
        user.email = email
        user.bio = bio
        user.profile_picture = profile_picture
        user.mobile_number = number

        if password != None and password != "":
            user.set_password(password)
        user.save()
        messages.success(request,'Profile Are Successfully Updated. ')
        return redirect('profile')

def mainProfile(request, id):                                                  #Profile View Function
    user = get_object_or_404(User, pk=id)
    courses = UserCourse.objects.filter(user = request.user)
    enroled_count= courses.count()
    CONTEXT = {
        'user':user,
        'courses':courses,
        'enroled_count':enroled_count,
    }
    return render(request, 'account/main_profile.html', CONTEXT)
    

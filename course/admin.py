from django.contrib import admin
from .models import *
# Register your models here.

class what_you_learn_TabularInline(admin.TabularInline):
    model = what_you_learn
class requirment_TabularInline(admin.TabularInline):
    model = requirment

class lesson_TabularInline(admin.TabularInline):
    model = lessons

class video_TabularInline(admin.TabularInline):
    model = Video



    
class course_admin(admin.ModelAdmin):
    inlines = (what_you_learn_TabularInline, requirment_TabularInline, lesson_TabularInline, video_TabularInline)




admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(Course, course_admin)
admin.site.register(lessons)
admin.site.register(Video)
admin.site.register(what_you_learn)
admin.site.register(requirment)
admin.site.register(UserCourse)
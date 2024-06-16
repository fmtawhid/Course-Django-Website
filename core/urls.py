from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('courses/', include('course.urls')),
    path('blog/', include('blog.urls')),
    path('shop/', include('shop.urls')),
    path('', include('account.urls')),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
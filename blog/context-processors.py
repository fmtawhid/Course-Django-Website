from .models import *
def cat_links(request):
    links = Category.objects.all()
    return dict(links = links)
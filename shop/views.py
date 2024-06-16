from django.shortcuts import render

# Create your views here.
def shop_page(request):
    return render(request, 'shop.html')
def product_page(request):
    return render(request, 'product.html')

from django.shortcuts import render

def index(request):
    context = {
        'title': 'Store_hom',
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'Store - Каталог',
    }
    return render(request, 'products/products.html', context)

from django.shortcuts import render
from shop.models import Category, Brand, Product


def base_view(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.all()

    context = {
        'categories': categories,
        'brands': brands,
        'products': products
    }

    return render(request, 'base.html', context)

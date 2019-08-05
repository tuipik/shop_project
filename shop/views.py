from django.shortcuts import render
from shop.models import Category, Brand, Product


def base_view(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.all()
    for_promo = Product.objects.filter(for_promo=True)

    context = {
        'categories': categories,
        'brands': brands,
        'products': products,
        'for_promo': for_promo,
    }

    return render(request, 'base.html', context)


def product_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    categories = Category.objects.all()

    context = {
        'product': product,
        'categories': categories,
    }
    return render(request, 'product.html', context)


def category_view(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    categories = Category.objects.all()
    products_of_category = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products_of_category': products_of_category,
        'categories': categories,
    }
    return render(request, 'category.html', context)

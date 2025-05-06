from django.shortcuts import render
from .models import Product, Category


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    category_filter = request.GET.get('category')
    if category_filter:
        products = products.filter(category__slug=category_filter)

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'index.html', context)

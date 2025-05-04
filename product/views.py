from django.shortcuts import render
from django.views.generic import ListView
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


class ProductListView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category_filter = self.request.GET.get('category')
        if category_filter:
            queryset = queryset.filter(category__slug=category_filter)
        return queryset
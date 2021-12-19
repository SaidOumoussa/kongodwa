from django.shortcuts import render
from .models import Product


def index(request):
    product = Product.objects.all()
    return render(request, 'index.html', {'product': product})


def contact(request):
    return render(request, 'contact.html', {})


def shoping(request):
    return render(request, 'shoping-cart.html', {})


def checkout(request):
    return render(request, 'checkout.html', {})


def shoprod(request):
    return render(request, 'shop-grid.html', {})


def index1(request):
    product = Product.objects.all()
    return render(request, 'ecoapp/index.html', {'product':product})


def base(request):
    return render(request, 'ecoapp/base.html', {})


def article1(request):
    return render(request, 'blog-details.html', {})


def shope(request):
    return render(request, 'shop-details.html', {})


def shop(request):
    return render(request, 'shop-grid.html', {})


def products(request):
    products = Product.objects.all()
    return render(request, 'ecoapp/product.html', {'products': products})


def product(request, id, *args, **kwargs, ):
    product = Product.objects.filter(id=id)
    return render(request, 'ecoapp/product_id.html', {'product': product})


from django.shortcuts import render
from .models import Product


def products(request):
    pro =Product.objects.all()
    x = {"pro":pro}
    return render(request,"products/products.html",x)

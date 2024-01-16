from django.shortcuts import render
from .models import Product

# def company_productList(request):
#     content_list = MainContent.objects.order_by("-pub_date")
#     context = {"content_list": content_list}
#     return render(request, "mysite/productList.html", context)

def company_productList(request):
    productList = Product.objects.order_by("-pub_date")
    dataSet = {"productList": productList}
    return render(request, "mysite/productList.html", dataSet)

def company_productLine(request, productLineNumber):
    productList = Product.objects.filter(productLine=productLineNumber).order_by("-pub_date")
    dataSet = {"productList": productList}
    return render(request, "mysite/productLine.html", dataSet)

def detail(request, product_name):
    productList = Product.objects.get(name=product_name)
    dataSet = {'productList': productList}
    return render(request, 'mysite/detail.html', dataSet)


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

def company_productLine1(request):
    productList = Product.objects.order_by("-pub_date")
    dataSet = {"productList": productList}
    return render(request, "mysite/productLine1.html", dataSet)

def company_productLine2(request):
    productList = Product.objects.order_by("-pub_date")
    dataSet = {"productList": productList}
    return render(request, "mysite/productLine2.html", dataSet)

def company_productLine3(request):
    productList = Product.objects.order_by("-pub_date")
    dataSet = {"productList": productList}
    return render(request, "mysite/productLine3.html", dataSet)

def company_productLine4(request):
    productList = Product.objects.order_by("-pub_date")
    dataSet = {"productList": productList}
    return render(request, "mysite/productLine4.html", dataSet)
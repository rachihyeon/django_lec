from django.shortcuts import render

def mainpage(request):
    return render(request, 'pages/mainpage.html')

def company_introduce(request):
    return render(request, 'pages/company_introduce.html')

def company_history(request):
    return render(request, 'pages/company_history.html')

def company_info(request):
    return render(request, 'pages/company_info.html')

def login_page(request):
    return render(request, 'pages/login.html')
from django.core.exceptions import PermissionDenied
from django.shortcuts import  get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Comment
from .forms import CommentForm

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

@login_required(login_url='common:login')
def comment_create(request, product_name):
    # productList = get_object_or_404(Product, pk=product_name)
    productList = Product.objects.get(name=product_name)
    if request.method == 'POST':
        form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.content_list = productList
        comment.author = request.user
        comment.save()
        # return redirect('detail', content_id=productList.name)
        return render(request, 'mysite/detail.html', {'productList': productList})
    else:
        form = CommentForm()
        context = {'productList': productList, 'form': form}
        return render(request, 'mysite/detail.html', context)

@login_required(login_url='common:login')
def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    productList = Product.objects.get(name=comment.content_list)
    if request.user != comment.author:
        raise PermissionDenied
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            # return redirect('detail', content_id=comment.content_list.id)
            return render(request, 'mysite/detail.html', {'productList': productList})
    else:
        form = CommentForm(instance=comment)
    context = {'comment': comment, 'form': form}
    return render(request, 'mysite/comment_form.html', context)

@login_required(login_url='accounts:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    productList = Product.objects.get(name=comment.content_list)
    if request.user != comment.author:
        raise PermissionDenied
    else:
        comment.delete()
    # return redirect('detail', content_id=comment.content_list.id)
    return render(request, 'mysite/detail.html', {'productList': productList})
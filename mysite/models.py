from django.db import models
from django.contrib.auth.models import User

class MainContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField("date published")

class Product(models.Model):
    name = models.CharField(max_length=100)
    productLine = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    description = models.TextField()
    pub_date = models.DateTimeField("date published")
    image = models.ImageField(upload_to='products/', blank=True)
    def __str__(self):
        return self.name

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content_list = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

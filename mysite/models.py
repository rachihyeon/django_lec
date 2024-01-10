from django.db import models

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

# 택일적인 제품군을 필드를 만들어서 제작 -> admin페이지 새로 제작 必
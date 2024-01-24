
from django.contrib import admin
from .models import MainContent
from .models import Product, Comment

admin.site.register(MainContent)
admin.site.register(Product)
admin.site.register(Comment)
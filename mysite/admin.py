
from django.contrib import admin
from .models import MainContent
from .models import Product, Comment
class MainContentAdmin(admin.ModelAdmin):
    list_display = ['name', 'productLine', 'price', 'description', 'pub_date', 'image']
    search_fields = ['name']
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'content_list', 'content', 'create_date', 'modify_date']
    search_fields = ['author__username']

admin.site.register(MainContent)
admin.site.register(Product, MainContentAdmin)
admin.site.register(Comment, CommentAdmin)


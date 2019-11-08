from django.contrib import admin
from .models import Article,Comment

"""выносим наши модели в админку"""
admin.site.register(Article)
admin.site.register(Comment)
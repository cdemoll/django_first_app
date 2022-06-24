from django.contrib import admin
from django.urls import path
from django.views.defaults import server_error

from blog.views import index, article01, article02, article03

urlpatterns = [
    path('', index, name='blog-index'),
    path('article-01/', article01, name='blog-article-01'),
    path('article-02/', article02, name='blog-article-02'),
    path("article-03/", article03, name='blog-article-03')
]
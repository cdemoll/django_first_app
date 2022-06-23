from django.contrib import admin
from django.urls import path
from django.views.defaults import server_error

from blog.views import index

urlpatterns = [
    path('', index, name='blog-index'),
]

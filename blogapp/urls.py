from django.contrib import admin
from django.urls import path
# import blogapp.views 또는
from .import views

urlpatterns = [
    path('<int:blog_id>', views.detail, name="detail"),
    path('new/', views.new, name='new'),
    path('create/', views.create, name="create"),
    # path('newblog/', views.blogpost, name="blogpost"),
]

from django.shortcuts import render
from .models import Post
from django.views.generic import ListView


class PostListView(ListView):
    template_name = 'posts/home.htm'
    model = Post
    context_object_name = 'posts'
    
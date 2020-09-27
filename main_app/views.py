from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def index(request):
    return HttpResponse('<h1>Hello, World</h1>')

def post_index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts':posts})
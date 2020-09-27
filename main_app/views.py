from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/posts'

class PostUpdate(UpdateView):
    model = Post
    fields = ['content','title','category']

    def form_valid(self, form):
        self.object = form.save(commit=False) 
        self.object.save()
        return HttpResponseRedirect('/posts/'+str(self.object.pk))

class PostDelete(DeleteView):
    model = Post
    success_url = '/posts'


def index(request):
    return HttpResponse('<h1>Hello, World</h1>')

def post_index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts':posts})

def post_show(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/show.html', {'post':post})
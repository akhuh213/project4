from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'posts': posts})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled.')
            else:
                print('The username and/or password is incorrect.')
        else:
            print('The username and/or password is incorrect.')
    else: 
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/posts')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/posts')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/posts'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/posts'+str(self.object.pk))
        

class PostUpdate(UpdateView):
    model = Post
    fields = ['content','title','category']

    def form_valid(self, form):
        self.object = form.save(commit=False) 
        self.object.save()
        return HttpResponseRedirect('/posts/'+str(self.object.pk))

@method_decorator(login_required, name='dispatch')
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
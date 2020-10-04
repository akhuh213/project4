from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Post, Comment, Profile, Message
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .filters import SearchFilter
from django.contrib import messages
from django.db.models import Q

# Create your views here.


@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(user=user)
    return render(request, 'profile.html', {'user': user, 'posts': posts})

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
                    messages.info(request, 'You are logged in')
                    return HttpResponseRedirect('/posts/')
                else:
                    messages.info(request, 'The acccount has been disabled')
                    return HttpResponseRedirect('/login/')
                   
            else:
                messages.info(request, 'The username and/or password is incorrect.')
                return HttpResponseRedirect('/login/')
           
        else:
            messages.info(request, 'The username and/or password is incorrect.')
            return HttpResponseRedirect('/login/')
         
    else: 
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    # messages.info(request, 'Successfully logged out')
    return HttpResponseRedirect('/')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            user = form.cleaned_data['username']
            # return render(request, 'profile.html', {'username':user})
            return HttpResponseRedirect('/posts')
        else:            
            return render(request, 'signup.html', {'form': form})  
            
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

class PostCreate(CreateView):
    model = Post
    fields = ['title','content','category','age','condition','price','zipcode','img']


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/posts/'+str(self.object.pk))
        

class PostUpdate(UpdateView):
    model = Post
    fields = ['content','title','category','price','sold']

    def form_valid(self, form):
        self.object = form.save(commit=False) 
        self.object.save()
        return HttpResponseRedirect('/posts/'+str(self.object.pk))

@method_decorator(login_required, name='dispatch')
class PostDelete(DeleteView):
    model = Post
    success_url = '/posts'



class CommentCreate(CreateView):
    model = Comment
    fields = ['content']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.post_id = Post.objects.get(pk= self.kwargs['pk'])
        self.object.save()
        print(self.object.post_id)
        return HttpResponseRedirect('/posts/'+str(self.object.post_id.pk))

@method_decorator(login_required, name='dispatch')
class CommentUpdate(UpdateView):
    model = Comment
    fields = ['content']

    def form_valid(self, form):
        self.object = form.save(commit=False) 
        self.object.save()
        return HttpResponseRedirect('/posts/'+str(self.object.post_id.pk))



@method_decorator(login_required, name='dispatch')
class CommentDelete(DeleteView):
    model = Comment    
    success_url = '/posts/'   

class MessageCreate(CreateView):
    model = Message
    fields = ['content']


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.sender = self.request.user
        self.object.receiver = User.objects.get(pk= self.kwargs['pk'])
        self.object.save()
        print(self.object.receiver)
        
        return HttpResponseRedirect('/message/'+str(self.object.sender.pk)+'/inbox/'+str(self.object.receiver.pk))

@method_decorator(login_required, name='dispatch')
class MessageDelete(DeleteView):
    model = Message    
    success_url = '/posts/' 

def inbox_view(request, username):
    print(username)
    user = User.objects.get(username=username)
    message = Message.objects.filter(receiver=user.pk).order_by('sender','-timestamp').distinct('sender')
    print(message)
    # messagess = message.distinct('receiver_id')
    return render(request, 'message/inbox.html', {'messagess':message, 'user':user })

def inbox_detail_view(request, username, sender_id):
    # print(username)
    user = User.objects.get(pk=username)
    message = Message.objects.filter(Q(receiver=user.pk,sender= sender_id)| Q(receiver= sender_id, sender=user.pk)).order_by('timestamp') 
    receiver = sender_id
    receiver_name = User.objects.get(pk=sender_id)
    for msg in message:
        print(msg.receiver.id, username, msg.new)
        if str(msg.receiver.id) == username:
            print(msg.receiver.id, username)
            msg.new = False
            msg.save()
            print(msg.new)
        else:
            print('hello')

    # message = Message.objects.filter(receiver=user, sender=sender_id)
    return render(request, 'message/inbox_detail.html', {'messagess':message, 'user':user, 'receiver':receiver, 'receiver_name':receiver_name})

def index(request):

    return render(request, 'index.html')



def post_index(request):
    posts = Post.objects.all().order_by('-created_on')    
    myFilter = SearchFilter(request.GET, queryset=posts)
    posts = myFilter.qs

    return render(request, 'posts/index.html', {'posts':posts, 'myFilter':myFilter})


def post_show(request, post_id):
    post = Post.objects.get(id=post_id)
    comment = Comment.objects.get
    return render(request, 'posts/show.html', {'post':post})


def handler404(request):
    return render(request, '404.html', status=404)
    
def handler500(request):
    return render(request, '500.html', status=500)

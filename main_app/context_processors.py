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





# def add_variable_to_context(request):
#     print(str(request.user.id))
#     message = Message.objects.filter(receiver=str(request.user.id))

#     print(message)
#     count = 0
#     for msg in message:
#         print(msg.new)
#         if msg.new == True:
#             count += 1
#             print(msg.receiver, msg.content, msg.new, msg.timestamp)
#             return {"test": "new message"}
#         if msg.new == False:
#             return {"test": "no message"}

def add_variable_to_context(request):
    print(str(request.user.id))

    if request.user.id:
        message = Message.objects.filter(receiver=str(request.user.id), new=True) 
        print(message)
        if message:
            return {"test": "You have new message!"}
        else:
            return{"test":"no new message"}
    else:
        return {"test":""}
            
            
            
            
    #         return {""}
    #         for msg in message:
    #             print(msg.new)
    #             if msg.new == True:
    #                 count=+1
    #                 if count >= 1:

    #                     print(msg.receiver, msg.content, msg.new, msg.timestamp)
    #                     return {"test": "You have new messages!"}
    #                 else:
    #                     return {"test": "no new message"}
    #             else:
    #                 return {"test": "no new message"}
    #     else:
    #         return {"test":"."}
    # else:
    #     return {"test":"please, log in"}
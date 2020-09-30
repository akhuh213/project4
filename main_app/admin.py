from django.contrib import admin
from .models import Post, Comment, Profile, Message
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Message)
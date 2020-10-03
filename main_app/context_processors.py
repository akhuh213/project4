
from .models import Post, Comment, Profile, Message
from .filters import SearchFilter
from django.contrib import messages



def add_variable_to_context(request):
    # print(str(request.user.id))
    return {"test":"test"}
    # if request.user.id is not None:
    #     message = Message.objects.filter(receiver=str(request.user.id))

    #     print(message)
    #     if message is not None:
    #         for msg in message:
    #             print(msg.new)
    #             if msg.new == True:

    #                 print(msg.receiver, msg.content, msg.new, msg.timestamp)
    #                 return {"test": "You have new messages!"}
    #             if msg.new == False:
    #                 return {"test": "no new message"}
    #     else:
    #         return {"test":"."}
    # else:
    #     return {"test":"please, log in"}
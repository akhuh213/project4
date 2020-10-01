
from .models import Post, Comment, Profile, Message


def add_variable_to_context(request):
    print(str(request.user.id))
    message = Message.objects.filter(receiver=str(request.user.id))

    print(message)
    count = 0
    for msg in message:
        print(msg.new)
        if msg.new == True:
            count += 1
            print(msg.receiver, msg.content, msg.new, msg.timestamp)
            return {"test": "new message"}
        if msg.new == False:
            return {"test": "no message"}
    
        # else:
        #     pass
   
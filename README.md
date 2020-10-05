# project4 - Kids 2 Kids

## Purpose
This is an app for users to enable to sell or buy children's used items

## Technologies Used
- django
- Postgresql
- python


Database ERD
![ERD](./static/image/kids2kids_erd.png)

working scope

Sun :
1. setup posts model (x)
2. finish CRUD for posts  
    - Get route for posts (x)
    - get route for specific post (x)
    - put route for posts (x)
    - delete route for posts (x)
3. User model 
    - user authentication (x)

Mon : 

struggle: 
- grabbing post id when create the comments 
    - solution: self.object.post_id = Post.objects.get(pk= self.kwargs['pk']) 
- grabing posot id when deleting comment. cannot go back to the post (success_url)
    - solution: not solved completely. for now, just set the success_url to '/posts/'


1. Post (x)
    - image uploading (x)
2. zipcode 
3. setup the comments model (x)
4. comments CRUD
    - comment get (x)
    - commnet post (x)
    - comment put (x)
    - comment delete (x)


Tue : 
struggle : pip install filter to python 2.7
solution: 
pip3 install --upgrade --force pip
python3 -m pip install --upgrade --force pip
pip -V


1. Search 
    a. basic (x)
    - Set up search model (x)
    - Make search bar (x)
    - Filter function (x)
    - get route to post model (x)
    - result showing page (x)

* stretch goals : more precise search 

    b. showing previous related search 
    - create route to search model 
    - get route to search model to grab the realted posts from Post model to display 


    2. zipcode (half)



Wed :

blocker: displaying the reciever's name in create msg form. (solved)
displaying sender's name olny once in message index

1. setup the message model (x)
2. message CRUD 
    - msg create(x)
        - msg form (x)
    - msg get (using filter) 
        - sender (x)
        - recieved msg (x)
    - msg delete all
        - sender
        - reciever

3. new msg alert

Thurs : 
1. people also viewed 
2. CSS 


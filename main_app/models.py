from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver 

# Create your models here.
class Post(models.Model):
    TOY = 'TY'
    DIAPER = 'DP'
    CLOTHES = 'CL'
    BOOK = 'BK'
    OTHERS = 'OT'
    THREEMONTH = '3M'
    SIXMONTH = '6M'
    NINEMONTH = '9M'
    ONEYEAR = '1y'
    TWOYEAR = '2Y'
    THREEYEAR = '3Y'
    FOURYEAR = '4Y'
    FIVEYEAR = '5Y'
    NEW = 'NW'
    LIKEANEW = 'LN'
    GOOD = "GD"
    FAIR = "FR"
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=300)
    CATEGORY_CHOICES = [
        (TOY, 'Toys'),
        (DIAPER, 'Diapers'),
        (CLOTHES, 'Clothes'),
        (BOOK, 'Books'),
        (OTHERS, 'Others'),
    ]
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
    )
    AGE_CHOICES = [
        (THREEMONTH,'3m'),
        (SIXMONTH, '6m'),
        (NINEMONTH, '9m'),
        (ONEYEAR, '1yr'),
        (TWOYEAR, '2yr'),
        (THREEYEAR, '3yr'),
        (FOURYEAR, '4yr'),
        (FIVEYEAR, '5yr'),
    ]
    age = models.CharField(
        max_length=2,
        choices=AGE_CHOICES,
    )
    CONDITION_CHOICES = [
        (NEW, 'New'),
        (LIKEANEW, 'Like a new'),
        (GOOD, 'Good'),
        (FAIR, 'Fair'),
    ]
    condition = models.CharField(
        max_length=2,
        choices=CONDITION_CHOICES,
    )
    zipcode = models.CharField(max_length=5, default = 20152)
    price = models.IntegerField()
    sold = models.BooleanField(default=False)
    img = models.ImageField(upload_to='images/', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   
    
    class Meta:
        ordering = ['created_on']


    def __str__(self):
        return (self.title)



class Search(models.Model):
    item = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Message(models.Model):
    content = models.TextField(max_length=500)
    sender = models.ForeignKey(User(), on_delete=models.CASCADE,related_name="sender")
    receiver = models.ForeignKey(User(), on_delete=models.CASCADE, related_name="receiver")
    message_file = models.FileField(upload_to='message/')
    timestamp = models.DateTimeField(auto_now_add=True)
    new = models.BooleanField(default = True)
    
    class Meta:
        ordering = ['timestamp']
    def __str__(self):
        return (self.content)




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    zipcode = models.PositiveIntegerField()
    email = models.EmailField()
    searches = models.ManyToManyField(Search)
    

    def __str__(self):
        return (self.zipcode)




   
class Comment(models.Model):
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
    def __str__(self):
        return 'Comment {} by {}'.format(self.content, self.user)



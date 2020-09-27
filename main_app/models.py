from django.db import models
from django.contrib.auth.models import User

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
    content = models.CharField(max_length=300)
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
    price = models.IntegerField
    sold = models.BooleanField(default=False)
    img = models.ImageField(upload_to='images/', blank=True)
    

    
    


    def __str__(self):
        return (self.title)
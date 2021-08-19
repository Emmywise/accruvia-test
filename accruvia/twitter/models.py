from django.db import models
# Create your models here.

#tweet model class
class Tweets(models.Model):

    name = models.CharField(max_length=50,)
    tweet = models.CharField(max_length=50, )
    date_created = models.DateTimeField(auto_now_add=True)
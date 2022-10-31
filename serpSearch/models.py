from cmd import IDENTCHARS
from unittest.util import _MAX_LENGTH
from django.db import models

class Searches(models.Model):
    factCheckUser= models.CharField(max_length=100)
    TwitterHandle= models.CharField(max_length=100)
    TweetId=models.CharField(max_length=200)
    created_date = models.DateTimeField('date published')
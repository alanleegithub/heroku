from django.db import models
import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    published_date = models.DateTimeField(default=datetime.datetime.now)
    author = models.CharField(max_length=250)

    def __unicode__(self):
      return self.title

class Comment(models.Model):
     post_id = models.DecimalField(decimal_places=2, max_digits=5)
     body = models.CharField(max_length=250)
     published_date = models.DateTimeField(default=datetime.datetime.now)
     author = models.CharField(max_length=250)

     def __unicode__(self):
       return self.body

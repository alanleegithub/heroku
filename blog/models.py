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

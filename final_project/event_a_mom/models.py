from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.template.defaultfilters import slugify

# class Events(models.Model):
#     event_id = models.IntegerField()
#     event_count = models.IntegerField()
#     event_time = models.CharField(max_length=45)

class Event(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    slug = models.SlugField(blank=True, unique=True, default='')

    def save(self, *args, **kwargs):
        self.slug =slugify(self.name)
        super(Event,self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'events'

    def __str__(self): #For Python 2, use __unicode__ too
        return self.name


class EventDetails(models.Model):
    event = models.ForeignKey(Event)
    title = models.CharField(max_length=128)
    cost = models.CharField(max_length=10,default='')
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self): #For Python 2, use _unicode__ too
        return self.title


class UserProfile (models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

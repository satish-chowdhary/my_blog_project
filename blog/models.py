from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
       def get_queryset(self):
              return super(PublishedManager, self).get_queryset().filter(status= 'published')

class Post(models.Model):
       STATUS_CHOICE = (
              ('draft' , 'Draft'),
              ('published' , 'Published')
       )
       title = models.CharField(max_length = 200)
       slug = models.SlugField(max_length = 200, unique_for_date = 'publish')
       author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blog_post')
       body = models.TextField()
       publish = models.DateTimeField(default = timezone.now)
       created = models.DateTimeField(auto_now_add = True)
       updated = models.DateTimeField(auto_now = True)
       status = models.CharField(max_length = 200, choices = STATUS_CHOICE, default = 'draft')

       objects = models.Manager()
       published = PublishedManager()
       class Meta:
              ordering = ('-publish',)

       def __str__(self):
           return self.title
                                                                                      

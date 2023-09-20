from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField(max_length=100000, blank=True, null=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title[50:] + '...'
    
    def get_absolute_ulr(self):
        reverse("post", kwargs={"post_id": self.pk})

    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['publication_date', 'title', 'author']


class Comment(models.Model):
    text = models.TextField(max_length=10000)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
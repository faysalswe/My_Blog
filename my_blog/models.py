from django.db import models
from datetime import datetime
from django.conf import settings
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    info = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    is_publish = models.BooleanField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=2)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Articles"

class Comment(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=2)

    def __str__(self):
        return self.body
    class Meta:
        verbose_name_plural = "Comments"
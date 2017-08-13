from __future__ import unicode_literals

from django.db import models

from ArticleClassModel.models import ArticleClass

# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=20)
    create_datetime = models.DateTimeField()
    artile_class = models.ForeignKey(ArticleClass)
    browse_times = models.IntegerField()
    fabulous = models.IntegerField()
    
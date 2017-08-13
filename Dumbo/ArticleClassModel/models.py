from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ArticleClass(models.Model):
    article_class_id = models.AutoField(primary_key=True)
    name = models.CharField(20)
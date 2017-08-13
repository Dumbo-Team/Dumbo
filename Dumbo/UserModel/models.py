from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20)
    passwd = models.CharField(max_length=10)
    portrait = models.URLField()
    email = models.EmailField()
    qq = models.CharField(max_length=20)
    tele = models.CharField(max_length=15)
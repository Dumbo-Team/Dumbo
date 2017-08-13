from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TeamUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    tele = models.CharField(max_length=15)
    email = models.EmailField()
    school = models.CharField(max_length=50)
    education = models.CharField(max_length=10)
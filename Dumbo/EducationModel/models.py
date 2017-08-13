from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Education(models.Model):
    edu_id = models.AutoField(primary_key=True)
    school = models.CharField(max_length=50)
    education = models.CharField(max_length=20)
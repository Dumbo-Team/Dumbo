from __future__ import unicode_literals

from django.db import models
from UserModel.models import User

# Create your models here.
class UserMap(models.Model):
    name = models.CharField(max_length=50)
    longtitude = models.FloatField()
    latitude = models.FloatField()
    describe = models.TextField()
    user = models.ForeignKey(User)
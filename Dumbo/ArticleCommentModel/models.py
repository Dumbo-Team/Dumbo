from __future__ import unicode_literals

from django.db import models

from UserModel.models import User
from ArticleModel.models import Article

# Create your models here.
class ArticleCommentModel(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    article = models.ForeignKey(Article)
    content = models.TextField()
from django.db import models
from datetime import datetime
from django.db.models import *
import ast
 #自定义数据库字段
class ListField(models.TextField):
	# __metaclass__ = models.SubfieldBase
	description = "Stores a python list"
	def __init__(self, *args, **kwargs):
		super(ListField, self).__init__(*args, **kwargs)
	def to_python(self, value):
		if not value:
			value = []
		if isinstance(value, list):
			return value
		return ast.literal_eval(value)
	def get_prep_value(self, value):
		if value is None:
			return value
		return str(value) #use str(value) in Python 3
	def value_to_string(self, obj):
		value = self._get_val_from_obj(obj)
		return self.get_db_prep_value(value)
# Create your MoodTalk here.映射为sport_delicacy
class MoodTalk(models.Model):
    moodtalk_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    datetime = models.DateTimeField(datetime.now())
    paragraph = models.TextField()
    image_list = ListField(blank=True,default=[])


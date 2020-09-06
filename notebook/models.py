from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class MainCategory(models.Model):
	category=models.CharField(max_length=30)
	category_creator=models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		return self.category
	def get_absolute_url(self):
		return reverse('create_category')
class Tasks(models.Model):
	task=models.CharField(max_length=40)
	task_category=models.ForeignKey(MainCategory,on_delete=models.CASCADE)
	task_creator=models.ForeignKey(User,on_delete=models.CASCADE)
	task_status=models.BooleanField(default=False)
	priority_list=[ 
	(1,'Important and Urgent'),
	(2,'Urgent'),
	(3,'Important'),
	(4,'Not Important Nor Urgent')
	]
	task_priority=models.IntegerField(choices=priority_list,default=4)

	def __str__(self):
		return self.task
	def get_absolute_url(self):
		return reverse('')

				

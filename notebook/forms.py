from django import forms
from django.forms import ModelForm
from .models import Tasks,MainCategory

class TaskForm(forms.ModelForm):
	class Meta:
		model=Tasks
		fields=['task','task_priority']
class Task_Category_Form(forms.ModelForm):
	class Meta:
		model=Tasks
		fields=['task','task_category','task_priority']

class CategoryForm(forms.ModelForm):
	class Meta:
		model=MainCategory
		fields=['category']
		

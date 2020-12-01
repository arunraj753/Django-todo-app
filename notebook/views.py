from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import MainCategory,Tasks
from .forms import TaskForm,Task_Category_Form,CategoryForm
# Create your views here.
@login_required
def Task_Create(request):
	if(request.method=='POST'):
		form=Task_Category_Form(request.POST)
		form.instance.task_creator=request.user
		form.save()
		print("Success")
	form=Task_Category_Form()
	form.fields["task_category"].queryset=MainCategory.objects.filter(category_creator=request.user)
	nav=MainCategory.objects.filter(category_creator=request.user).all()
	context={'form':form,'nav':nav}
	return render(request,'notebook/homepage.html',context)
@login_required
def Category_Create(request):
	if request.method=='POST':
		form=CategoryForm(request.POST)
		form.instance.category_creator=request.user
		if form.is_valid():
			form.save()
	form=CategoryForm()
	nav=MainCategory.objects.filter(category_creator=request.user).all()
	context={'form':form,'nav':nav}
	return render(request,'notebook/createcategory.html',context)
def Task_Update(request,pk):
	task_to_update=Tasks.objects.get(pk=pk)
	if (task_to_update.task_creator)==request.user:
		form=Task_Category_Form(request.POST or None, instance=task_to_update)
		form.fields["task_category"].queryset=MainCategory.objects.filter(category_creator=request.user)
		id=task_to_update.task_category.pk
		if form.is_valid():
			form.save()
			return redirect("/category/details/"+str(id))
		context={'form':form}
		return render(request,'notebook/taskupdate.html',context)
	return HttpResponse("Access Denied")
@login_required
def Category_Update(request,pk):
	category_to_update=MainCategory.objects.get(pk=pk)
	if category_to_update.category_creator==request.user:
		form=CategoryForm(request.POST or None,instance=category_to_update)
		if form.is_valid():
			form.save()
			return redirect("/profile")	
		context={'form':form}
		return render(request,'notebook/categoryupdate.html',context)
	return HttpResponse("Access Denied")
@login_required
def Category_Delete(request,pk):
	category_to_delete=MainCategory.objects.get(pk=pk)
	if category_to_delete.category_creator==request.user:
			category_to_delete.delete()
			return redirect("/profile")	
		
	return HttpResponse("Access Denied")

@login_required
def Delete_Completed(request,pk):
	MainCategory_Object=MainCategory.objects.get(pk=pk)
	if MainCategory_Object.category_creator==request.user:
		MainCategory_Object.tasks_set.filter(task_status=True).delete()
		return redirect("/profile")
	return HttpResponse("Access Denied")

@login_required
def home(request):
	nav=MainCategory.objects.filter(category_creator=request.user).all()
	tasks=Tasks.objects.filter(task_creator=request.user).filter(task_status=False).order_by('task_priority')
	context={'tasks':tasks,'nav':nav}
	return render(request,'notebook/home.html',context)
def index(request):
	return render(request,'notebook/index.html')
@login_required
def CategoryDetails(request,pk):
	MainCategory_Object=MainCategory.objects.get(pk=pk)
	if MainCategory_Object.category_creator==request.user:
		tasks=MainCategory_Object.tasks_set.filter(task_creator=request.user).order_by('task_status','task_priority')
		if request.method=='POST':
			print("Inside Form")
			form=TaskForm(request.POST)
			form.instance.task_creator=request.user
			form.instance.task_category=MainCategory_Object
			if form.is_valid():
				form.save()	
		form=TaskForm()	
		nav=MainCategory.objects.filter(category_creator=request.user).all()
		context={'tasks':tasks,'nav':nav,'form':form,'category':MainCategory_Object}
		return render(request,'notebook/categorydetails.html',context)
	return HttpResponse("Access Denied")

@login_required
def Task_Delete(request,pk):
	task_to_del=Tasks.objects.get(pk=pk)
	print(request.user)
	print(task_to_del.task_category.category_creator)
	if (task_to_del.task_creator)==request.user:
		id=task_to_del.task_category.pk
		task_to_del.delete()
		return redirect("/category/details/"+str(id))
	return HttpResponse("Access Denied")

@login_required
def TaskComplete(request,pk):
	completed_task_object=Tasks.objects.get(pk=pk)
	if completed_task_object.task_creator==request.user:
		if completed_task_object.task_status==True:
			completed_task_object.task_status=False
		else:
			completed_task_object.task_status=True
		completed_task_object.save()
		cat_id=completed_task_object.task_category.pk
		return redirect('category-details',pk=cat_id)
	return HttpResponse("Access Denied")

@login_required
def profile(request):
	nav=MainCategory.objects.filter(category_creator=request.user).all()
	context={'nav':nav}
	return render(request,'notebook/profile.html',context)

@login_required
def CategoryChange(request,pk,id):
	task = Tasks.objects.get(pk=pk)
	category = MainCategory.objects.get(pk=id)
	task.task_category = category
	task.save()
	return HttpResponse("Category Changed")









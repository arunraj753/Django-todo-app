from django.urls import path
from .import views

urlpatterns=[
path('',views.index,name='index'),
path('task/create',views.Task_Create,name='create_task'),
path('home',views.home,name='home'),
path('category/create',views.Category_Create,name='create_category'),
path('category/update/<int:pk>',views.Category_Update,name='category-update'),
path('category/details/<int:pk>',views.CategoryDetails,name='category-details'),
path('category/delete/<int:pk>',views.Category_Delete,name='category-delete'),
path('tasks/update/<int:pk>',views.Task_Update,name='task-update'),
path('tasks/delete/<int:pk>',views.Task_Delete,name='task-delete'),
path('tasks/complete/<int:pk>',views.TaskComplete,name='task-complete'),
path('profile',views.profile,name='profile'),
path('category/deletecompleted/<int:pk>',views.Delete_Completed,name='delete-completed'),
]

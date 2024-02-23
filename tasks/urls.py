from django.urls import path
from .import views
from .views import TaskListCreate, TaskRetrieveUpdateDestroy

urlpatterns = [
    path('', views.homepage, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('products/', views.product_list, name='product_list'),
    path('api/Task/', TaskListCreate.as_view(), name='task-list-create'),
    path('api/Task/<int:pk>/', TaskRetrieveUpdateDestroy.as_view(), name='task-retrieve-update-destroy'),
]


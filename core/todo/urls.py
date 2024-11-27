from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='home'),
    path('create/', views.TaskCreateView.as_view(), name='create'),
    path('status/<int:pk>/', views.TaskStatusUpdateView.as_view(), name='status'),
    path('Delete/<int:pk>/', views.TaskDeleteView.as_view(), name='delete'),
    path('Update/<int:pk>/', views.TaskUpdateView.as_view(), name='update'),
]

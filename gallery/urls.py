from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project/<str:project_name>/', views.project_view, name='project_view'),
]

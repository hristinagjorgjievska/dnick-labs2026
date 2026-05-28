from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('trainings/add/', views.add_training, name='add_training')
]
from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('list/', views.list, name='list'),
    path('add/', views.add.list, name='add'),
    path('delete/', views.delete.list, name='delete'),
]

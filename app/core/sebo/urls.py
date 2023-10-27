from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('disk/<int:pk>', disk, name='disk'),
    path('disk/create/', disk_create, name='disk_create'),
    path('disk/edit/<int:pk>', disk_edit, name='disk_edit'),
    path('disk/delete/<int:pk>', disk_delete, name='disk_delete'),
]
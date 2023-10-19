from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('disk/<int:pk>', disk, name='disk'),
]
from django.urls import re_path
from django.urls import path
from .views import generate_teachers, create_teacher, get_teachers

app_name = 'teachers'

urlpatterns = [
    re_path('generate_teachers/', generate_teachers, name='generate'),
    path('', get_teachers, name='list'),
    path('create/', create_teacher, name='create'),
]

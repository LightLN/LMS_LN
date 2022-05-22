from django.urls import re_path
from . import views


urlpatterns = [
    re_path('generate_teachers/', views.generate_teachers, name='generate'),
]

from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio),
    path('cursos', cursos, name="Cursos"),
    path('profesores', profesores, name="Profesores"),
    path('estudiantes', estudiantes, name="Estudiantes"),
    path('entregables', entregables, name="Entregables"),
]
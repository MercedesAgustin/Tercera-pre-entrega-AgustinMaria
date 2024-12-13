
from django.urls import path
from app import views

urlpatterns = [
    path("", views.inicio, name="Inicio"),
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('poesia', views.poesia, name="Poesia"),
]

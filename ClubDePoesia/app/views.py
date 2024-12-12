from django.shortcuts import render
from django.http import HttpResponse

def inicio(request) :
    return render (request, "app/inicio.html")

def cursos(request) :
    return render (request, "app/cursos.html")

def profesores(request) :
    return render (request, "app/profesores.html")

def estudiantes(request) :
    return render (request, "app/estudiantes.html")

def poesia(request) :
    return render (request, "app/poesia.html")
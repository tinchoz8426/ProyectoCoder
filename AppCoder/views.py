from django.shortcuts import render

from AppCoder.models import Curso

# Create your views here.
def inicio(request):

    return render(request, "AppCoder/index.html")


def cursos(request):

    cursos = Curso.objects.all()
    print(cursos)

    return render(request, "AppCoder/cursos.html", {"cursos":cursos})


def profesores(request):

    return render(request, "AppCoder/profesores.html")


def estudiantes(request):

    return render(request, "AppCoder/estudiantes.html")


def entregables(request):

    return render(request, "AppCoder/entregables.html")

from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse
from inicio.models import Curso

# Create your views here.
def inicio(request):
    archivo = open(r'inicio\templates\inicio\inicio.html', 'r')
    template = Template(archivo.read())
    archivo.close()
    contexto = Context()
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)

def crear_curso(request, titulo, numero):
    curso = Curso(titulo=titulo,numero=numero)
    curso.save()
    return render(request, r'inicio/curso.html',{})
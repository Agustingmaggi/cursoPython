from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):

    archivo = open(r'C:\Coding\ch\python\cursoRevision\Proyecto1\Proyecto1\templates\vista1.html')
    template = Template(archivo.read())
    archivo.close()
    contexto = Context()
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)

def dia(request):
    dia = datetime.datetime.now()
    documentoDeTexto = f"Hoy es dia: {dia}"
    return HttpResponse(documentoDeTexto)
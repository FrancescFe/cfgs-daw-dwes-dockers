from html import escape
from django.http import HttpResponse

def saludo(request):
    nombre = request.GET.get("nombre", "Invitado")
    return HttpResponse('<!doctype html><html lang="es"><meta charset="utf-8"><h1>Django funciona</h1><p>Hola, ' + escape(nombre) + '.</p></html>')

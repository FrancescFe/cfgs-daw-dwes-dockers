"""Prueba WSGI pura y aplicación Django, servidas por el mismo Gunicorn."""
import os
from html import escape
from urllib.parse import parse_qs
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django_application = get_wsgi_application()

def application(environ, start_response):
    if environ.get("PATH_INFO") == "/prueba-wsgi/":
        nombre = parse_qs(environ.get("QUERY_STRING", "")).get("nombre", ["Invitado"])[0]
        contenido = ('<!doctype html><html lang="es"><meta charset="utf-8"><h1>WSGI funciona</h1><p>Hola, ' + escape(nombre) + '.</p></html>').encode("utf-8")
        start_response("200 OK", [("Content-Type", "text/html; charset=utf-8"), ("Content-Length", str(len(contenido)))])
        return [contenido]
    return django_application(environ, start_response)

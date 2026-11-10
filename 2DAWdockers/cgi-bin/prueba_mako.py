#!/usr/bin/env python3
import os
from urllib.parse import parse_qs
from mako.template import Template
nombre = parse_qs(os.environ.get("QUERY_STRING", "")).get("nombre", ["Invitado"])[0]
plantilla = Template(filename="/app/templatesMako/prueba_saludo.mako", input_encoding="utf-8")
print("Content-Type: text/html; charset=utf-8")
print()
print(plantilla.render(nombre=nombre))

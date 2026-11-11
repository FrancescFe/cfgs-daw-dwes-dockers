#!/usr/bin/env python3

import os
import sys
from urllib.parse import parse_qs

from mako import exceptions
from mako.template import Template

metodo = os.environ.get("REQUEST_METHOD", "")
error = ""
numero = None

if metodo == "GET":
    consulta = os.environ.get("QUERY_STRING", "")
    parametros = parse_qs(consulta, keep_blank_values=True)
else:
    parametros = {}
    error = "Método no admitido. Vuelve a abrir el formulario."

if metodo == "GET":
    numero_texto = parametros.get("numero", [""])[0].strip()

    try:
        numero = int(numero_texto)
    except ValueError:
        numero = None
        error = "Introduce un número entero válido."

try:
    plantilla = Template(
        filename="/app/templatesMako/01_tabla_multiplicar.mako",
        input_encoding="utf-8",
        default_filters=["h"],
    )

    html = plantilla.render(
        numero=numero,
        error=error,
    )
except Exception:
    detalle = exceptions.text_error_template().render()
    print(detalle, file=sys.stderr)

    print("Content-Type: text/plain; charset=utf-8")
    print()
    print("Error al generar la página. Consulta los registros del servidor.")

else:
    print("Content-Type: text/html; charset=utf-8")
    print()
    print(html)
#!/usr/bin/env python3

import sys

from mako import exceptions
from mako.template import Template

try:
    plantilla = Template(
        filename="/app/templatesMako/01_tablas_multiplicar_ampliacion.mako",
        input_encoding="utf-8",
        default_filters=["h"],
    )

    html = plantilla.render()

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
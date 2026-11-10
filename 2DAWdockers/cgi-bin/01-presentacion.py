#!/usr/bin/env python3

import os
import sys
from urllib.parse import parse_qs
from html import escape

metodo = os.environ.get("REQUEST_METHOD", "GET")

print("Content-type: text/html; charset=utf-8")
print()
print("""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <title>Presentación</title>
</head>
<body>""")

if metodo == "GET":
    print("<h1>Formulario de presentación</h1>")
    print('<form action="" method="post" accept-charset="UTF-8">')
    print('<p><label for="nombre">Nombre:</label> '
          '<input type="text" id="nombre" name="nombre" required></p>')
    print('<p><label for="edad">Edad:</label> '
          '<input type="number" id="edad" name="edad" '
          'min="0" step="1" required></p>')
    print('<p><label for="localidad">Localidad:</label> '
          '<input type="text" id="localidad" name="localidad" required></p>')
    print('<p><label for="aficion">Afición:</label> '
          '<input type="text" id="aficion" name="aficion" required></p>')
    print('<button type="submit">Enviar</button>')
    print("</form>")

elif metodo == "POST":
    longitud = int(os.environ.get("CONTENT_LENGTH", "0") or "0")
    cuerpo_bytes = sys.stdin.buffer.read(longitud)
    cuerpo = cuerpo_bytes.decode("utf-8")
    parametros = parse_qs(cuerpo, keep_blank_values=True)

    nombre = parametros.get("nombre", [""])[0].strip()
    edad_texto = parametros.get("edad", [""])[0].strip()
    localidad = parametros.get("localidad", [""])[0].strip()
    aficion = parametros.get("aficion", [""])[0].strip()

    try:
        edad = int(edad_texto)
        edad_valida = edad >= 0
    except ValueError:
        edad = 0
        edad_valida = False

    datos_validos = bool(
        nombre and localidad and aficion and edad_valida
    )

    if datos_validos:
        nombre_html = escape(nombre)
        localidad_html = escape(localidad)
        aficion_html = escape(aficion)

        print(f"<h1>¡Hola, {nombre_html}!</h1>")
        print(
            f"<p>Me llamo {nombre_html}, tengo {edad} años, "
            f"vivo en {localidad_html} y mi afición es {aficion_html}.</p>"
        )


    else:
        print("<h1>No se pudo generar la presentación</h1>")
        print("<p>Completa todos los campos y escribe una edad entera "
              "igual o mayor que cero.</p>")
        print('<p><a href="">Volver al formulario</a></p>')

else:
    print("<h1>Método no admitido</h1>")
    print("<p>Abre el formulario y vuelve a enviarlo.</p>")
    print('<p><a href="">Volver al formulario</a></p>')

print("""</body>
</html>""")
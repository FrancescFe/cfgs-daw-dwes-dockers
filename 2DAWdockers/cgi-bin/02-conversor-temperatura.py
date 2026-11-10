#!/usr/bin/env python3

import math
import os
import sys
from urllib.parse import parse_qs

metodo = os.environ.get("REQUEST_METHOD", "GET")

print("Content-Type: text/html; charset=utf-8")
print()
print("""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <title>Conversor de temperaturas</title>
</head>
<body>""")

if metodo == "GET":
    print("<h1>Conversor de temperaturas</h1>")
    print('<form action="" method="post" accept-charset="UTF-8">')

    print('<p><label for="temperatura">Temperatura:</label> '
          '<input type="number" id="temperatura" name="temperatura" '
          'step="any" required></p>')

    print('<p><label for="conversion">Tipo de conversión:</label> '
          '<select id="conversion" name="conversion" required>')
    print('<option value="" selected disabled>Elige una conversión</option>')
    print('<option value="celsius_fahrenheit">Celsius a Fahrenheit</option>')
    print('<option value="fahrenheit_celsius">Fahrenheit a Celsius</option>')
    print('</select></p>')

    print('<button type="submit">Convertir</button>')

    print("</form>")

elif metodo == "POST":
    longitud = int(os.environ.get("CONTENT_LENGTH", "0") or "0")
    cuerpo_bytes = sys.stdin.buffer.read(longitud)
    cuerpo = cuerpo_bytes.decode("utf-8")
    parametros = parse_qs(cuerpo, keep_blank_values=True)

    temperatura_texto = parametros.get("temperatura", [""])[0].strip()
    conversion = parametros.get("conversion", [""])[0].strip()

    try:
        temperatura = float(temperatura_texto)
        temperatura_valida = math.isfinite(temperatura)
    except ValueError:
        temperatura = 0.0
        temperatura_valida = False

    conversion_valida = conversion in (
        "celsius_fahrenheit",
        "fahrenheit_celsius",
    )

    datos_validos = temperatura_valida and conversion_valida

    if datos_validos:
        if conversion == "celsius_fahrenheit":
            resultado = temperatura * 9 / 5 + 32
            unidad_origen = "°C"
            unidad_destino = "°F"
            tipo_conversion = "Celsius a Fahrenheit"
        else:
            resultado = (temperatura - 32) * 5 / 9
            unidad_origen = "°F"
            unidad_destino = "°C"
            tipo_conversion = "Fahrenheit a Celsius"

        print("<h1>Resultado de la conversión</h1>")
        print(f"<p>Temperatura original: {temperatura} {unidad_origen}</p>")
        print(f"<p>Tipo de conversión: {tipo_conversion}</p>")
        print(f"<p>Resultado: {resultado:.2f} {unidad_destino}</p>")

    else:
        print("<h1>No se pudo realizar la conversión</h1>")
        print("<p>Introduce una temperatura numérica finita y elige "
              "una conversión válida.</p>")
        print('<p><a href="">Volver al formulario</a></p>')

else:
    print("<h1>Método no admitido</h1>")
    print("<p>Abre el formulario y vuelve a enviarlo.</p>")
    print('<p><a href="">Volver al formulario</a></p>')

print("""</body>
</html>""")
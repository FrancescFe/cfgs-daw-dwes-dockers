#!/usr/bin/env python3

import os
from urllib.parse import parse_qs
from html import escape

# 1. Recuperamos la cadena de parámetros
query = os.environ.get("QUERY_STRING", "")

# 2. Interpretamos los parámetros
parametros = parse_qs(query)

# 3. Obtenemos el nombre
nombre = parametros.get("nombre", ["Invitado"])[0]

# 4. Generamos las cabeceras de la respuesta CGI
print("Content-Type: text/html; charset=utf-8")
print()

# 5. Generamos el contenido HTML
print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print('<meta charset="UTF-8">')
print("<title>Mi primer CGI</title>")
print("</head>")

print("<body>")

print("<h1>Mi primer programa CGI con Docker</h1>")

print(f"<p>Bienvenido, {escape(nombre)}</p>")

print("</body>")
print("</html>")
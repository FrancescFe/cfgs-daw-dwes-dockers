# Cabecera HTTP
print("Content-Type: text/html; charset=utf-8")
print()

# Documento HTML
print("<!DOCTYPE html>")
print('<html lang="es">')
print("<head>")
print('    <meta charset="UTF-8">')
print("    <title>Mi página web</title>")
print("</head>")
print("<body>")

# Contenido dinámico de la página
print("    <h1>Mi primera página CGI</h1>")
print("    <p>Contenido generado desde Python</p>")

# Cierre del documento
print("</body>")
print("</html>")
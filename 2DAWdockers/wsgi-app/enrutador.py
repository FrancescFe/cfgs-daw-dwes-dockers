
#from calculadora import contenido as contenido_calculadora

from carteles_objetos_perdidos import contenido as contenido_carteles

def application(environ, start_response):
    # Rutas disponibles: añadir una entrada por cada ejercicio.
    rutas = {
        "/carteles": contenido_carteles,
   # "/calculadora": contenido_calculadora
}
    ruta: str = environ.get("PATH_INFO", "/")
    estado: str = "200 OK"
    contenido: str

    if ruta in ("/", "/prueba"):
        contenido = "<h1>El servicio WSGI funciona correctamente</h1>"
    elif ruta in rutas:
        contenido = rutas[ruta](environ)
    else:
        estado = "404 Not Found"
        contenido = "<h1>No existe esa ruta</h1>"

    html: str = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Pruebas WSGI</title>
</head>
<body>
    {contenido}
</body>
</html>"""
    respuesta: bytes = html.encode("utf-8")

    start_response(
        estado,
        [
            ("Content-Type", "text/html; charset=utf-8"),
            ("Content-Length", str(len(respuesta)))
        ]
    )

    return [respuesta]

#docker compose logs --tail=50 wsgi  #lista 50 últimos errores  
#docker compose logs --tail=1m wsgi  #lista errores  ultimo minuto
#docker compose logs -f wsgi #Visualizar en terminal lo que se imprime por medio de print


from urllib.parse import parse_qs
from html import escape

def contenido(environ) -> str:
    longitud = int(environ.get("CONTENT_LENGTH", "") or "0")
    cuerpo: str = environ["wsgi.input"].read(longitud).decode("utf-8")
    parametros: dict[str, list[str]] = parse_qs(
        cuerpo,
        keep_blank_values=True
    )

    nombre: str = parametros.get("nombre", [""])[0].strip()
    nota_texto = parametros.get("nota", [""])[0].strip()

    if not nombre:
        return """
            <h1>Datos incorrectos</h1>
            <p>El nombre es obligatorio.</p>
            <p>
                <a href="http://localhost:8080/forms/02_clasificacion_notas.html">
                    Volver al formulario
                </a>
            </p>
            """

    try:
        nota = float(nota_texto)
    except ValueError:
        return """
            <h1>Nota no válida</h1>
            <p>Introduce una nota numérica entre 0 y 10.</p>
            <p>
                <a href="http://localhost:8080/forms/02_clasificacion_notas.html">
                    Volver al formulario
                </a>
            </p>
            """

    if not 0 <= nota <= 10:
        return """
            <h1>Nota fuera de rango</h1>
            <p>La nota debe estar entre 0 y 10.</p>
            <p>
                <a href="http://localhost:8080/forms/02_clasificacion_notas.html">
                    Volver al formulario
                </a>
            </p>
            """

    if nota >= 5:
        resultado = "Aprueba"
    else:
        resultado = "Suspende"

    if nota < 5:
        clasificacion = "Insuficiente"
    elif nota < 6:
        clasificacion = "Suficiente"
    elif nota < 7:
        clasificacion = "Bien"
    elif nota < 9:
        clasificacion = "Notable"
    else:
        clasificacion = "Sobresaliente"

    return f"""
    <h1>Resultado de la evaluación</h1>
    <p>Nombre: {escape(nombre)}</p>
    <p>Nota: {nota}</p>
    <p>Resultado: {resultado}</p>
    <p>Clasificación: {clasificacion}</p>
    <p>
        <a href="http://localhost:8080/forms/02_clasificacion_notas.html">
            Volver al formulario
        </a>
    </p>
    """
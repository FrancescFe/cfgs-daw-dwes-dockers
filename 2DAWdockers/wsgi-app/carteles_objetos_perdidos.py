from urllib.parse import parse_qs
from html import escape

def contenido(environ) -> str:
    query_string = environ.get("QUERY_STRING", "")
    parametros = parse_qs(query_string, keep_blank_values=True)

    objeto = parametros.get("objeto", [""])[0]
    descripcion = parametros.get("descripcion", [""])[0]
    lugar = parametros.get("lugar", [""])[0]
    correo = parametros.get("correo", [""])[0]
    tipo_aviso = parametros.get("tipo_aviso", [""])[0]


    if (
        not objeto.strip()
        or not descripcion.strip()
        or not lugar.strip()
        or not correo.strip()
        or not tipo_aviso.strip()
    ):
        return """
        <h1>Faltan datos</h1>
        <p>Completa todos los campos del formulario.</p>
        <p>
            <a href="http://localhost:8080/forms/01_carteles_objetos_perdidos.html">
                Volver al formulario
            </a>
        </p>
        """

    if tipo_aviso not in ("discreto", "destacado"):
        return """
        <h1>Tipo de aviso no válido</h1>
        <p>Selecciona «discreto» o «destacado».</p>
        <p>
            <a href="http://localhost:8080/forms/01_carteles_objetos_perdidos.html">
                Volver al formulario
            </a>
        </p>
        """

    cartel = f"""
    <section>
        <h1>OBJETO ENCONTRADO</h1>
        <p><strong>Objeto:</strong> {escape(objeto)}</p>
        <p><strong>Descripción:</strong> {escape(descripcion)}</p>
    """

    if tipo_aviso == "destacado":
        cartel += f"""
        <p><strong>Lugar donde se encontró:</strong> {escape(lugar)}</p>
        <p><strong>Correo de contacto:</strong> {escape(correo)}</p>
        """

    cartel += """
    <p>
        <a href="http://localhost:8080/forms/01_carteles_objetos_perdidos.html">
            Volver al formulario
        </a>
    </p>
    """

    return cartel
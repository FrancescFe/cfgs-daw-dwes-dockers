#shebang

#imports 
from mako import exceptions


#atributos del constructor del objeto Template 
#                     filename="/app/templatesMako/xxxxxx.mako",
#                     input_encoding="utf-8",
#                     default_filters=["h"])



#renderizar
    try:
        html=xxxx.render(
            #parametros
        
        )
    except Exception:
        print(exceptions.text_error_template().render(), file=sys.stderr)
        print("Content-Type: text/plain; charset=utf-8")
        print()
        print("Error al generar la página. Consulta los logs.")
        return

    #cabecera


# Para ver los 50 ultimos errores que captura la excepcion ejecutar en el terminal esta instrucción

# docker compose logs --tail=50 cgi 

#para ver los ultimos errores en tiempo real

# docker compose logs --tail=0 -f cgi

# En cada ejecución saldra una nueva cola de errores. Hay que buscar los últimos para ver en que linea del codigo mako tienes un error
# Partimos de una imagen que ya incluye Python
FROM python:3.13-slim

# Instalamos fcgiwrap
RUN apt-get update && \
    apt-get install -y --no-install-recommends fcgiwrap && \
    rm -rf /var/lib/apt/lists/*

#instalamos  mako para poder usar código encriptado
RUN pip install mako

# Creamos el directorio para nuestros programas CGI
WORKDIR /app

# Copiamos los programas Python al contenedor
COPY cgi-bin/ /app/cgi-bin/

# Corregimos posibles finales de línea de Windows
# y concedemos permisos de ejecución
RUN sed -i 's/\r$//' /app/cgi-bin/*.py && \
    chmod 755 /app/cgi-bin/*.py

# Ejecutamos fcgiwrap como usuario no privilegiado
USER www-data

# Puerto de comunicación FastCGI
EXPOSE 9000

# Arrancamos fcgiwrap escuchando peticiones TCP
CMD ["/usr/sbin/fcgiwrap", "-s", "tcp:0.0.0.0:9000"]


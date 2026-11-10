
from django.shortcuts import render
def comprobar_paridad(request):
    resultado = None
    error = None
    if request.method == "POST":
        texto_numero = request.POST.get("numero", "")

        try:
            numero = int(texto_numero)

            if numero % 2 == 0:
                resultado = f"El número {numero} es par."
            else:
                resultado = f"El número {numero} es impar."

        except ValueError:
            error = "Debes introducir un número entero válido."

    return render(
        request,
        "paridad/formulario.html",
        {
            "resultado": resultado,
            "error": error,
        },
    )

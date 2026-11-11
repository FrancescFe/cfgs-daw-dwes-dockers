<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Tabla de multiplicar</title>
    <style>
        tbody tr.impar {
            background-color: #f2f2f2;
        }

        tbody tr.par {
            background-color: #dbeafe;
        }
    </style>
</head>
<body>
    <h1>Tabla de multiplicar</h1>

    % if error:
        <p class="error">${error}</p>
        <p><a href="/forms/01_tabla_multiplicar.html">Volver al formulario</a></p>
    % else:
        <table>
            <thead>
                <tr>
                    <th>Primer operando</th>
                    <th>Segundo operando</th>
                    <th>Resultado</th>
                </tr>
            </thead>
            <tbody>
                % for multiplicador in range(1, 11):
                    <tr class="${'par' if multiplicador % 2 == 0 else 'impar'}">
                        <td>${numero}</td>
                        <td>${multiplicador}</td>
                        <td>${numero * multiplicador}</td>
                    </tr>
                % endfor
            </tbody>
        </table>
    % endif
</body>
</html>
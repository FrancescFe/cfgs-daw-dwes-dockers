<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Tablas de multiplicar (ampliación)</title>
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
    <h1>Tablas de multiplicar (ampliación)</h1>

% for primer_operando in range(1, 11):
    <h2>Tabla del ${primer_operando}</h2>
    <table>
        <thead>
            <tr>
                <th>Primer operando</th>
                <th>Segundo operando</th>
                <th>Resultado</th>
            </tr>
        </thead>

        <tbody>
% for segundo_operando in range(1, 11):
            <tr class="${'par' if segundo_operando % 2 == 0 else 'impar'}">
                <td>${primer_operando}</td>
                <td>${segundo_operando}</td>
                <td>${primer_operando * segundo_operando}</td>
            </tr>
% endfor
        </tbody>
    </table>
% endfor
</body>
</html>
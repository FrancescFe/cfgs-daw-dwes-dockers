<%@ page contentType="text/html; charset=UTF-8" %>

<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <title>Primera JSP</title>
</head>

<body>

<%
    String nombre = "Felipe";
    int edad = 25;
%>

<h1>Hola, <%= nombre %></h1>

<p>Edad actual: <%= edad %></p>

<p>El año que viene tendrás <%= edad + 1 %> años.</p>

</body>

</html>
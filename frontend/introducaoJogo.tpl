<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Xtreme</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <h1 class="titulo">XTREME</h1>
    {{!# each resultados }}
    <div id="board">{{ this.tabuleiro }}</div>
    <p>Ganhador: {{ this.ganhador }}</p>
    {{!# end }}
    <a class="acesso" href="desktop_9.html">Visualizar histórico de placar</a>
</body>

<footer>
    <p>&copy; 2023 Trabalho final FGA0158. Todos os direitos reservados.</p>
</footer>

</html>

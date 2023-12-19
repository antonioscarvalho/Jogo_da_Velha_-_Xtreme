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
    <h2 class="frase">BEM-VINDO DE VOLTA AO DESAFIO!</h2>

    <form id="loginForm" action="/validar_usuario" method="POST">
        <label for="usuario">Usuário:</label>
        <input type="text" id="usuario" name="usuario" required>

        <label for="senha">Senha:</label>
        <input type="password" id="senha" name="senha" required>

        <button type="submit">ENTRAR</button>
    </form>

    <a class="acesso" href="desktop_3">Cadastrar</a>
</body>

<footer>
    <p>&copy; 2023 Trabalho final FGA0158. Todos os direitos reservados.</p>
</footer>

</html>
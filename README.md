# Jogo da Velha - Xtreme

## Projeto Final de Orientação a Objetos - UnB

## Apresentação do Projeto
[Apresentação do trabalho](https://www.youtube.com/watch?v=UDn3MKWBs7w)

### Descrição

Este projeto consiste em um jogo da velha implementado em Python, dividido em componentes de backend, banco de dados e frontend. A aplicação utiliza o framework Bottle para a parte web e os templates de Jinja2 para renderizar as páginas HTML.

### Objetivo

- **Jogo da Velha Interativo:** Os jogadores podem jogar o clássico jogo da velha contra um oponente inteligente chamado "Xtreme".

- **IA Xtreme:** A inteligência artificial "Xtreme" é implementada para proporcionar um desafio ao jogador. Ela faz escolhas estratégicas para tentar vencer ou bloquear o jogador humano.

- **Persistência de Dados:** O estado do jogo é salvo em um banco de dados JSON, permitindo que os jogadores continuem o jogo depois de fechar e reabrir a aplicação.

### Estrutura do Projeto

O projeto está dividido em três principais componentes:

1. **Backend:**
   - Implementa a lógica do jogo, a IA "Xtreme" e a interação com o banco de dados.
   - Utiliza o framework Bottle para roteamento web.

2. **Banco de Dados:**
   - Os dados do jogo são armazenados em um arquivo JSON.
   - A persistência de dados é gerenciada pelo componente de backend.

3. **Frontend:**
   - As páginas web são renderizadas usando templates Jinja2.
   - Interface simples para o jogador interagir com o jogo.

### Conclusão do Projeto

O projeto foi concluído, alcançando as seguintes etapas:

- **HTML e CSS Funcionais:** As páginas web foram desenvolvidas com HTML e CSS, proporcionando uma interface amigável, embora a lógica do jogo ainda não esteja implementada.

- **Banco de Dados Independente:** O banco de dados foi implementado e realiza o cadastro por meio do `app.py` e `desktop_3.tpl`.

- **Jogo em Python no Terminal:** A lógica do jogo está funcional no terminal, permitindo a interação do jogador com o jogo.

- **Rotas no app.py:** As rotas no `app.py` estão configuradas, mas a implementação do jogo web e a verificação do usuário ainda não funcionam.

### Instalação e Execução

1. **Instalar Dependências:**
   ```bash
   pip install bottle
   ```

2. **Executar o Aplicativo:**
   ```bash
   python app.py
   ```
   O servidor web será iniciado, e a aplicação estará acessível em `http://localhost:8080`.

### Como Jogar

1. Acesse a aplicação no navegador.
2. Escolha entre jogar contra a IA "Xtreme" ou com outro jogador.
3. Faça suas jogadas clicando nas células do tabuleiro.
4. A IA "Xtreme" responderá automaticamente.
5. Continue o jogo ou reinicie conforme desejar.

## Autores

- [Antônio Amadeu de Sousa Carvalho](https://github.com/antonioscarvalho)
  - Matrícula: 222006552

- [Bruno de Oliveira](https://github.com/BrunoOLiveirax)
  - Matrícula: 180062778

- [Jéssica Eveline Saraiva Araújo](https://github.com/xzxjesse)
  - Matrícula: 221022319

# Jogo da Velha - Xtreme

##Projeto Final de Orientação a Objetos-UnB

## Descrição

Este projeto é um jogo da velha implementado em Python, dividido em componentes de backend, banco de dados e frontend. A aplicação utiliza o framework Bottle para a parte web e os templates de Jinja2 para renderizar as páginas HTML.

## Funcionalidades

- **Jogo da Velha Interativo:** Os jogadores podem jogar o clássico jogo da velha contra um oponente inteligente chamado "Xtreme".
  
- **IA Xtreme:** A inteligência artificial "Xtreme" é implementada para proporcionar um desafio ao jogador. Ela faz escolhas estratégicas para tentar vencer ou bloquear o jogador humano.

- **Persistência de Dados:** O estado do jogo é salvo em um banco de dados JSON, permitindo que os jogadores continuem o jogo depois de fechar e reabrir a aplicação.

## Estrutura do Projeto

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

## Instalação e Execução

1. **Instalar Dependências:**
   ```bash
   pip install bottle
   ```

2. **Executar o Aplicativo:**
   ```bash
   python main.py
   ```
   O servidor web será iniciado e a aplicação estará acessível em `http://localhost:8080`.

## Como Jogar

1. Acesse a aplicação no navegador.
2. Escolha entre jogar contra a IA "Xtreme" ou com outro jogador.
3. Faça suas jogadas clicando nas células do tabuleiro.
4. A IA "Xtreme" responderá automaticamente.
5. Continue o jogo ou reinicie conforme desejar.

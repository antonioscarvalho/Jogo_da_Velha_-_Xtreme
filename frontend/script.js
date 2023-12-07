document.addEventListener('DOMContentLoaded', function () {
    const board = document.getElementById('board');
    let currentPlayer = 'X';
    let gameBoard = ['', '', '', '', '', '', '', '', ''];

    function renderBoard() {
        board.innerHTML = '';
        gameBoard.forEach((cell, index) => {
            const cellElement = document.createElement('div');
            cellElement.classList.add('cell');
            cellElement.textContent = cell;
            cellElement.addEventListener('click', () => handleCellClick(index));
            board.appendChild(cellElement);
        });
    }

    function handleCellClick(index) {
        if (gameBoard[index] === '' && !checkWinner()) {
            gameBoard[index] = currentPlayer;
            currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
            renderBoard();

            if (checkWinner()) {
                alert(`Player ${currentPlayer === 'X' ? 'O' : 'X'} wins!`);
                resetGame();
            } else if (!gameBoard.includes('')) {
                alert('It\'s a draw!');
                resetGame();
            }
        }
    }

    function checkWinner() {
        const winPatterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
            [0, 4, 8], [2, 4, 6]             // Diagonals
        ];

        return winPatterns.some(pattern =>
            gameBoard[pattern[0]] !== '' &&
            gameBoard[pattern[0]] === gameBoard[pattern[1]] &&
            gameBoard[pattern[1]] === gameBoard[pattern[2]]
        );
    }

    function resetGame() {
        currentPlayer = 'X';
        gameBoard = ['', '', '', '', '', '', '', '', ''];
        renderBoard();
    }

    // Função para iniciar o jogo após o envio do formulário
    window.startGame = function () {
        // Aqui você pode adicionar lógica para verificar os dados do formulário
        const usuario = document.getElementById('usuario').value;
        const senha = document.getElementById('senha').value;

        // Verificação simples, substitua por uma lógica mais robusta no ambiente de produção
        if (usuario === 'seuUsuario' && senha === 'suaSenha') {
            // Redirecionar para a página desktop_4.html
            window.location.href = 'desktop_4.html';
        } else {
            alert('Usuário ou senha inválidos. Tente novamente.');
        }
    };

    renderBoard();
});

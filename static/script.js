// Function to display the chessboard on the web interface
function displayChessboard(chessboardState) {
    const chessboardDiv = document.querySelector('.chessboard');
    chessboardDiv.innerHTML = '';

    for (let row = 0; row < 8; row++) {
        for (let col = 0; col < 8; col++) {
            const square = document.createElement('div');
            square.classList.add('square');

            // Set class for black or white square
            const squareColor = (row + col) % 2 === 0 ? 'white' : 'black';
            square.classList.add(squareColor);

            // Add the chess piece (Unicode symbol) to the square
            const piece = chessboardState[row][col];
            if (piece !== ' ') {
                square.textContent = piece;
            }

            chessboardDiv.appendChild(square);
        }
    }
}

// Function to fetch and display the chessboard
function fetchChessboard() {
    fetch('/get_chessboard')
        .then((response) => response.json())
        .then((data) => displayChessboard(data));
}

// Call the fetchChessboard function when the page loads
document.addEventListener('DOMContentLoaded', fetchChessboard);

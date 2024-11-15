let board = [];
let numMines = 0;

document.getElementById("start-game").addEventListener("click", async () => {
    const minesInput = document.getElementById("num-mines");
    numMines = parseInt(minesInput.value);

    if (numMines < 1 || numMines > 25 || isNaN(numMines)) {
        alert("Please enter a valid number between 1 and 25");
        return;
    }

    // Fetch board from the server
    const response = await fetch('/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ num_mines: numMines }),
    });

    const data = await response.json();
    board = data.board;
    renderBoard();
});

function renderBoard() {
    const container = document.getElementById("game-container");
    container.innerHTML = '';
    for (let i = 0; i < 5; i++) {
        for (let j = 0; j < 5; j++) {
            const cell = document.createElement("div");
            cell.className = "cell";
            cell.dataset.row = i;
            cell.dataset.col = j;
            cell.addEventListener("click", () => checkCell(i, j, cell));
            container.appendChild(cell);
        }
    }
}

async function checkCell(row, col, cell) {
    if (cell.classList.contains("clicked")) return;

    const response = await fetch('/check', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ board, row, col }),
    });

    const data = await response.json();

    if (data.status === 'game over') {
        alert("Game Over!");
        revealBoard();
    } else {
        cell.textContent = data.count;
        cell.classList.add("clicked");
    }
}

function revealBoard() {
    const cells = document.querySelectorAll(".cell");
    cells.forEach(cell => {
        const row = parseInt(cell.dataset.row);
        const col = parseInt(cell.dataset.col);
        cell.classList.add("clicked");
        if (board[row][col] === 1) {
            cell.textContent = "X";
            cell.classList.add("mine");
        }
    });
}

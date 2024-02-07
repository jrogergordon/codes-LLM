function solveNQueens(n) {
    const results = [];

    // Helper function to check if a queen can be placed at (row, col)
    function isSafe(board, row, col) {
        // Check row
        for (let i = 0; i < col; i++) {
            if (board[row][i] === 'Q') {
                return false;
            }
        }

        // Check upper diagonal
        for (let i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] === 'Q') {
                return false;
            }
        }

        // Check lower diagonal
        for (let i = row, j = col; i < n && j >= 0; i++, j--) {
            if (board[i][j] === 'Q') {
                return false;
            }
        }

        return true;
    }

    // Recursive backtracking function to place queens
    function backtrack(board, col) {
        if (col === n) {
            // Base case: all queens placed, add solution
            results.push(board.map(row => row.join('')));
            return;
        }

        for (let row = 0; row < n; row++) {
            if (isSafe(board, row, col)) {
                board[row][col] = 'Q'; // Place queen
                backtrack(board, col + 1); // Try placing next queen
                board[row][col] = '.'; // Backtrack
            }
        }
    }

    // Initialize empty board
    const board = Array.from({ length: n }, () => Array(n).fill('.'));
    backtrack(board, 0);
    return results;
}

const solutions = solveNQueens(4);
console.log(solutions);
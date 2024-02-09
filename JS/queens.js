function nQueensRooks(n) {
    const results = [];
    const board = Array(n).fill(null).map(() => Array(n).fill('.'));

    function isSafe(board, row, col, piece) {
        // Check row and column
        for (let i = 0; i < n; i++) {
            if (board[row][i] !== '.' || board[i][col] !== '.') {
                return false;
            }
        }

        // Check diagonals (only check for potential queens)
        for (let i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] === 'Q') {
                return false;
            }
            for (let i = row, j = col; j >= 0 && i < n; i++, j--) {
                if (board[i][j] === 'Q') {
                    return false;
                }
            }
        }

        return true;
    }

    function solveNQURUtil(board, col, pieceType) {
        if (col === n) {
            results.push(board.map(row => row.join('')));
            return;
        }

        for (let i = 0; i < n; i++) {
            if (isSafe(board, i, col, pieceType)) {
                board[i][col] = pieceType;

                // Alternate between 'Q' and 'R' for the next placement
                const nextPieceType = pieceType === 'Q' ? 'R' : 'Q';
                solveNQURUtil(board, col + 1, nextPieceType);

                board[i][col] = '.';
            }
        }
    }

    solveNQURUtil(board, 0, 'Q'); // Start with placing a queen 
    return results;
}
const solutions = nQueensRooks(4);
console.log(solutions);




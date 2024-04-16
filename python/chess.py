class ChessBoard:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        # Create an 8x8 board
        board = [[' ' for _ in range(8)] for _ in range(8)]

        # Populate the board with pieces
        for i in range(8):
            board[1][i] = '\u265F'  # Black pawns
            board[6][i] = '\u2659'  # White pawns

        return board

    def get_pawn_moves(self, x, y):
        """
        Returns a list of available moves for a pawn at position (x, y) on the board.

        Args:
            x: The x-coordinate of the pawn.
            y: The y-coordinate of the pawn.

        Returns:
            A list of tuples representing the available moves. Each tuple contains the x and y coordinates of the move.
        """
        moves = []

        # Check if the pawn is white or black
        if self.board[y][x] == '\u2659':  # White pawn
            # Check if the pawn can move forward one square
            if y > 0 and self.board[y-1][x] == ' ':
                moves.append((x, y-1))
            # Check if the pawn can move forward two squares (only from starting position)
            if y == 6 and self.board[5][x] == ' ' and self.board[4][x] == ' ':
                moves.append((x, 4))
            # Check if the pawn can capture diagonally
            if x > 0 and y > 0 and self.board[y-1][x-1] != ' ' and self.board[y-1][x-1].islower():
                moves.append((x-1, y-1))
            if x < 7 and y > 0 and self.board[y-1][x+1] != ' ' and self.board[y-1][x+1].islower():
                moves.append((x+1, y-1))

        elif self.board[y][x] == '\u265F':  # Black pawn
            # Check if the pawn can move forward one square
            if y < 7 and self.board[y+1][x] == ' ':
                moves.append((x, y+1))
            # Check if the pawn can move forward two squares (only from starting position)
            if y == 1 and self.board[2][x] == ' ' and self.board[3][x] == ' ':
                moves.append((x, 3))
            # Check if the pawn can capture diagonally
            if x > 0 and y < 7 and self.board[y+1][x-1] != ' ' and self.board[y+1][x-1].isupper():
                moves.append((x-1, y+1))
            if x < 7 and y < 7 and self.board[y+1][x+1] != ' ' and self.board[y+1][x+1].isupper():
                moves.append((x+1, y+1))

        return moves
    def display_board_and_collect_piece(self):
        # Display the board with digits along the x and y axis
        print('  0 1 2 3 4 5 6 7')
        for i in range(8):
            row = ' '.join(self.board[i])
            print(f'{i} {row}')

        # Collect a piece for movement
        while True:
            try:
                x = int(input('Enter the x-coordinate of the piece to move (0-7): '))
                y = int(input('Enter the y-coordinate of the piece to move (0-7): '))
                if 0 <= x <= 7 and 0 <= y <= 7:
                    return x, y
                else:
                    print('Invalid coordinates. Please enter a number between 0 and 7.')
            except ValueError:
                print('Invalid input. Please enter a number.')

board = ChessBoard
board.create_board(self)
board.display_board_and_collect_piece()
class ChessBoard:
    def __init__(self):
        self.board = self.create_board()
        self.whiteX, self.whiteY = 0, 4
        self.blackX, self.blackY = 7, 4
        self.blackCaptures = {}
        self.whiteCaptures= {}


    def create_board(self):
        # Create an 8x8 board
        board = [[' ' for _ in range(8)] for _ in range(8)]

        # Populate the board with pieces
        for i in range(8):
            board[1][i] = '\u265F'  # Black pawns
            board[6][i] = '\u2659'  # White pawns

        # Rooks
        board[0][0] = board[0][7] = '\u265C'
        board[7][0] = board[7][7] = '\u2656'

        # Knights
        board[0][1] = board[0][6] = '\u265E'
        board[7][1] = board[7][6] = '\u2658'

        # Bishops
        board[0][2] = board[0][5] = '\u265D'
        board[7][2] = board[7][5] = '\u2657'

        # Queens
        board[0][3] = '\u265B'
        board[7][3] = '\u2655'

        # Kings
        board[0][4] = '\u265A'
        board[7][4] = '\u2654'

        return board

    def collect_pawn_moves(self, x, y):
        moves = []
        piece = self.board[y][x]

        if piece in ['\u2659', '\u2658', '\u2657', '\u2656', '\u2655', '\u2654']:
            opponent_pieces = ['\u265F', '\u265C', '\u265E', '\u265D', '\u265B', '\u265A']
            forward_direction = 1 # white
        else:
            opponent_pieces = ['\u2659', '\u2658', '\u2657', '\u2656', '\u2655', '\u2654']
            forward_direction = -1 #black

        # Check if the pawn can move forward one square
        if 0 <= y + forward_direction < 8 and self.board[y + forward_direction][x] == ' ':
            moves.append((x, y + forward_direction))
        # Check if the pawn can move forward two squares (only from starting position)
        if (y == 6 and forward_direction == -1) or (y == 1 and forward_direction == 1):
            if self.board[y + forward_direction][x] == ' ' and self.board[y + 2 * forward_direction][x] == ' ':
                moves.append((x, y + 2 * forward_direction))
        # Check if the pawn can capture diagonally
        if x > 0 and 0 <= y + forward_direction < 8 and self.board[y + forward_direction][x - 1] in opponent_pieces:
            moves.append((x - 1, y + forward_direction))
        if x < 7 and 0 <= y + forward_direction < 8 and self.board[y + forward_direction][x + 1] in opponent_pieces:
            moves.append((x + 1, y + forward_direction))
        moves.sort()
        return moves


    def collect_knight_moves(self, x, y):
        possible_moves = []
        knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

        piece = self.board[y][x]

        # Check if the piece is white
        if piece in ['\u2658', '\u2657', '\u2656', '\u2655', '\u2654']:
            opponent_pieces = ['\u265F', '\u265C', '\u265E', '\u265D', '\u265B', '\u265A']
        else:
            opponent_pieces = ['\u2659', '\u2658', '\u2657', '\u2656', '\u2655', '\u2654']

        for dx, dy in knight_moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                if self.board[new_y][new_x] == ' ' or self.board[new_y][new_x] in opponent_pieces:
                    possible_moves.append((new_x, new_y))
        possible_moves.sort()
        return possible_moves
    
    def collect_rook_moves(self, x, y):
        possible_moves = []
        piece = self.board[y][x]

        # Check if the piece is a rook
        if piece not in ['\u2656', '\u265C']:
            return possible_moves

        # Check if the piece is white
        if piece == '\u2656':
            opponent_pieces = ['\u265F', '\u265C', '\u265E', '\u265D', '\u265B', '\u265A']
        else:
            opponent_pieces = ['\u2659', '\u2658', '\u2657', '\u2656', '\u2655', '\u2654']

        # Check up
        for i in range(y-1, -1, -1):
            # print(i, x)
            if self.board[i][x] == ' ':
                possible_moves.append((x, i))
            elif self.board[i][x] in opponent_pieces:
                possible_moves.append((x, i))
                break
            else:
                break

        # Check down
        for i in range(y+1, 8):
            # print(i, x)
            if self.board[i][x] == ' ':
                possible_moves.append((x, i))
            elif self.board[i][x] in opponent_pieces:
                possible_moves.append((x, i))
                break
            else:
                break

        # Check left
        for i in range(x-1, -1, -1):
            # print(y,i)
            if self.board[y][i] == ' ':
                possible_moves.append((i, y))
            elif self.board[y][i] in opponent_pieces:
                possible_moves.append((i, y))
                break
            else:
                break

        # Check right
        for i in range(x+1, 8):
            # print(y,i)
            if self.board[y][i] == ' ':
                possible_moves.append((i, y))
            elif self.board[y][i] in opponent_pieces:
                possible_moves.append((i, y))
                break
            else:
                break
        possible_moves.sort()
        return possible_moves

    def collect_bishop_moves(self, x, y):
        possible_moves = []
        piece = self.board[y][x]

        # Check if the piece is a bishop
        if piece not in ['\u2657', '\u265D']:
            return possible_moves

        # Check if the piece is white
        if piece == '\u2657':
            opponent_pieces = ['\u265F', '\u265C', '\u265E', '\u265D', '\u265B', '\u265A']
        else:
            opponent_pieces = ['\u2659', '\u2658', '\u2657', '\u2656', '\u2655', '\u2654']

        # Check up-left
        i, j = x-1, y-1
        while i >= 0 and j >= 0:
            if self.board[j][i] == ' ':
                possible_moves.append((i, j))
            elif self.board[j][i] in opponent_pieces:
                possible_moves.append((i, j))
                break
            else:
                break
            i -= 1
            j -= 1

        # Check up-right
        i, j = x+1, y-1
        while i < 8 and j >= 0:
            if self.board[j][i] == ' ':
                possible_moves.append((i, j))
            elif self.board[j][i] in opponent_pieces:
                possible_moves.append((i, j))
                break
            else:
                break
            i += 1
            j -= 1

        # Check down-left
        i, j = x-1, y+1
        while i >= 0 and j < 8:
            if self.board[j][i] == ' ':
                possible_moves.append((i, j))
            elif self.board[j][i] in opponent_pieces:
                possible_moves.append((i, j))
                break
            else:
                break
            i -= 1
            j += 1

        # Check down-right
        i, j = x+1, y+1
        while i < 8 and j < 8:
            if self.board[j][i] == ' ':
                possible_moves.append((i, j))
            elif self.board[j][i] in opponent_pieces:
                possible_moves.append((i, j))
                break
            else:
                break
            i += 1
            j += 1

        possible_moves.sort()  # Sort the possible moves
        return possible_moves
    
    def collect_queen_moves(self, x, y):
        moves = []
        piece = self.board[y][x]

        if piece in ['\u2659', '\u2658', '\u2657', '\u2656', '\u2655', '\u2654']:
            opponent_pieces = ['\u265F', '\u265C', '\u265E', '\u265D', '\u265B', '\u265A']
        else:
            opponent_pieces = ['\u2659', '\u2658', '\u2657', '\u2656', '\u2655', '\u2654']

        # Calculate moves in all 8 directions
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                if self.board[ny][nx] == ' ':  # Empty space
                    moves.append((nx, ny))
                elif self.board[ny][nx] in opponent_pieces:  # Enemy piece
                    moves.append((nx, ny))
                    break
                else:  # Friendly piece
                    break
                nx += dx
                ny += dy
        
        return moves

    def collect_king_moves(self, x, y):
        possible_moves = []
        piece = self.board[y][x]

        # Check if the piece is a king
        if piece not in ['\u2654', '\u265A']:
            return possible_moves

        # Check if the piece is white
        if piece == '\u2654':
            opponent_pieces = ['\u265F', '\u265C', '\u265E', '\u265D', '\u265B', '\u265A']
        else:
            opponent_pieces = ['\u2659', '\u2658', '\u2657', '\u2656', '\u2655', '\u2654']

        # Check all 8 directions
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if (dx, dy) != (0, 0) and 0 <= nx < 8 and 0 <= ny < 8:
                    if self.board[ny][nx] == ' ' or self.board[ny][nx] in opponent_pieces:
                        possible_moves.append((nx, ny))

        possible_moves.sort()
        return possible_moves

    def move_piece(self, start, end, moves):
        piece = self.board[start[1]][start[0]]
        if end not in moves:
            return False

        # Determine opponent pieces
        if piece in ['\u2659', '\u2658', '\u2657', '\u2656', '\u2655', '\u2654']:
            opponent_pieces = ['\u265F', '\u265C', '\u265E', '\u265D', '\u265B', '\u265A']
            capture = self.blackCaptures
        else:
            opponent_pieces = ['\u2659', '\u2658', '\u2657', '\u2656', '\u2655', '\u2654']
            capture = self.whiteCaptures

        # Check if it's a capture
        captured_piece = self.board[end[1]][end[0]]

        if captured_piece != " " and captured_piece in opponent_pieces:
            if capture.get(captured_piece) != None:
                capture[captured_piece] += 1
            else:
                capture[captured_piece] = 1

        # Move the piece
        self.board[end[1]][end[0]] = piece
        self.board[start[1]][start[0]] = ' '

        return True

    def is_king_in_check(self, king):
        if king == '\u2654':  # Black King
            x, y = self.blackX, self.blackY
            diagonal_enemy_pieces = ['\u265D', '\u265B']  # White Bishop and Queen
            straight_enemy_pieces = ['\u265C', '\u265B']  # White Rook and Queen
            pawn_enemy_piece = '\u265F'  # White Pawn
            horse_enemy_piece = '\u265E'  # White Knight
        elif king == '\u265A':  # White King
            x, y = self.whiteX, self.whiteY
            diagonal_enemy_pieces = ['\u2657', '\u2655']  # Black Bishop and Queen
            straight_enemy_pieces = ['\u2656', '\u2655']  # Black Rook and Queen
            pawn_enemy_piece = '\u2659'  # Black Pawn
            horse_enemy_piece = '\u2658'  # Black Knight
        else:
            raise ValueError("The piece at the given position is not a king.")

        knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        for move in knight_moves:
            new_x, new_y = x + move[0], y + move[1]
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                if self.board[new_y][new_x] == horse_enemy_piece:
                    return True

        pawn_moves = [(1, -1), (-1, -1)] if king == '\u2654' else [(-1, 1), (1, 1)]
        for move in pawn_moves:
            new_x, new_y = x + move[0], y + move[1]
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                # print(new_y, new_x)
                if self.board[new_y][new_x] == pawn_enemy_piece:
                    return True

        horizontal_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for move in horizontal_moves:
            new_x, new_y = x + move[0], y + move[1]
            while 0 <= new_x < 8 and 0 <= new_y < 8:
                if self.board[new_y][new_x] != ' ':
                    if self.board[new_y][new_x] in straight_enemy_pieces:
                        return True
                    break
                new_x += move[0]
                new_y += move[1]

        diagonal_moves = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        for move in diagonal_moves:
            new_x, new_y = x + move[0], y + move[1]
            while 0 <= new_x < 8 and 0 <= new_y < 8:
                if self.board[new_y][new_x] != ' ':
                    if self.board[new_y][new_x] in diagonal_enemy_pieces:
                        return True
                    break
                new_x += move[0]
                new_y += move[1]

        return False
    
    
    def clear_board(self):
        # Clear the board of all pieces
        for i in range(8):
            for j in range(8):
                self.board[i][j] = ' '
    
    def print_board(self):
        print("  ", end="")
        for i in range(8):
            print(i, end=" ")
        print()
        for i in range(8):
            print(i, end=" ")
            for j in range(8):
                print(self.board[i][j], end=" ")
            print()


# chess = ChessBoard()
# chess.clear_board()
# chess.board[1][1] = '\u2656'
# chess.board[3][1] = '\u265F'
# chess.print_board()
# moves = chess.collect_rook_moves(1, 1)
# chess.move_piece((1, 1), (1, 3), moves)
# chess.print_board()

import unittest
from chess import ChessBoard
from unittest.mock import patch

class TestChessBoard(unittest.TestCase):
    def setUp(self):
        self.board = ChessBoard()

    def test_white_pawn_no_pieces_in_front(self):
        self.board.clear_board()
        self.board.board[6][4] = '\u265F'  # Switched to white pawn
        moves = self.board.collect_pawn_moves(4, 6)
        moves.sort()
        expected_moves = [(4, 7)]
        expected_moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_white_pawn_piece_in_front(self):
        self.board.clear_board()        
        self.board.board[6][4] = '\u265F'  # Switched to white pawn
        self.board.board[7][4] = '\u2656'  # Switched to white rook
        moves = self.board.collect_pawn_moves(4, 6)
        moves.sort()
        self.assertEqual(moves, [])

    def test_white_pawn_diagonal_capture(self):
        self.board.clear_board()        
        self.board.board[6][4] = '\u265F'  # Switched to white pawn
        self.board.board[7][3] = '\u2659'  # Switched to black pawn
        moves = self.board.collect_pawn_moves(4, 6)
        moves.sort()
        expected_moves = [(3, 7), (4, 7)]  # Added move forward one square
        expected_moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_black_pawn_no_pieces_in_front(self):
        self.board.clear_board()        
        self.board.board[1][4] = '\u265F' 
        moves = self.board.collect_pawn_moves(4, 1)
        moves.sort()
        expected_moves = [(4, 2), (4, 3)] # Black pawn can move two squares from starting position
        expected_moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_black_pawn_piece_in_front(self):
        self.board.clear_board()        
        self.board.board[1][4] = '\u265F'
        self.board.board[2][4] = '\u2659'
        moves = self.board.collect_pawn_moves(4, 1)
        moves.sort()
        self.assertEqual(moves, []) # Black pawn is blocked by another piece

    def test_black_pawn_diagonal_capture(self):
        self.board.clear_board()
        self.board.board[1][4] = '\u265F'
        self.board.board[2][5] = '\u2659'
        moves = self.board.collect_pawn_moves(4, 1)
        moves.sort()
        expected_moves = [(4, 2), (4, 3), (5, 2)] # Black pawn can capture diagonally
        expected_moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_collect_knight_moves_white_knight(self):
        self.board.clear_board()
        self.board.board[0][0] = '\u2658'  # White knight
        moves = self.board.collect_knight_moves(0, 0)
        expected_moves = [(1, 2), (2, 1)]
        expected_moves.sort()
        moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_collect_knight_moves_white_knight_capture(self):
        self.board.clear_board()
        self.board.board[0][0] = '\u2658'  # White knight
        self.board.board[1][2] = '\u265F'  # Black pawn
        moves = self.board.collect_knight_moves(0, 0)
        expected_moves = [(1, 2), (2, 1)]
        expected_moves.sort()
        moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_collect_knight_moves_black_knight(self):
        self.board.clear_board()
        self.board.board[0][0] = '\u265E'  # Black knight
        moves = self.board.collect_knight_moves(0, 0)
        expected_moves = [(1, 2), (2, 1)]
        expected_moves.sort()
        moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_collect_knight_moves_black_knight_all_moves(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265E'  # Black knight
        moves = self.board.collect_knight_moves(4, 4)
        expected_moves = [(2,3), (2,5), (3,2), (3,6), (5,2), (5,6), (6,3), (6,5)]
        expected_moves.sort()
        moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_white_rook_blocked_moves(self):
        self.board.clear_board()
        self.board.board[0][0] = '\u265C'  # White rook
        moves = self.board.collect_rook_moves(0, 0)
        expected_moves = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
        expected_moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_white_rook_capture_moves(self):
        self.board.clear_board()
        self.board.board[0][0] = '\u265C'  # White rook
        moves = self.board.collect_rook_moves(0, 0)
        expected_moves = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), 
                          (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
        expected_moves.sort()
        moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_white_rook_open_moves(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265C'  # White rook
        moves = self.board.collect_rook_moves(4, 4)
        expected_moves = [(4, 3), (4, 2), (4, 1), (4,0), (4, 5), (4, 6), (4, 7), 
                          (3, 4), (2, 4), (1, 4), (0, 4), (5, 4), (6, 4), (7, 4)]
        expected_moves.sort()
        moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_black_rook_blocked_moves(self):
        self.board.clear_board()
        self.board.board[7][7] = '\u2656'  # Black rook
        moves = self.board.collect_rook_moves(7, 7)
        expected_moves = [(7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (7, 0), 
                          (6, 7), (5, 7), (4, 7), (3, 7), (2, 7), (1, 7), (0, 7)]
        expected_moves.sort()
        moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_black_rook_capture_moves(self):
        self.board.clear_board()
        self.board.board[7][7] = '\u2656'  # Black rook
        moves = self.board.collect_rook_moves(7, 7)
        expected_moves = [(7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (7, 0), 
                          (6, 7), (5, 7), (4, 7), (3, 7), (2, 7), (1, 7), (0, 7)]
        expected_moves.sort()
        moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_black_rook_open_moves(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u2656'  # Black rook
        moves = self.board.collect_rook_moves(4, 4)
        expected_moves = [(4, 3), (4, 2), (4, 1), (4,0), (4, 5), (4, 6), (4, 7),
                          (3, 4), (2, 4), (1, 4), (0, 4), (5, 4), (6, 4), (7, 4)]
        expected_moves.sort()
        moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_collect_bishop_moves_white_bishop_blocked_by_own_piece(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u2657'  # White bishop
        self.board.board[3][3] = '\u2659'  # White pawn
        moves = self.board.collect_bishop_moves(4, 4)
        expected_moves = [(5, 5), (6, 6), (7, 7), (5, 3), (6, 2), (7, 1), (3, 5), (2, 6), (1, 7)]
        expected_moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_collect_bishop_moves_black_bishop_blocked_by_own_piece(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265D'  # Black bishop
        self.board.board[3][3] = '\u265F'  # Black pawn
        moves = self.board.collect_bishop_moves(4, 4)
        expected_moves = [(5, 5), (6, 6), (7, 7), (5, 3), (6, 2), (7, 1), (3, 5), (2, 6), (1, 7)]
        expected_moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_collect_bishop_moves_white_bishop_capturing_opponent_piece(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u2657'  # White bishop
        self.board.board[3][3] = '\u265F'  # Black pawn
        moves = self.board.collect_bishop_moves(4, 4)
        expected_moves = [(3, 3), (5, 5), (6, 6), (7, 7), (5, 3), (6, 2), (7, 1), (3, 5), (2, 6), (1, 7)]
        expected_moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_collect_bishop_moves_black_bishop_capturing_opponent_piece(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265D'  # Black bishop
        self.board.board[3][3] = '\u2659'  # White pawn
        moves = self.board.collect_bishop_moves(4, 4)
        expected_moves = [(3, 3), (5, 5), (6, 6), (7, 7), (5, 3), (6, 2), (7, 1), (3, 5), (2, 6), (1, 7)]
        expected_moves.sort()
        self.assertEqual(moves, expected_moves)
    
    def test_collect_queen_moves_white_queen_blocked_by_own_piece(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u2655'  # White queen
        self.board.board[3][3] = '\u2659'  # White pawn
        moves = self.board.collect_queen_moves(4, 4)
        expected_moves = [(5, 5), (6, 6), (7, 7), (5, 3), (6, 2), (7, 1), 
                          (4, 3), (4, 2), (4, 1), (4, 0), (4, 5), (4, 6), (4, 7), 
                          (3, 5), (2, 6), (1, 7), (3, 4), (2, 4), (1, 4), (0, 4), 
                          (5, 4), (6, 4), (7, 4)]
        expected_moves.sort()
        moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_collect_queen_moves_black_queen_blocked_by_own_piece(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265B'  # Black queen
        self.board.board[3][3] = '\u265F'  # Black pawn
        moves = self.board.collect_queen_moves(4, 4)
        expected_moves = [(5, 5), (6, 6), (7, 7), (5, 3), (6, 2), (7, 1), 
                          (4, 3), (4, 2), (4, 1), (4, 0), (4, 5), (4, 6), (4, 7), 
                          (3, 5), (2, 6), (1, 7), (3, 4), (2, 4), (1, 4), (0, 4), 
                          (5, 4), (6, 4), (7, 4)]
        expected_moves.sort()
        moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_collect_queen_moves_white_queen_capturing_opponent_piece(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u2655'  # White queen
        self.board.board[3][3] = '\u265F'  # Black pawn
        moves = self.board.collect_queen_moves(4, 4)
        expected_moves = [(5, 5), (6, 6), (7, 7), (5, 3), (6, 2), (7, 1), 
                          (4, 3), (4, 2), (4, 1), (4, 0), (4, 5), (4, 6), (4, 7), 
                          (3, 5), (2, 6), (1, 7), (3, 4), (2, 4), (1, 4), (0, 4), 
                          (5, 4), (6, 4), (7, 4), (3, 3)]  # Expected space to be captured
        expected_moves.sort()
        moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_collect_queen_moves_black_queen_capturing_opponent_piece(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265B'  # Black queen
        self.board.board[3][3] = '\u2659'  # White pawn
        moves = self.board.collect_queen_moves(4, 4)
        expected_moves = [(5, 5), (6, 6), (7, 7), (5, 3), (6, 2), (7, 1), 
                          (4, 3), (4, 2), (4, 1), (4, 0), (4, 5), (4, 6), (4, 7), 
                          (3, 5), (2, 6), (1, 7), (3, 4), (2, 4), (1, 4), (0, 4), 
                          (5, 4), (6, 4), (7, 4), (3, 3)]  # Expected space to be captured
        expected_moves.sort()
        moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_collect_king_moves_white_king_in_center(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u2654'  # White king
        moves = self.board.collect_king_moves(4, 4)
        expected_moves = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)]
        expected_moves.sort()
        moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_collect_king_moves_black_king_in_center(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265A'  # Black king
        moves = self.board.collect_king_moves(4, 4)
        expected_moves = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)]
        expected_moves.sort()
        moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_collect_king_moves_white_king_on_edge(self):
        self.board.clear_board()
        self.board.board[0][0] = '\u2654'  # White king
        moves = self.board.collect_king_moves(0, 0)
        expected_moves = [(0, 1), (1, 0), (1, 1)]
        expected_moves.sort()
        moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_collect_king_moves_black_king_on_edge(self):
        self.board.clear_board()
        self.board.board[7][7] = '\u265A'  # Black king
        moves = self.board.collect_king_moves(7, 7)
        expected_moves = [(6, 6), (6, 7), (7, 6)]
        expected_moves.sort()
        moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_collect_king_moves_white_king_capturing_opponent_piece(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u2654'  # White king
        self.board.board[3][3] = '\u265F'  # Black pawn
        moves = self.board.collect_king_moves(4, 4)
        expected_moves = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)]
        expected_moves.sort()
        moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_collect_king_moves_black_king_capturing_opponent_piece(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265A'  # Black king
        self.board.board[3][3] = '\u2659'  # White pawn
        moves = self.board.collect_king_moves(4, 4)
        expected_moves = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)]
        expected_moves.sort()
        moves.sort()
        self.assertEqual(moves, expected_moves)

    def test_move_pawn_returns_true(self):
        self.board.clear_board()
        self.board.board[1][1] = '\u2659'  # White pawn
        moves = self.board.collect_pawn_moves(1, 1)
        self.assertTrue(self.board.move_piece((1, 1), (1, 0), moves))

    def test_move_pawn_to_new_spot(self):
        self.board.clear_board()
        self.board.board[1][1] = '\u2659'  # White pawn
        moves = self.board.collect_pawn_moves(1, 1)
        self.board.move_piece((1, 1), (1, 0), moves)
        self.assertEqual(self.board.board[0][1], '\u2659')
        self.assertEqual(self.board.board[1][1], ' ')

    def test_pawn_capture3(self):
        self.board.clear_board()
        self.board.board[1][1] = '\u265F' # Black pawn
        self.board.board[2][2] = '\u2659'  # White pawn
        moves = self.board.collect_pawn_moves(1, 1)
        self.board.move_piece((1, 1), (2, 2), moves)
        self.assertEqual(self.board.board[2][2], '\u265F')
        self.assertEqual(self.board.board[1][1], ' ')

    def test_knight_move_returns_true(self):
        self.board.clear_board()
        self.board.board[1][1] = '\u2658'  # White knight
        moves = self.board.collect_knight_moves(1, 1)
        self.assertTrue(self.board.move_piece((1, 1), (2, 3), moves))

    def test_knight_move(self):
        self.board.clear_board()
        self.board.board[1][1] = '\u2658'  # White knight
        moves = self.board.collect_knight_moves(1, 1)
        self.board.move_piece((1, 1), (2, 3), moves)
        self.assertEqual(self.board.board[3][2], '\u2658')
        self.assertEqual(self.board.board[1][1], ' ')

    def test_knight_capture(self):
        self.board.clear_board()
        self.board.board[1][1] = '\u2658'  # White knight
        self.board.board[3][2] = '\u265F'  # Black pawn
        moves = self.board.collect_knight_moves(1, 1)
        self.board.move_piece((1, 1), (2, 3), moves)
        self.assertEqual(self.board.board[3][2], '\u2658')
        self.assertEqual(self.board.board[1][1], ' ')

    def test_rook_move_returns_true(self):
        self.board.clear_board()
        self.board.board[1][1] = '\u2656'  # White rook
        moves = self.board.collect_rook_moves(1, 1)
        self.assertTrue(self.board.move_piece((1, 1), (1, 3), moves))

    def test_rook_move(self):
        self.board.clear_board()
        self.board.board[1][1] = '\u2656'  # White rook
        moves = self.board.collect_rook_moves(1, 1)
        self.board.move_piece((1, 1), (1, 3), moves)
        self.assertEqual(self.board.board[3][1], '\u2656')
        self.assertEqual(self.board.board[1][1], ' ')

    def test_rook_capture(self):
        self.board.clear_board()
        self.board.board[1][1] = '\u2656'  # White rook
        self.board.board[3][1] = '\u265F'  # Black pawn
        moves = self.board.collect_rook_moves(1, 1)
        self.board.move_piece((1, 1), (1, 3), moves)
        self.assertEqual(self.board.board[3][1], '\u2656')
        self.assertEqual(self.board.board[1][1], ' ')

    def test_bishop_move_returns_true(self):
        self.board.clear_board()
        self.board.board[1][1] = '\u2657'  # White bishop
        moves = self.board.collect_bishop_moves(1, 1)
        self.assertTrue(self.board.move_piece((1, 1), (3, 3), moves))

    def test_bishop_move(self):
        self.board.clear_board()
        self.board.board[1][1] = '\u2657'  # White bishop
        moves = self.board.collect_bishop_moves(1, 1)
        self.board.move_piece((1, 1), (3, 3), moves)
        self.assertEqual(self.board.board[3][3], '\u2657')
        self.assertEqual(self.board.board[1][1], ' ')

    def test_bishop_capture(self):
        self.board.clear_board()
        self.board.board[1][1] = '\u2657'  # White bishop
        self.board.board[3][3] = '\u265F'  # Black pawn
        moves = self.board.collect_bishop_moves(1, 1)
        self.board.move_piece((1, 1), (3, 3), moves)
        self.assertEqual(self.board.board[3][3], '\u2657')
        self.assertEqual(self.board.board[1][1], ' ')


    def test_is_king_in_check_no_threats(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u2654'  # Black king
        self.board.blackX, self.board.blackY = 4, 4
        self.assertFalse(self.board.is_king_in_check('\u2654'))

    def test_is_king_in_check_pawn_threatening(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u2654'  # Black king
        self.board.board[3][5] = '\u265F'  # White pawn threatening the king
        self.board.blackX, self.board.blackY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u2654'))

    def test_is_king_in_check_no_threats_black(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265A'  # White king
        self.board.whiteX, self.board.whiteY = 4, 4
        self.assertFalse(self.board.is_king_in_check('\u2654'))

    def test_is_king_in_check_pawn_threatening(self):
        self.board.clear_board()
        self.board.board[3][5] = '\u265A'  # White king
        self.board.board[4][4] = '\u2659'  # Black pawn threatening the king
        self.board.whiteX, self.board.whiteY = 5, 3
        self.assertTrue(self.board.is_king_in_check('\u265A'))

    def test_is_king_in_check_bishop_threatening_diagonal1(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u2654'  # White king (pretending to be black)
        self.board.board[7][7] = '\u265D'  # White bishop threatening the king
        self.board.blackX, self.board.blackY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u2654'))

    def test_is_king_in_check_bishop_threatening_diagonal2(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u2654'  # White king (pretending to be black)
        self.board.board[1][7] = '\u265D'  # White bishop threatening the king
        self.board.blackX, self.board.blackY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u2654'))

    def test_is_king_in_check_bishop_threatening_diagonal1_white(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u2654'  # White king
        self.board.board[0][0] = '\u265D'  # White bishop threatening the king
        self.board.blackX, self.board.blackY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u2654'))

    def test_is_king_in_check_bishop_threatening_diagonal2_white(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u2654'  # White king
        self.board.board[7][1] = '\u265D'  # White bishop threatening the king
        self.board.blackX, self.board.blackY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u2654'))

    def test_is_king_in_check_queen_threatening_diagonal1_white(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u2654'  # White king
        self.board.board[7][7] = '\u265B'  # White queen threatening the king
        self.board.blackX, self.board.blackY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u2654'))

    def test_is_king_in_check_queen_threatening_diagonal2_white(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u2654'  # White king
        self.board.board[1][7] = '\u265B'  # White queen threatening the king
        self.board.blackX, self.board.blackY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u2654'))

    def test_is_king_in_check_queen_threatening_diagonal1_white(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u2654'  # White king
        self.board.board[0][0] = '\u265B'  # White queen threatening the king
        self.board.blackX, self.board.blackY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u2654'))

    def test_is_king_in_check_queen_threatening_diagonal2_white(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u2654'  # White king
        self.board.board[7][1] = '\u265B'  # White queen threatening the king
        self.board.blackX, self.board.blackY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u2654'))

    def test_is_king_in_check_bishop_threatening_diagonal1(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265A'  # Black king (pretending to be white)
        self.board.board[7][7] = '\u2657'  # Black bishop threatening the king
        self.board.whiteX, self.board.whiteY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u265A'))

    def test_is_king_in_check_bishop_threatening_diagonal2(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265A'  # Black king (pretending to be white)
        self.board.board[1][7] = '\u2657'  # Black bishop threatening the king
        self.board.whiteX, self.board.whiteY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u265A'))

    def test_is_king_in_check_bishop_threatening_diagonal1_black(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265A'  # Black king
        self.board.board[0][0] = '\u2657'  # Black bishop threatening the king
        self.board.whiteX, self.board.whiteY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u265A'))

    def test_is_king_in_check_bishop_threatening_diagonal2_black(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265A'  # Black king
        self.board.board[7][1] = '\u2657'  # Black bishop threatening the king
        self.board.whiteX, self.board.whiteY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u265A'))

    def test_is_king_in_check_queen_threatening_diagonal1_black(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265A'  # Black king
        self.board.board[7][7] = '\u2655'  # Black queen threatening the king
        self.board.whiteX, self.board.whiteY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u265A'))

    def test_is_king_in_check_queen_threatening_diagonal2_black(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265A'  # Black king
        self.board.board[1][7] = '\u2655'  # Black queen threatening the king
        self.board.whiteX, self.board.whiteY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u265A'))

    def test_is_king_in_check_queen_threatening_diagonal1_black(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265A'  # Black king
        self.board.board[0][0] = '\u2655'  # Black queen threatening the king
        self.board.whiteX, self.board.whiteY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u265A'))

    def test_is_king_in_check_queen_threatening_diagonal2_black(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265A'  # Black king
        self.board.board[7][1] = '\u2655'  # Black queen threatening the king
        self.board.whiteX, self.board.whiteY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u265A'))

    def test_is_king_in_check_knight_threatening1_white(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u2654'  # White king
        self.board.board[6][5] = '\u265e'  # Black knight threatening the king
        self.board.blackX, self.board.blackY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u2654'))

    def test_is_king_in_check_knight_threatening2_white(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u2654'  # White king
        self.board.board[5][6] = '\u265e'  # Black knight threatening the king
        self.board.blackX, self.board.blackY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u2654'))

    def test_is_king_in_check_knight_threatening1_black(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265A'  # Black king
        self.board.board[6][5] = '\u2658'  # White knight threatening the king
        self.board.whiteX, self.board.whiteY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u265A'))

    def test_is_king_in_check_knight_threatening2_black(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265A'  # Black king
        self.board.board[5][6] = '\u2658'  # White knight threatening the king
        self.board.whiteX, self.board.blackY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u265A'))

    def test_is_king_in_check_knight_threatening_3_black(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265A'  # Black king
        self.board.board[5][6] = '\u2658'  # White knight threatening the king
        self.board.whiteX, self.board.whiteY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u265A'))

    def test_is_king_in_check_knight_threatening_4_black(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265A'  # Black king
        self.board.board[5][2] = '\u2658'  # White knight threatening the king
        self.board.whiteX, self.board.whiteY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u265A'))

    def test_is_king_in_check_knight_threatening_5_black(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265A'  # Black king
        self.board.board[3][6] = '\u2658'  # White knight threatening the king
        self.board.whiteX, self.board.whiteY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u265A'))

    def test_is_king_in_check_knight_threatening_6_black(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265A'  # Black king
        self.board.board[3][2] = '\u2658'  # White knight threatening the king
        self.board.whiteX, self.board.whiteY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u265A'))

    def test_is_king_in_check_knight_threatening_7_black(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265A'  # Black king
        self.board.board[2][3] = '\u2658'  # White knight threatening the king
        self.board.whiteX, self.board.whiteY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u265A'))

    def test_is_king_in_check_knight_threatening_8_black(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265A'  # Black king
        self.board.board[6][3] = '\u2658'  # White knight threatening the king
        self.board.whiteX, self.board.whiteY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u265A'))

    def test_is_king_in_check_rook_threatening_north_black(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265A'  # Black king
        self.board.board[4][7] = '\u2656'  # White rook threatening the king
        self.board.whiteX, self.board.whiteY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u265A'))

    def test_is_king_in_check_rook_threatening_east_black(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265A'  # Black king
        self.board.board[7][4] = '\u2656'  # White rook threatening the king
        self.board.whiteX, self.board.whiteY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u265A'))

    def test_is_king_in_check_rook_threatening_south_white(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u2654'  # White king
        self.board.board[4][1] = '\u265C'  # Black rook threatening the king
        self.board.blackX, self.board.blackY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u2654'))

    def test_is_king_in_check_rook_threatening_west_white(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u2654'  # White king
        self.board.board[1][4] = '\u265C'  # Black rook threatening the king
        self.board.blackX, self.board.blackY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u2654'))

    def test_is_king_in_check_queen_threatening_north_black(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265A'  # Black king
        self.board.board[4][7] = '\u2655'  # Black queen threatening the king
        self.board.whiteX, self.board.whiteY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u265A'))

    def test_is_king_in_check_queen_threatening_east_black(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u265A'  # Black king
        self.board.board[7][4] = '\u2655'  # Black queen threatening the king
        self.board.whiteX, self.board.whiteY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u265A'))

    def test_is_king_in_check_queen_threatening_south_white(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u2654'  # White king
        self.board.board[4][1] = '\u265B'  # White queen threatening the king
        self.board.blackX, self.board.blackY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u2654'))

    def test_is_king_in_check_queen_threatening_west_white(self):
        self.board.clear_board()
        self.board.board[4][4] = '\u2654'  # White king
        self.board.board[1][4] = '\u265B'  # White queen threatening the king
        self.board.blackX, self.board.blackY = 4, 4
        self.assertTrue(self.board.is_king_in_check('\u2654'))

    def test_rook_capture(self):
        self.board.clear_board()
        self.board.board[1][1] = '\u2656'  # White rook
        self.board.board[1][3] = '\u265F'  # Black pawn
        moves = self.board.collect_rook_moves(1, 1)
        self.board.move_piece((1, 1), (3, 1), moves)
        self.assertEqual(self.board.blackCaptures['\u265F'], 1)

    def test_queen_capture(self):
        self.board.clear_board()
        self.board.board[1][1] = '\u2655'  # White queen
        self.board.board[3][3] = '\u265F'  # Black pawn
        moves = self.board.collect_queen_moves(1, 1)
        self.board.move_piece((1, 1), (3, 3), moves)
        self.assertEqual(self.board.blackCaptures['\u265F'], 1)


    def test_knight_capture(self):
        self.board.clear_board()
        self.board.board[1][1] = '\u2658'  # White knight
        self.board.board[2][3] = '\u265F'  # Black pawn
        moves = self.board.collect_knight_moves(1, 1)
        self.board.move_piece((1, 1), (3, 2), moves)
        self.assertEqual(self.board.blackCaptures['\u265F'], 1)

    def test_bishop_capture(self):
        self.board.clear_board()
        self.board.board[1][1] = '\u2657'  # White bishop
        self.board.board[3][3] = '\u265F'  # Black pawn
        moves = self.board.collect_bishop_moves(1, 1)
        self.board.move_piece((1, 1), (3, 3), moves)
        self.assertEqual(self.board.blackCaptures['\u265F'], 1)

    def test_capture_multiple_pawns(self):
        self.board.clear_board()
        self.board.board[1][1] = '\u265F'  # Black pawn
        self.board.board[2][2] = '\u2659'  # White pawn
        self.board.board[3][3] = '\u2659'  # White pawn
        moves = self.board.collect_pawn_moves(1, 1)
        self.board.move_piece((1, 1), (2, 2), moves)
        moves = self.board.collect_pawn_moves(2, 2)
        self.board.move_piece((2, 2), (3, 3), moves)
        self.assertEqual(self.board.whiteCaptures['\u2659'], 2)

    def test_pawn_capture(self):
        self.board.clear_board()
        self.board.board[2][2] = '\u2659'  # White pawn
        self.board.board[1][1] = '\u265F'  # Black pawn
        moves = self.board.collect_pawn_moves(2, 2)
        self.board.move_piece((2, 2), (1, 1), moves)
        self.assertEqual(self.board.blackCaptures['\u265F'], 1)

    def test_knight_capture(self):
        self.board.clear_board()
        self.board.board[1][1] = '\u265E'  # Black knight
        self.board.board[2][3] = '\u2659'  # White pawn
        moves = self.board.collect_knight_moves(1, 1)
        self.board.move_piece((1, 1), (3, 2), moves)
        self.assertEqual(self.board.whiteCaptures['\u2659'], 1)

    def test_bishop_capture(self):
        self.board.clear_board()
        self.board.board[1][1] = '\u265D'  # Black bishop
        self.board.board[3][3] = '\u2659'  # White pawn
        moves = self.board.collect_bishop_moves(1, 1)
        self.board.move_piece((1, 1), (3, 3), moves)
        self.assertEqual(self.board.whiteCaptures['\u2659'], 1)

    def test_king_side_castle(self):
        self.board.clear_board()
        self.board.board[7][4] = '\u2654'  # White king
        self.board.board[7][7] = '\u2656'  # White rook
        self.board.castle((7, 7), (4, 7))
        self.assertEqual(self.board.board[7][6], '\u2654')  # King moved to f1
        self.assertEqual(self.board.board[7][5], '\u2656')  # Rook moved to g1

    def test_queen_side_castle(self):
        self.board.clear_board()
        self.board.board[7][4] = '\u2654'  # White king
        self.board.board[7][0] = '\u2656'  # White rook
        self.board.castle((0, 7), (4, 7))
        self.assertEqual(self.board.board[7][1], '\u2654')  # King moved to c1
        self.assertEqual(self.board.board[7][2], '\u2656')  # Rook moved to d1

    def test_black_king_side_castle(self):
        self.board.clear_board()
        self.board.board[0][4] = '\u265A'  # Black king
        self.board.board[0][7] = '\u265C'  # Black rook
        self.board.castle((7, 0), (4, 0))
        self.assertEqual(self.board.board[0][6], '\u265A')  # King moved to f8
        self.assertEqual(self.board.board[0][5], '\u265C')  # Rook moved to g8

    def test_black_queen_side_castle(self):
        self.board.clear_board()
        self.board.board[0][4] = '\u265A'  # Black king
        self.board.board[0][0] = '\u265C'  # Black rook
        self.board.castle((0, 0), (4, 0))
        self.assertEqual(self.board.board[0][1], '\u265A')  # King moved to c8
        self.assertEqual(self.board.board[0][2], '\u265C')  # Rook moved to d8

    def test_castling_already_happened(self):
        self.board.clear_board()
        self.board.has_castled_white = True
        self.board.board[7][4] = '\u2654'  # White king
        self.board.board[7][7] = '\u2656'  # White rook
        result = self.board.castle((7, 7), (4, 7))
        self.assertFalse(result)

    def test_incorrect_castling_coordinates(self):
        self.board.clear_board()
        self.board.board[7][3] = '\u2654'  # White king not in starting position
        self.board.board[7][7] = '\u2656'  # White rook
        result = self.board.castle((7, 7), (3, 7))
        self.assertFalse(result)

    def test_king_not_in_check(self):
        self.board.clear_board()
        self.board.board[7][4] = '\u2654'  # White king
        self.board.board[6][4] = '\u2659'  # White pawn
        self.board.blackX, self.board.blackY = 4, 7
        self.assertFalse(self.board.is_check(4, 6))

    def test_black_king_in_check_by_white_pawn(self):
        self.board.clear_board()
        self.board.board[7][4] = '\u2654'  # black king
        self.board.board[6][3] = '\u265F'  # white pawn
        self.board.blackX, self.board.blackY = 4, 7
        self.assertTrue(self.board.is_check(3, 6))

    # def test_white_king_in_check_by_black_knight(self):
    #     self.board.clear_board()
    #     self.board.board[7][4] = '\u2654'  # White king
    #     self.board.board[5][3] = '\u265E'  # Black knight
    #     self.board.whiteX, self.board.whiteY = 4, 7
    #     self.assertTrue(self.board.is_check(3, 5))

    # def test_white_king_in_check_by_black_bishop(self):
    #     self.board.clear_board()
    #     self.board.board[7][4] = '\u2654'  # White king
    #     self.board.board[5][2] = '\u265D'  # Black bishop
    #     self.board.whiteX, self.board.whiteY = 4, 7
    #     self.assertTrue(self.board.is_check(2, 5))

    # def test_black_king_in_check_by_white_rook(self):
    #     self.board.clear_board()
    #     self.board.board[0][4] = '\u265A'  # Black king
    #     self.board.board[1][4] = '\u2656'  # White rook
    #     self.board.blackX, self.board.blackY = 4, 0
    #     self.assertTrue(self.board.is_check(4, 1))

    # def test_black_king_in_check_by_white_queen(self):
    #     self.board.clear_board()
    #     self.board.board[0][4] = '\u265A'  # Black king
    #     self.board.board[1][4] = '\u2655'  # White queen
    #     self.board.blackX, self.board.blackY = 4, 0
    #     self.assertTrue(self.board.is_check(4, 1))

    # def test_black_king_in_check_by_white_king(self):
    #     self.board.clear_board()
    #     self.board.board[0][4] = '\u265A'  # Black king
    #     self.board.board[1][4] = '\u2654'  # White king
    #     self.board.blackX, self.board.blackY = 4, 0
    #     self.assertTrue(self.board.is_check(4, 1))









if __name__ == '__main__':
    unittest.main()
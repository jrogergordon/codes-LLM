import unittest
from chess import ChessBoard
from unittest.mock import patch

class TestChessBoard(unittest.TestCase):
    def setUp(self):
        self.board = ChessBoard()

    # def test_white_pawn_no_pieces_in_front(self):
    #     self.board.board[6][4] = '\u2659'
    #     self.assertEqual(self.board.get_pawn_moves(4, 6), [(4, 5), (4, 4)])

    # def test_white_pawn_piece_in_front(self):
    #     self.board.board[6][4] = '\u2659'
    #     self.board.board[5][4] = '\u265C'
    #     self.assertEqual(self.board.get_pawn_moves(4, 6), [])

    # def test_white_pawn_diagonal_capture(self):*************
    #     self.board.board[6][4] = '\u2659'
    #     self.board.board[5][3] = '\u265F'
    #     self.assertEqual(self.board.get_pawn_moves(4, 6), [(3, 5)])

    # def test_black_pawn_no_pieces_in_front(self):
    #     self.board.board[1][4] = '\u265F'
    #     self.assertEqual(self.board.get_pawn_moves(4, 1), [(4, 2), (4, 3)])

    # def test_black_pawn_piece_in_front(self):
    #     self.board.board[1][4] = '\u265F'
    #     self.board.board[2][4] = '\u2656'
    #     self.assertEqual(self.board.get_pawn_moves(4, 1), [])

    # def test_black_pawn_diagonal_capture(self):**********
    #     self.board.board[1][4] = '\u265F'
    #     self.board.board[2][5] = '\u2659'
    #     self.assertEqual(self.board.get_pawn_moves(4, 1), [(5, 2)])

    # def test_display_board_and_collect_piece_valid_input(self):
    #     self.board.board[4][4] = '\u2659'  # White pawn
    #     with patch('builtins.input', side_effect=['4', '4']):
    #         x, y = self.board.display_board_and_collect_piece()
    #     self.assertEqual((x, y), (4, 4))

    # def test_display_board_and_collect_piece_invalid_input(self):
    #     self.board.board[4][4] = '\u2659'  # White pawn
    #     with patch('builtins.input', side_effect=['8', '4', 'a', '4', '4']):
    #         x, y = self.board.display_board_and_collect_piece()
    #     self.assertEqual((x, y), (4, 4))
    # def test_collect_knight_moves_white_knight(self):
    #     self.board.board[0][0] = '\u2658'  # White knight
    #     moves = self.board.collect_knight_moves(0, 0)
    #     expected_moves = [(2, 1), (1,2)]
    #     self.assertEqual(moves, expected_moves)

    # def test_collect_knight_moves_white_knight_capture(self):
    #     self.board.board[0][0] = '\u2658'  # White knight
    #     self.board.board[1][2] = '\u265F'  # Black pawn
    #     moves = self.board.collect_knight_moves(0, 0)
    #     expected_moves = [(2, 1), (1, 2)]
    #     self.assertEqual(moves, expected_moves)

    # def test_collect_knight_moves_black_knight(self):
    #     self.board.board[0][0] = '\u265E'  # Black knight
    #     moves = self.board.collect_knight_moves(0, 0)
    #     expected_moves = [(1, 2)]
    #     self.assertEqual(moves, expected_moves)

    # def test_collect_knight_moves_black_knight_all_moves(self):
    #     self.board.board[4][4] = '\u265E'  # Black knight
    #     moves = self.board.collect_knight_moves(4, 4)
    #     expected_moves = [(6,5), (5,6), (3,6), (2,5), (2,3), (3,2), (5,2), (6,3)]
    #     self.assertEqual(moves, expected_moves)

    def test_white_rook_blocked_moves(self):
        self.board.clear_board()
        self.board.board[0][0] = '\u265C'  # White rook
        moves = self.board.collect_rook_moves(0, 0)
        expected_moves = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
        expected_moves.sort()
        self.assertEqual(moves, expected_moves)

    # def test_white_rook_capture_moves(self):
    #     self.board.clear_board()
    #     self.board.board[0][0] = '\u265C'  # White rook
    #     moves = self.board.collect_rook_moves(0, 0)
    #     expected_moves = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), 
    #                       (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
    #     expected_moves.sort()
    #     moves.sort()
    #     self.assertEqual(moves, expected_moves)

    # def test_white_rook_open_moves(self):
    #     self.board.clear_board()
    #     self.board.board[4][4] = '\u265C'  # White rook
    #     moves = self.board.collect_rook_moves(4, 4)
    #     expected_moves = [(4, 3), (4, 2), (4, 1), (4, 5), (4, 6), (4, 7), 
    #                       (3, 4), (2, 4), (1, 4), (0, 4), (5, 4), (6, 4), (7, 4)]
    #     expected_moves.sort()
    #     moves.sort()
    #     self.assertEqual(moves, expected_moves)

    # def test_black_rook_blocked_moves(self):
    #     self.board.clear_board()
    #     self.board.board[7][7] = '\u2656'  # Black rook
    #     moves = self.board.collect_rook_moves(7, 7)
    #     expected_moves = [(7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (7, 0), 
    #                       (6, 7), (5, 7), (4, 7), (3, 7), (2, 7), (1, 7), (0, 7)]
    #     expected_moves.sort()
    #     moves.sort()
    #     self.assertEqual(moves, expected_moves)

    # def test_black_rook_capture_moves(self):
    #     self.board.clear_board()
    #     self.board.board[7][7] = '\u2656'  # Black rook
    #     moves = self.board.collect_rook_moves(7, 7)
    #     expected_moves = [(7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (7, 0), 
    #                       (6, 7), (5, 7), (4, 7), (3, 7), (2, 7), (1, 7), (0, 7)]
    #     expected_moves.sort()
    #     moves.sort()
    #     self.assertEqual(moves, expected_moves)

    # def test_black_rook_open_moves(self):
    #     self.board.clear_board()
    #     self.board.board[4][4] = '\u2656'  # Black rook
    #     moves = self.board.collect_rook_moves(4, 4)
    #     expected_moves = [(4, 3), (4, 2), (4, 1), (4, 5), (4, 6), (4, 7), 
    #                       (3, 4), (2, 4), (1, 4), (0, 4), (5, 4), (6, 4), (7, 4)]
    #     expected_moves.sort()
    #     moves.sort()
    #     self.assertEqual(moves, expected_moves)

    # def test_collect_bishop_moves_white_bishop_blocked_by_own_piece(self):
    #     self.board.board[4][4] = '\u2657'  # White bishop
    #     self.board.board[3][3] = '\u2659'  # White pawn
    #     moves = self.board.collect_bishop_moves(4, 4)
    #     self.board.print_board()
    #     expected_moves = [(5, 5), (6, 6), (7, 7), (5, 3), (6, 2), (7, 1)]
    #     self.assertEqual(moves, expected_moves)

    # def test_collect_bishop_moves_black_bishop_blocked_by_own_piece(self):
    #     self.board.board[4][4] = '\u265D'  # Black bishop
    #     self.board.board[3][3] = '\u265F'  # Black pawn
    #     moves = self.board.collect_bishop_moves(4, 4)
    #     self.board.print_board()
    #     expected_moves = [(5, 5), (6, 6), (7, 7), (5, 3), (6, 2), (7, 1)]
    #     self.assertEqual(moves, expected_moves)

    # def test_collect_bishop_moves_white_bishop_capturing_opponent_piece(self):
    #     self.board.board[4][4] = '\u2657'  # White bishop
    #     self.board.board[3][3] = '\u265F'  # Black pawn
    #     moves = self.board.collect_bishop_moves(4, 4)
    #     self.board.print_board()
    #     expected_moves = [(3, 3), (5, 5), (6, 6), (7, 7), (5, 3), (6, 2), (7, 1)]
    #     self.assertEqual(moves, expected_moves)

    # def test_collect_bishop_moves_black_bishop_capturing_opponent_piece(self):
    #     self.board.board[4][4] = '\u265D'  # Black bishop
    #     self.board.board[3][3] = '\u2659'  # White pawn
    #     moves = self.board.collect_bishop_moves(4, 4)
    #     self.board.print_board()
    #     expected_moves = [(3, 3), (5, 5), (6, 6), (7, 7), (5, 3), (6, 2), (7, 1)]
    #     self.assertEqual(moves, expected_moves)
    

if __name__ == '__main__':
    unittest.main()
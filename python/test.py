import unittest
from chess import ChessBoard

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

    # def test_white_pawn_diagonal_capture(self):
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

    # def test_black_pawn_diagonal_capture(self):
    #     self.board.board[1][4] = '\u265F'
    #     self.board.board[2][5] = '\u2659'
    #     self.assertEqual(self.board.get_pawn_moves(4, 1), [(5, 2)])
    def test_display_board_and_collect_piece_valid_input(self):
        self.board.board[4][4] = '\u2659'  # White pawn
        x, y = self.board.display_board_and_collect_piece()
        self.assertEqual((x, y), (4, 4))

    def test_display_board_and_collect_piece_invalid_input(self):
        self.board.board[4][4] = '\u2659'  # White pawn
        with patch('builtins.input', side_effect=['8', '4', 'a', '4']):
            x, y = self.board.display_board_and_collect_piece()
        self.assertEqual((x, y), (4, 4))

if __name__ == '__main__':
    unittest.main()
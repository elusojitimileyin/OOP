import unittest

from OOP.tic_tac_toe.TicTacToe import TicTacToe


class TicTacToeTest(unittest.TestCase):
    def test_initial_board_is_empty(self):
        self.game = TicTacToe()
        board = self.game.get_board()
        expected_board = [['-', '-', '-'],
                          ['-', '-', '-'],
                          ['-', '-', '-']]
        self.assertEqual(board, expected_board)

    def test_initial_board_is_full(self):
        self.game = TicTacToe()
        board = self.game.make_move("X", "O")
        expected_board = [['X', 'X', 'O'],
                          ['O', 'O', 'X'],
                          ['X', 'X', 'O']]
        self.assertEqual(board, expected_board)


if __name__ == '__main__':
    unittest.main()

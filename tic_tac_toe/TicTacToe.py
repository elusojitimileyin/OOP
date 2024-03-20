from OOP.exceptions.board_filled_exception import BoardFilledException
from OOP.exceptions.null_player_exception import NullPlayerException
from OOP.tic_tac_toe import Players


class TicTacToe:

    def __init__(self):
        self.board = [['-' for i in range(3)] for j in range(3)]
        self.currentPlayer = Players.X

    def make_move(self, row, col):
        if row < 0 or row >= 3 or col < 0 or col >= 3:
            return
        if self.board[row][col] != '-':
            raise BoardFilledException("Broad is filled")
        if self.currentPlayer == ' -':
            raise NullPlayerException("Wrong player")

        self.board[row][col] = self.currentPlayer.getplayer()
        self.switchPlayer()

    def check_rows(self):
        for i in range(3):
            if self.board[i][0] != '-' and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return True
            return False

    def check_cols(self):
        for i in range(3):
            if self.board[0][i] != '-' and self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return True
            return False

    def check_diagonals(self):
        return (self.board[0][0] != '-' and self.board[0][0] == self.board[1][1] == self.board[2][2] or self.board[0][2]
                != '-' and self.board[0][2] == self.board[1][1] == self.board[2][0])

    def check_for_win(self):
        return self.check_rows() or self.check_cols() or self.check_diagonals()

    def switchPlayer(self):
        if self.currentPlayer == Players.X():
            self.currentPlayer = Players.O()
        else:
            self.currentPlayer = Players.X()

    def get_board(self):
        return self.board

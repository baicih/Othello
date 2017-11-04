# -*- coding: utf-8 -*-


class Board(object):
    """Board class is a representation of an 8x8 othello board.

    Attributes:
        EMPTY (int): 0, represents a empty space
        BLACK (int): 1, represents a black piece
        WHITE (int): 2, represents a white piece
        board (list): list of lists of int, dimension: 8 x 8
    """

    EMPTY = 0
    BLACK = 1
    WHITE = 2

    def __init__(self):
        """Initialize an othello board.
        """
        self.board = [[Board.EMPTY] * 8 for _ in range(8)]
        self.board[3][3] = self.board[4][4] = Board.WHITE
        self.board[4][3] = self.board[3][4] = Board.BLACK

    def count(self):
        """count the number of stones.

        Returns:
            list: [num of empty spaces, num of black, num of white]
        """
        ans = [0] * 3
        for row in self.board:
            for col in row:
                ans[col] += 1
        return ans

    def is_valid_move(self, r, c, color):
        """Validate `color` at row `r` column `c` for the current board.

        Args:
            r (int): row
            c (int): col
            color (int): color of stone

        Returns:
            bool: Ture if `color` can be placed at (r, c),
                False otherwise.
        """
        if self.board[r][c] != Board.EMPTY:
            return False
        opponent = 3 - color
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == dc == 0:
                    continue
                x, y = r + dr, c + dc
                tmp = 0
                while 0 <= x < 8 and 0 <= y < 8 and\
                        self.board[x][y] == opponent:
                    x, y = x + dr, y + dc
                    tmp += 1
                if 0 <= x < 8 and 0 <= y < 8 and\
                        self.board[x][y] == color and tmp > 0:
                    return True
        return False

    def valid_moves(self, color):
        """Find all valid moves for `color` for the current board.

        Args:
            color (int): color of stone

        Returns:
            list: a list of coordinates (r, c).
        """
        return [(i, j) for i in range(8)
                for j in range(8) if self.is_valid_move(i, j, color)]

    def stone_captured(self, r, c, color):
        """Find all stones captured by the move `color` at (r, c).

        Args:
            r (int): row
            c (int): column
            color (int): color of stone

        Returns:
            list: a list of stones captured.
        """
        if self.board[r][c] != Board.EMPTY:
            return []
        ans = []
        opponent = 3 - color
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == dc == 0:
                    continue
                tmp = []
                x, y = r + dr, c + dc
                while 0 <= x < 8 and 0 <= y < 8 and\
                        self.board[x][y] == opponent:
                    tmp.append((x, y))
                    x, y = x + dr, y + dc
                if 0 <= x < 8 and 0 <= y < 8 and self.board[x][y] == color:
                    ans.extend(tmp)
        return ans

    def make_move(self, r, c, color):
        """Make move `color` at (r, c).

        Args:
            r (int): row
            c (int): column
            color (int): color of stones

        Returns:
            bool: True if the move made successfully,
                False otherwise.
        """
        stones = self.stone_captured(r, c, color)
        if not stones:
            return False
        stones.append((r, c))
        for x, y in stones:
            self.board[x][y] = color
        return True

    def reset_board(self, reference=None):
        """Reset board according to `reference`. If `reference` is None,
        reset board to initial board.

        Args:
            reference (Board): an instance from Board, or subclass derived
                from Board.
        """
        if reference is None:
            for i in range(8):
                for j in range(8):
                    self.board[i][j] = Board.EMPTY
            self.board[3][3] = self.board[4][4] = Board.WHITE
            self.board[4][3] = self.board[3][4] = Board.BLACK
            return

        for i in range(8):
            for j in range(8):
                self.board[i][j] = reference.board[i][j]

    def has_valid_move(self, color):
        moves = self.valid_moves(color);
        if moves:
            return True
        return False

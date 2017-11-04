# -*- coding: utf-8 -*-
from board import Board


class JudgeSystem(Board):
    """Judge system for Player class.

    Attributes:
        current (int): current player
        history (list): history of current game
        players (list): list of players
        results (int): results of all tests
    """

    def __init__(self, player1, player2):
        """Initialize a judge system with players.

        Args:
            player1 (Player): Player or subclass of Player, black
            player2 (Player): Player or subclass of Player, white
        """
        self.players = ['',
                        player1(Board.BLACK),
                        player2(Board.WHITE)]
        self.current = Board.BLACK
        self.history = []
        self.results = [0] * 3
        super(JudgeSystem, self).__init__()

    def run_games(self, cnt=1):
        """automatically run games for `cnt` times.

        Args:
            cnt (int, optional): number of games
        """
        for _ in range(cnt):
            while self.has_next_move():
                r, c = self.players[self.current].next_move()
                self.history.append((self.current, r, c))
                self.make_move(r, c, self.current)
                self.current = 3 - self.current
            _, b, w = self.count()
            if b == w:
                self.results[0] += 1
            elif b > w:
                self.results[1] += 1
            else:
                self.results[2] += 1
            self.reset_board()

    def has_next_move(self):
        """whether the game has next move

        Returns:
            bool: True if the game can be still running, False otherwise
        """
        moves = self.valid_moves(self.current)
        if moves:
            self.players[self.current].reset_board(self)
            return True
        self.current = 3 - self.current
        moves = self.valid_moves(self.current)
        if moves:
            self.players[self.current].reset_board(self)
            return True
        return False

    def reset_board(self):
        """reset the judge system
        """
        super(JudgeSystem, self).reset_board()
        self.current = Board.BLACK
        self.history = []

    def get_results(self):
        """get results of the tests

        Returns:
            list: [num of draws, num of black wins, num of white wins]
        """
        return self.results[:]

# -*- coding: utf-8 -*-
from board import Board


class Player(Board):

    """Player class to represent a player for an othello games.

    Player is a subclass of Board.

    Attributes:
        color (int): Board.BLACK or Board.WHITE to represent a role.
    """

    def __init__(self, color):
        """Initialize a player

        Args:
            color (int): Board.BLACK or Board.WHITE to represent a role.
        """
        self.color = color
        super(Player, self).__init__()

    def next_move(self):
        """find next move based on current state of the board. It should
        return a tuple (r, c) representing the coordinate of the move.

        Raises:
            NotImplementedError
        """
        raise NotImplementedError()

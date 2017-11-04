from player import Player
import random


class RandomPlayer(Player):

    def next_move(self):
        moves = self.valid_moves(self.color)
        return random.choice(moves)

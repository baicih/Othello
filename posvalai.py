from player import Player
from board import Board
import random
from judge import JudgeSystem


class PosValPlayer(Player):
	DEPTH = 5

    def next_move(self):
        return next_move_with_depth(self, DEPTH)


    def next_move_with_depth(self, depth):
    	move = -2
    	if (not self.has_valid_move(self.color)):
    		int judge = board.judge()
    		if (judge > 0) return new int[]{Integer.MAX_VALUE - 1, -1};
    		if (judge < 0) return new int[]{Integer.MIN_VALUE + 1, -1};
    		return new int[]{0, -1};
    	}
    	if (depth == 0) return new int[]{evaluateBoard(board), -1};
    	if (board.getTurn() == 'B') {
    		int v = Integer.MIN_VALUE;
    		List<Integer> validMoves = board.getValidMoves();
    		for (Integer a : validMoves) {
    			Board newBoard = new Board(board);
    			newBoard.makeMove(a / 8, a % 8);
    			int tmp = alphabeta(newBoard, depth - 1, alpha, beta)[0];
    			if (tmp > v) {
    				v = tmp;
    				move = a;
    			}
    			alpha = Math.max(alpha, v);
    			if (beta <= alpha) break;
    		}
    		return new int[]{v, move};
    	}
    	else {
    		int v = Integer.MAX_VALUE;
    		List<Integer> validMoves = board.getValidMoves();
    		for (Integer a : validMoves) {
    			Board newBoard = new Board(board);
    			newBoard.makeMove(a / 8, a % 8);
    			int tmp = alphabeta(newBoard, depth - 1, alpha, beta)[0];
    			if (tmp < v) {
    				v = tmp;
    				move = a;
    			}
    			beta = Math.min(beta, v);
    			if (beta <= alpha) break;
    		}
    		return new int[]{v, move};


    def evaluateBoard(board):
    	value = 0
    	for i in range(8):
    		for j in range(8):
    			c = board.board[i][j]
    			if (c == 1):
    				value += evaluatePosition(i, j)
    			else:
    				if (c == 0):
    					continue
    				else:
    					value -= evaluatePosition(i, j)
    	return value

    def evaluatePosition(row, col):
    	if (row > 3):
    		row = 7 - row
    	if (col > 3):
    		col = 7 - col
    	if (row > col):
    		tmp = row
    		row = col
    		col = tmp
    	values = [99,-8,8,6,-24,-4,-3,7,4,0]
    	index = 0
    	for i in range(4):
    		for j in range(i, 4):
    			if (i == row and j == col):
    				return values[index]
    			index += 1
    	return values[index]
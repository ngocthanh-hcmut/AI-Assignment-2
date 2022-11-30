from algorithm import *
from copy import *

board = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, -1], [-1, 0, 0, 0, -1], [-1, -1, -1, -1, -1]]
prev_board = None

def play(player):
    next_move = move(prev_board, board, player, remain_time_x, remain_time_o)
    prev_board = copy.deepcopy(board)
    act_move(board, next_move)



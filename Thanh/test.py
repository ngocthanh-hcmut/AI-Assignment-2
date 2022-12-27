from algorithm import *

def printBoard(board):
    temp = copy.deepcopy(board)

    for x in range(5):
        for y in range(5):
            if temp[x][y] == -1:
                temp[x][y] = "X"
            elif temp[x][y] == 1:
                temp[x][y] = "O"
            elif temp[x][y] == 0:
                temp[x][y] = "-"

    for i in temp:
        print('\t'.join(map(str, i)))
        print()

# temp_pieces = set()

# prev_board = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, -1, 1], [1, 1, 1, 1, 0]]

# board = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, -1]]


# printBoard(prev_board)
# print("------------------------------------------")
# printBoard(board)
# print("------------------------------------------")

# machine_move = move(prev_board, board, 1, 999, 999)

# # machine_move = ((2,4), (3,3))
# act_move(board, machine_move, 1, temp_pieces)
# printBoard(board)


prev_board = None

board = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, -1], [-1, 0, 0, 0, -1], [-1, -1, -1, -1, -1]]

printBoard(board)

pieces = []
for x in range(5):
    for y in range(5):
        if board[x][y] == 1:
            pieces.append((x,y))

print(get_valid_moves(prev_board, board, 1, pieces))

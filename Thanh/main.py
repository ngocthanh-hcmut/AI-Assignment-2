from algorithm import *
import copy


def end_game(board):
    countX = 0
    for x in range(5):
        for y in range(5):
            if board[x][y] == -1:
                countX += 1

    if countX == 0 or countX == 16:
        return True

    return False

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

def inputMove(): pass


def play():
    print("You play X")

    prev_board = None
    board = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, -1], [-1, 0, 0, 0, -1], [-1, -1, -1, -1, -1]]
    printBoard(board)

    temp_pieces = set()
    while not end_game(board):
        print("Your move:")
        input_move = list(map(int, input().split()))
        src_x = input_move[0]
        src_y = input_move[1]
        dest_x = input_move[2]
        dest_y = input_move[3]

        human_move = ((src_x, src_y), (dest_x, dest_y))

        prev_board = copy.deepcopy(board)
        act_move(board, human_move, -1, temp_pieces)

        print("After your move:")
        printBoard(board)

        machine_move = move(prev_board, board, 1, 999, 999)

        act_move(board, machine_move, 1, temp_pieces)
        print("After machine move:")
        printBoard(board)


play()




from algorithm import *
from bad_machine import *
import copy
import random
from colored import *


def random_move(prev_board, board, player):
    pieces = []

    for x in range(5):
        for y in range(5):
            if board[x][y] == player:
                pieces.append((x,y))

    valid_moves = get_valid_moves(prev_board, board, player, pieces)

    num = random.randint(0, len(valid_moves) - 1)

    return valid_moves[num]


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
                temp[x][y] = fg("yellow") + "X"
            elif temp[x][y] == 1:
                temp[x][y] = fg("red") + "O"
            elif temp[x][y] == 0:
                temp[x][y] = fg("white") + "+"

    print('')
    print('    0   1   2   3   4')
    print('')
    print('0   ' + temp[0][0] + fg("white") +  '---'+temp[0][1] + fg("white") + '---' + temp[0][2] + fg("white") + '---'+  temp[0][3] + fg("white") + '---'+ temp[0][4])
    print('    '+fg("white") + '| \ | / | \ | / |' )
    print('1   '+ temp[1][0]+fg("white") + '---'+temp[1][1]+fg("white") + '---'+temp[1][2]+fg("white") + '---'+temp[1][3]+fg("white") + '---'+temp[1][4])
    print('    '+fg("white") + '| / | \ | / | \ |' )
    print('2   '+ temp[2][0]+fg("white") + '---'+temp[2][1]+fg("white") + '---'+temp[2][2]+fg("white") + '---'+temp[2][3]+fg("white") + '---'+temp[2][4])
    print('    '+fg("white") + '| \ | / | \ | / |' )
    print('3   '+ temp[3][0]+fg("white") + '---'+ temp[3][1]+fg("white") + '---'+temp[3][2]+fg("white") + '---'+temp[3][3]+fg("white") + '---'+temp[3][4])
    print('    '+fg("white") + '| / | \ | / | \ |' )
    print('4   '+ temp[4][0]+fg("white") + '---'+ temp[4][1]+fg("white") + '---'+temp[4][2]+fg("white") + '---'+ temp[4][3]+fg("white") + '---'+temp[4][4])
    print(fg("white") + '' )

def inputMove(): pass


def play():
    print("You play X")

    prev_board = None
    board = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, -1], [-1, 0, 0, 0, -1], [-1, -1, -1, -1, -1]]
    printBoard(board)

    temp_pieces = set()
    step = 0
    while step < 50:

        input_move = list(map(int, input("Your move: ").split()))
        src_x = input_move[0]
        src_y = input_move[1]
        dest_x = input_move[2]
        dest_y = input_move[3]
        x_move = ((src_x, src_y), (dest_x, dest_y))

        # x_move = random_move(prev_board, board, -1)

        # x_move = bad_machine_move(prev_board, board, -1, 999, 999)


        prev_board = copy.deepcopy(board)
        act_move(board, x_move, -1, temp_pieces)

        print("After your move:")
        printBoard(board)
        if end_game(board): 
            # print("Step = ", step)
            return

        machine_move = move(prev_board, board, 1, 999, 999)

        prev_board2 = copy.deepcopy(board)
        act_move(board, machine_move, 1, temp_pieces)

        print("After machine move: ", machine_move[0], " --> ", machine_move[1])
        printBoard(board)
        if end_game(board): 
            # print("Step = ", step)
            return

        traps = check_trap(prev_board2, board, -1)
        
        if traps:
            print("Cac nuoc di bay:")
            for trap in traps:
                print(trap[0]," --> ",trap[1])


        step += 1
        print("Step = ", step)



play()




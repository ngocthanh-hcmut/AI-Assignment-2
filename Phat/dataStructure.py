def vitri(board, pos):
    hang = pos[0]
    cot = pos[1]    
    return board[hang][cot]

def oTrong(board, pos):
    return vitri(board, pos) == 0

def chonQuan(board, pos, player):
    return player == vitri(board, pos)


    
    
         

def kiemTraDiChuyenHopLe(board, move, player):
    oldPos = move[0]
    nextPos = move[1]


def coTheGanh(board, move, player):
    pass

def coTheVay(board, move, player):
    pass

def coTheMo(board, move, player):
    pass

def 
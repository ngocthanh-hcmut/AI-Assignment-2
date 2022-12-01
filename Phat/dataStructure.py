

def vitri(board, pos):
    hang = pos[0]
    cot = pos[1]
    if (hang < 0) or (cot < 0) or (hang > 4) or (cot > 4):
        return None    
    return board[hang][cot]

def oTrong(board, pos):
    return vitri(board, pos) == 0

def gocDiChuyen(pos):
    if pos == (0,0):
        return [(0,1), (1,0), (1,1)]
    elif pos == (0,4):
        return [(0,3), (1,4), (1,3)]
    elif pos == (4,0):
        return [(4,1), (3,0), (3,1)]
    elif pos == (4,4):
        return [(4,3), (3,4), (3,3)]
    else:
        return None

def tamBienDIChuyen(pos):
    if pos == (0,2):
        return [(0,1), (0,3), (1,1), (1,2), (1,3)]
    elif pos == (2,4):
        return [(1,4), (3,4), (1,3), (2,3), (3,3)]
    elif pos == (4,2):
        return [(4,1), (4,3), (3,3), (3,2), (3,1)]
    elif pos == (2,0):
        return [(1,0), (3,0), (1,1), (2,1), (3,1)]
    else:
        return None
    

def luatDiChuyen(oldPos, nextPos):
    doDichChuyen = 

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
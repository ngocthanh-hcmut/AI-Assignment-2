testingBoard=[
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, -1],
    [-1, 0, 0, 0, -1],
    [-1, -1, -1, -1, -1]
    ];



# =======================================
VT00 = [ (0,1), (1,1), (1,0) ]  # [(0, 1), (1, 1), (1, 0)]
VT01 = [ (0,2), (1,1), (0,0) ]  # [(0, 2), (1, 1), (0, 0)]
VT02 = [ (0,3), (1,3), (1,2), (1,1), (0,1) ]    # [(0, 3), (1, 3), (1, 2), (1, 1), (0, 1)]
VT03 = [ (0,4), (1,3), (0,2) ]  # [(0, 4), (1, 3), (0, 2)]
VT04 = [ (1,4), (1,3) ,(0,3) ]  # [(1, 4), (1, 3), (0, 3)]
HANG0 = [VT00, VT01, VT02, VT03, VT04]

VT10 = [ (0,0), (1,1), (2,0) ]  # [(0, 0), (1, 1), (2, 0)]
VT11 = [ (0,0), (0,1), (0,2), (1,2), (2,2), (2,1), (2,0), (1,0) ] # [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0)]
VT12 = [ (0,2), (1,3), (2,2), (1,1) ] # [(0, 2), (1, 3), (2, 2), (1, 1)]
VT13 = [ (0,2), (0,3), (0,4), (1,4), (2,4), (2,3), (2,2), (1,2) ] # [(0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (2, 3), (2, 2), (1, 2)]
VT14 = [ (0,4), (2,4), (1,3) ] # [(0, 4), (2, 4), (1, 3)]
HANG1 = [VT10, VT11, VT12, VT13, VT14]

VT20 = [ (1,0), (1,1), (2,1), (3,1), (3,0) ]    # [(1, 0), (1, 1), (2, 1), (3, 1), (3, 0)]
VT21 = [ (1,1), (2,2), (3,1), (2,0) ]   # [(1, 1), (2, 2), (3, 1), (2, 0)]
VT22 = [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (2, 1)]
VT23 = [(1, 3), (2, 4), (3, 3), (2, 2)]
VT24 = [(1, 3), (1, 4), (3, 4), (3, 3), (2, 3)]
HANG2 = [VT20, VT21, VT22, VT23, VT24]

VT30 = [(2, 0), (3, 1), (4, 0)]
VT31 = [(2, 0), (2, 1), (2, 2), (3, 2), (4, 2), (4, 1), (4, 0), (3, 0)]
VT32 = [(2, 2), (3, 3), (4, 2), (3, 1)]
VT33 = [(2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (4, 3), (4, 2), (3, 2)]
VT34 = [(2, 4), (4, 4), (3, 3)]

HANG3 = [VT30,VT31,VT32,VT33,VT34]

VT40 = [(3, 0), (3, 1), (4, 1)]
VT41 = [(3, 1), (4, 2), (4, 0)]
VT42 = [(3, 1), (3, 2), (3, 3), (4, 3), (4, 1)]
VT43 = [(3, 3), (4, 4), (4, 2)]
VT44 = [(3, 3), (3, 4), (4, 3)]
HANG4 = [VT40,VT41,VT42,VT43,VT44]

MOVEGRAPH = [
    HANG0,
    HANG1,
    HANG2,
    HANG3,
    HANG4
]








# =======================================


def hang(pos):
    row = pos[0]
    if row < 0 or row > 4:
        return None
    return row

def cot(pos):
    col = pos[1]
    if col < 0 or col > 4:
        return None
    return col

def vitri(board, pos):
    hang = pos[0]
    cot = pos[1]
    if (hang < 0) or (cot < 0) or (hang > 4) or (cot > 4):
        return None    
    return board[hang][cot]

def kiemTraOTrong(board, pos):
    return vitri(board, pos) == 0


def phamViDiChuyen(pos):
    hang, cot = pos
    if (hang < 0) or (cot < 0) or (hang > 4) or (cot > 4):
        return []
    return MOVEGRAPH[hang][cot]


    


def luatDiChuyen(oldPos, nextPos):
    doDichChuyen = None

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


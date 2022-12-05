import copy

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

class AllPosNow:
    PLAYER = 1
    OPPONENT = -1
    PLAYER_POS = [
        (0,0),
        (0,1),
        (0,2),
        (0,3),
        (0,4),
        (1,4),
        (1,0),
        (2,0)
    ]
    OPPONENT_POS = [
        (4,0),
        (4,1),
        (4,2),
        (4,3),
        (4,4),
        (3,4),
        (2,4),
        (3,0)
    ]
    
    @staticmethod
    def getAllPos(player):
        if player == AllPosNow.PLAYER:
            return AllPosNow.PLAYER_POS
        elif player == AllPosNow.OPPONENT:
            return AllPosNow.OPPONENT_POS
        else:
            return []
        
    @staticmethod
    def replacePosition(oldPos, newPos, listPositions):
        if oldPos in listPositions:
            index = listPositions.index(oldPos)
            listPositions.remove(oldPos)
            listPositions.insert(index, newPos)
            return True
        return False 
        
    @staticmethod
    def replace(oldPos, newPos, player):
        if player == AllPosNow.PLAYER:
            return AllPosNow.replacePosition(oldPos, newPos, AllPosNow.PLAYER_POS)
        elif player == AllPosNow.OPPONENT:
            return AllPosNow.replacePosition(oldPos, newPos, AllPosNow.OPPONENT_POS)
        else:
            return False



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

def setValAt(pos,value,broad):
    h , c = pos
    broad[h][c] = value
    return broad

def kiemTraOTrong(pos, board):
    return vitri(board, pos) == 0

def phamViDiChuyen(pos):
    hang, cot = pos
    if (hang < 0) or (cot < 0) or (hang > 4) or (cot > 4):
        return []
    return MOVEGRAPH[hang][cot]

def chonQuan(player,pos,board):
    return player == vitri(board, pos)

def kiemTraDiChuyenHopLe(player,originPos,desPos, board):
    if chonQuan(player,originPos,board):
        if kiemTraOTrong(desPos, board):
            if desPos in phamViDiChuyen(originPos):
                return True
            return False        
        return False
    return False

def flipAtomic(pos,board):
    giatri = vitri(board,pos)
    if giatri is None:
        return None
    setValAt(pos,-1*giatri,board)
    return board
    
    
def flip(flipPositions,board):
    oldBoard = copy.deepcopy(board)
    for pos in flipPositions:
        flipAtomic(pos,board)
    fliptedBoard = board
    return [oldBoard, fliptedBoard]

def genNextPos(player, allPos, board):
    pass

def coTheGanh(board, move, player):
    pass

def coTheVay(board, move, player):
    pass

def coTheMo(board, move, player):
    pass



# print(testingBoard)
# p = (0, 1)
# setValAt(p, 8, testingBoard)
# print(testingBoard)
# lst = [
#     (0,0),
#     (0,2),
#     (4,4),
#     (2,2),
#     (3,0)
# ]

# print(testingBoard)
# oldb , newb=flip(lst,testingBoard)
# print(testingBoard)
# print(oldb)
# print(newb)



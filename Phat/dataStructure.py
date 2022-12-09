import copy
import queue


testingBoard=[
    # 0   1   2   3   4
    [ 1 , 1 , 1 , 1 , 1 ],  # 0
    [ 1 , 0 , 0 , 0 , 1 ],  # 1
    [ 1 , 0 , 0 , 0 ,-1 ],  # 2
    [-1 , 0 , 0 , 0 ,-1 ],  # 3
    [-1 ,-1 ,-1 ,-1 ,-1 ]   # 4
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

DIEMDICHEO = [
    (1,1),
    (1,4),
    (2,2),
    (3,1),
    (3,3)
]

class BoardManager:
    PLAYER = 1
    OPPONENT = -1
    def __init__(self, initBoard):
        self.board = initBoard
        self.PLAYER_POS = []
        self.OPPONENT_POS = []
        self.initProcess()
    
    def initProcess(self):
        for h in range(0,5):
            for c in range(0,5):
                pos = (h,c)
                if vitri(self.board, pos) == BoardManager.PLAYER:
                    self.PLAYER_POS.append(pos)
                elif vitri(self.board, pos) == BoardManager.OPPONENT:
                    self.OPPONENT_POS.append(pos)
                
    def getAllPos(self,player):
        if player == BoardManager.PLAYER:
            return self.PLAYER_POS
        elif player == BoardManager.OPPONENT:
            return self.OPPONENT_POS
        else:
            return []
        
    def replacePosition_in_POS(self, oldPos, newPos, listPositions):
        if (oldPos in listPositions) and (newPos not in listPositions):
            index = listPositions.index(oldPos)
            listPositions.remove(oldPos)
            listPositions.insert(index, newPos)
            return True
        return False             
    
    def replace_in_POS(self, oldPos, newPos, player):
        if player == BoardManager.PLAYER:
            return self.replacePosition_in_POS(oldPos, newPos, self.PLAYER_POS)
        elif player == BoardManager.OPPONENT:
            return self.replacePosition_in_POS(oldPos, newPos, self.OPPONENT_POS)
        else:
            return False


# class ABCD_EFG:
#     PLAYER = 1
#     OPPONENT = -1
#     PLAYER_POS = [
#         (0,0),
#         (0,1),
#         (0,2),
#         (0,3),
#         (0,4),
#         (1,4),
#         (1,0),
#         (2,0)
#     ]
#     OPPONENT_POS = [
#         (4,0),
#         (4,1),
#         (4,2),
#         (4,3),
#         (4,4),
#         (3,4),
#         (2,4),
#         (3,0)
#     ]
    
#     @staticmethod
#     def getAllPos(player):
#         if player == ABCD_EFG.PLAYER:
#             return ABCD_EFG.PLAYER_POS
#         elif player == ABCD_EFG.OPPONENT:
#             return ABCD_EFG.OPPONENT_POS
#         else:
#             return []
        
#     @staticmethod
#     def replacePosition(oldPos, newPos, listPositions):
#         if oldPos in listPositions:
#             index = listPositions.index(oldPos)
#             listPositions.remove(oldPos)
#             listPositions.insert(index, newPos)
#             return True
#         return False 
        
#     @staticmethod
#     def replace(oldPos, newPos, player):
#         if player == ABCD_EFG.PLAYER:
#             return ABCD_EFG.replacePosition(oldPos, newPos, ABCD_EFG.PLAYER_POS)
#         elif player == ABCD_EFG.OPPONENT:
#             return ABCD_EFG.replacePosition(oldPos, newPos, ABCD_EFG.OPPONENT_POS)
#         else:
#             return False



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

def dilen(pos):
    if pos[0] <=0:
        return None
    return (pos[0]-1,pos[1])

def dixuong(pos):
    if pos[0] >=4:
        return None
    return (pos[0]+1,pos[1])

def sangtrai(pos):
    if pos[1] <=0:
        return None    
    return ( pos[0],pos[1]-1)

def sangphai(pos):
    if pos[1] >=4:
        return None
    return ( pos[0],pos[1]+1)


def cheoLenTrai(pos):
    if pos[0] <=0 or pos[1] <=0:
        return None
    return (pos[0]-1, pos[1]-1 ) 

def cheoLenPhai(pos):
    if pos[0] <= 0 or pos[1] >=4:
        return None
    return (pos[0]-1, pos[1]+1 ) 

def cheoXuongTrai(pos):
    if pos[0] >=4 or pos[1] <= 0:
        return None
    return (pos[0]+1, pos[1]-1 ) 

def cheoXuongPhai(pos):
    if pos[0] >= 4 or pos[1] >= 4:
        return None
    return (pos[0]+1, pos[1]+1 ) 

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

# def cotheden(originPos,desPos, board):
#     if kiemTraOTrong(desPos, board):
#         if desPos in phamViDiChuyen(originPos):
#             return True
#         return False        
#     return False

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

# def genMove(player, board):
#     viTricacQuanCo = ABCD_EFG.getAllPos(player);
#     moveList = []    
#     if viTricacQuanCo:
#         for pos in viTricacQuanCo:
#             phamvi = phamViDiChuyen(pos)
#             for des in phamvi:
#                 if kiemTraOTrong(des,board):
#                     move = (pos,des)
#                     moveList.append(move)        
#     return moveList


# def genMove(player, board):
#     viTricacQuanCo = ABCD_EFG.getAllPos(player);
#     moveList = []    
#     if viTricacQuanCo:
#         for pos in viTricacQuanCo:
#             phamvi = phamViDiChuyen(pos)
#             for des in phamvi:
#                 if kiemTraOTrong(des,board):
#                     move = (pos,des)
#                     moveList.append(move)        
#     return moveList
                
                
        
    
def giuaHangNgang(pos):
    c = cot(pos)
    return ( c > 0 and c < 4 )

def giuaHangDoc(pos):
    h = hang(pos)
    return ( h > 0 and h < 4 )

def giuaHangCheo(pos):
    return pos in DIEMDICHEO
    
def coTheGanhNgang(player, pos, board):
    ganh = []
    if giuaHangNgang(pos):
        t = sangtrai(pos)
        p = sangphai(pos)
        vt = vitri(board,t)
        vp = vitri(board,p)
        if (vp != 0) and (vt == vp) and (vp == -1* player):
            ganh.append(t)
            ganh.append(p)
    return ganh

def coTheGanhDoc(player, pos, board):
    ganh = []
    if giuaHangDoc(pos):
        t = dilen(pos)
        d = dixuong(pos)
        vt = vitri(board,t)
        vd = vitri(board,d)
        if (vt != 0) and (vt == vd) and (vd == -1* player):
            ganh.append(t)
            ganh.append(d)
    return ganh

def coTheGanhCheoTrai(player, pos, board):
    ganh = []
    if giuaHangCheo(pos):
        lt = cheoLenTrai(pos)
        xp = cheoXuongPhai(pos)
        vlt = vitri(board,lt)
        vxp = vitri(board,xp)
        if (vxp != 0) and (vlt == vxp) and (vxp == -1* player):
            ganh.append(lt)
            ganh.append(xp)
    return ganh    
    
def coTheGanhCheoPhai(player, pos, board):
    ganh = []
    if giuaHangCheo(pos):
        lp = cheoLenPhai(pos) 
        xt = cheoXuongTrai(pos)
        vlp = vitri(board,lp)
        vxt = vitri(board,xt)
        if (vlp != 0) and (vxt == vlp) and (vlp == -1* player):
            ganh.append(lp)
            ganh.append(xt)        
    return ganh

        

def coTheGanh(player, putpos, board):
    danhSachGanh = []
    
    cheongang = coTheGanhNgang(player,putpos,board)
    if cheongang:
        trai, phai = cheongang
        danhSachGanh.append(trai)
        danhSachGanh.append(phai)
    
    cheodoc = coTheGanhDoc(player, putpos, board)
    if cheodoc:
        tren, duoi = cheodoc
        danhSachGanh.append(tren)
        danhSachGanh.append(duoi)
        
    cheoxientrai = coTheGanhCheoTrai(player, putpos, board)
    if cheoxientrai:
        lentrai,xuongphai = cheoxientrai
        danhSachGanh.append(lentrai)
        danhSachGanh.append(xuongphai)
        
    cheoxienphai = coTheGanhCheoPhai(player, putpos, board)
    if cheoxienphai:
        lenphai, xuongtrai = cheoxienphai
        danhSachGanh.append(lenphai)
        danhSachGanh.append(xuongtrai)
         
    return danhSachGanh


def lanCanCoOtrong(pos,board):
    phamvi = phamViDiChuyen(pos)
    for p in phamvi:
        if kiemTraOTrong(p, board):
            return True
    return False

def oTrongXungQuanh(pos,board):
    phamvi = phamViDiChuyen(pos)
    lst = []
    for p in phamvi:
        if kiemTraOTrong(p, board):
            lst.append(p)
    return lst

def nodeLanCanCungMau(pos, board, notInList = []):
    if kiemTraOTrong(pos,board):
        return []
    valpos = vitri(board, pos)
    phamvi = phamViDiChuyen(pos)
    nodelancan = []
    for p in phamvi:
        if (p not in notInList ) and  (vitri(board, p) == valpos):
            nodelancan.append(p)
    return nodelancan

def nodeLanCanNguocMau(pos, board):
    valpos = vitri(board, pos)
    if valpos == BoardManager.PLAYER or valpos == BoardManager.OPPONENT:
        phamvi = phamViDiChuyen(pos)
        poslistsurround = []
        for p in phamvi:
            if vitri(board, p) == -1* valpos:
                poslistsurround.append(p)
        return poslistsurround    
    return []

            
            
def dichuyen(player,oldpos, despos,board):    
    if kiemTraDiChuyenHopLe(player, oldpos, despos, board):
        newboard = copy.deepcopy(board)
        setValAt(oldpos, 0, newboard)
        setValAt(despos, player, newboard)
        return[newboard, board]        
    else:
        return [None,board]

def getSameColorGraph(pos,board):
    genlist = []
    genlist.append(pos)
    que = queue.Queue()
    que.put(pos)
    while(not que.empty()):
        now = que.get()
        children = nodeLanCanCungMau(now,board,genlist)
        genlist = genlist + children
        [que.put(child) for child in children]
    return genlist
        

def noikhongtrung(list1,list2):
    res = []
    [res.append(x) for x in list2 if x not in list1]
    res = list1 + res
    return res
        
def kiemtrabivaytatca(pos,board):
    """return [bi vay, danhsachvay, danhsachkhongbivay]"""
    if kiemTraOTrong(pos,board):
        return [False,None,None]
    nhomcungmau = getSameColorGraph(pos,board)
    for p in nhomcungmau:
        if lanCanCoOtrong(p,board):
            return [False,[],nhomcungmau]
    return [True,nhomcungmau,[]]


def coTheVay(player, move, board):    
    oldpos,despos = move
    newboard, oldBoard = dichuyen(player,oldpos,despos,board)
    if newboard:
        danhsachkiemtra = nodeLanCanNguocMau(despos,newboard)
        danhsachvay = []
        danhsachkhongvay = []
        for node in danhsachkiemtra:
            if node in danhsachvay:
                continue
            if node in danhsachkhongvay:
                continue
            vay,dsvay,dskhongvay = kiemtrabivaytatca(node,newboard)
            if vay:
                danhsachvay = noikhongtrung(danhsachvay,dsvay)
            else:
                danhsachkhongvay = noikhongtrung(danhsachkhongvay,dskhongvay)
        return danhsachvay
    return []
    
def getMoveFromBoards(prevboard, newboard):
    if prevboard == newboard:
        return [0,None,None]
    hanglist = []
    for h in range(0,len(prevboard)):
        if prevboard[h] != newboard[h]:
            hanglist.append(h)
    h1,h2 = hanglist
    
    poslist =[]  
    for c in range(0, len(prevboard[h1])):
        if prevboard[h1][c] != newboard[h1][c]:
            pos1 = (h1,c)
            poslist.append(pos1)
    for c in range(0, len(prevboard[h2])):
        if prevboard[h2][c] != newboard[h2][c]:
            pos2 = (h2,c)
            poslist.append(pos2)
    moveLst = []
    for p in poslist:
        if kiemTraOTrong(p,newboard):
            moveLst.insert(0,p)
        else:
            moveLst.append(p)
            
    val = vitri(newboard,moveLst[1])
    moveLst.insert(0,val)
    
    return moveLst
            

def danhsachquancuanguoichoi(player,board):
    if player == 1 or player == -1 or player == 0:
        lst = []
        for h in range(0,5):
            for c in range(0,5):
                pos = (h,c)
                if vitri(board,pos) == player:
                    lst.append(pos)
        
        return lst
    return []     

def coTheMo(prevboard, newboard):
    opponent, oldpos, newpos = getMoveFromBoards(prevboard, newboard)
    player = -1*opponent
    movelist = []
    listOtrong = oTrongXungQuanh(newpos,newboard)
    playerlst = danhsachquancuanguoichoi(player,newboard)
    for otrong in listOtrong:
        if coTheGanh(player,otrong,newboard):
            diemcothexuatquan = phamViDiChuyen(otrong)
            for p in playerlst:
                if p in diemcothexuatquan: 
                  m = (p,otrong)
                  movelist.append(m)
    
    return movelist
        
    



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



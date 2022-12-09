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
    """lay ra tham so hang"""
    row = pos[0]
    if row < 0 or row > 4:
        return None
    return row

def cot(pos):
    """lay ra tham so cot"""    
    col = pos[1]
    if col < 0 or col > 4:
        return None
    return col

def dilen(pos):
    """ham tao ra vi tri khi quan di len"""
    if pos[0] <=0:
        return None
    return (pos[0]-1,pos[1])

def dixuong(pos):
    """ham tao ra vi tri khi quan di xuong"""    
    if pos[0] >=4:
        return None
    return (pos[0]+1,pos[1])

def sangtrai(pos):
    """ham tao ra vi tri khi quan di trai"""
    if pos[1] <=0:
        return None    
    return ( pos[0],pos[1]-1)

def sangphai(pos):
    """ham tao ra vi tri khi quan di phai"""
    if pos[1] >=4:
        return None
    return ( pos[0],pos[1]+1)

def cheoLenTrai(pos):
    """ham tao ra vi tri khi quan di cheo len trai"""
    
    if pos[0] <=0 or pos[1] <=0:
        return None
    return (pos[0]-1, pos[1]-1 ) 

def cheoLenPhai(pos):
    """ham tao ra vi tri khi quan di cheo len phai"""    
    if pos[0] <= 0 or pos[1] >=4:
        return None
    return (pos[0]-1, pos[1]+1 ) 

def cheoXuongTrai(pos):
    """ham tao ra vi tri khi quan di cheo xuong trai"""
    if pos[0] >=4 or pos[1] <= 0:
        return None
    return (pos[0]+1, pos[1]-1 ) 

def cheoXuongPhai(pos):
    """ham tao ra vi tri khi quan di cheo xuong phai"""
    if pos[0] >= 4 or pos[1] >= 4:
        return None
    return (pos[0]+1, pos[1]+1 ) 

def vitri(board, pos):
    """lay ra gia tri cua quan co tai vi tri pos cua ban co board"""
    hang = pos[0]
    cot = pos[1]
    if (hang < 0) or (cot < 0) or (hang > 4) or (cot > 4):
        return None    
    return board[hang][cot]

def setValAt(pos,value,broad):
    """dat gia tri quan co cho vi tri pos cua ban co board"""
    h , c = pos
    broad[h][c] = value
    return broad

def kiemTraOTrong(pos, board):
    """kiem tra vi tri pos cua ban co board co trong hay khong"""
    return vitri(board, pos) == 0

def phamViDiChuyen(pos):
    """trả về phạm vi di chuyển hợp lệ của vị trí pos"""
    hang, cot = pos
    if (hang < 0) or (cot < 0) or (hang > 4) or (cot > 4):
        return []
    return MOVEGRAPH[hang][cot]

def chonQuan(player,pos,board):
    """kiểm tra xem player có thể chọn quân cờ tại vị trí pos của bàn cờ board hay không"""
    return player == vitri(board, pos)

def kiemTraDiChuyenHopLe(player,originPos,desPos, board):
    """kiem tra xem player có di chuyển hợp lệ hay không"""
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
    """kiểm tra xem vi trí pos không nằm trên biên ngang"""
    c = cot(pos)
    return ( c > 0 and c < 4 )

def giuaHangDoc(pos):
    """kiểm tra xem vi trí pos không nằm trên biên dọc"""    
    h = hang(pos)
    return ( h > 0 and h < 4 )

def giuaHangCheo(pos):
    """kiểm tra xem vị trí pos có đi chéo được không"""
    return pos in DIEMDICHEO
    
def coTheGanhNgang(player, pos, board):
    """kiểm tra player tại vi trí pos có thể gánh ngang được không nếu có trả về danh sách"""
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
    """kiểm tra player tại vi trí pos có thể gánh dọc được không nếu có trả về danh sách"""    
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
    """kiểm tra player tại vi trí pos có thể gánh chéo trái được không nếu có trả về danh sách"""    
    
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
    """kiểm tra player tại vi trí pos có thể gánh chéo phải được không nếu có trả về danh sách"""    
    
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
    """trả về danh sách gánh khi player đặt quân tại vị trí putpos của bảng board"""
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
    """kiem tra xem lân cận có ô trong hay không"""
    phamvi = phamViDiChuyen(pos)
    for p in phamvi:
        if kiemTraOTrong(p, board):
            return True
    return False

def oTrongXungQuanh(pos,board):
    """trả về ô trống lân cận"""
    phamvi = phamViDiChuyen(pos)
    lst = []
    for p in phamvi:
        if kiemTraOTrong(p, board):
            lst.append(p)
    return lst

def nodeLanCanCungMau(pos, board, notInList = []):
    """trả về danh sách vị trí cùng màu lân cận không nằm trong notInList"""
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
    """trả về danh sách vị trí ngược màu lân cận"""
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
    """Di chuyen nhung khong doi mau khi co the an quan"""   
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

    changespos = []
    if len(hanglist) == 1 :   # di chuyen ngang
        h = hanglist[0]
        for c in range(0,len(prevboard[h])):
            if prevboard[h][c] != newboard[h][c]:
                p = (h,c)
                changespos.append(p)        
    else:
        h1, h2 = hanglist
        for c in range(0,len(prevboard[h1])):
            if prevboard[h1][c] != newboard[h1][c]:
                p = (h1,c)
                changespos.append(p)
        for c in range(0,len(prevboard[h2])):
            if prevboard[h2][c] != newboard[h2][c]:
                p = (h2,c)
                changespos.append(p)
    movelist = []
    for pos in changespos:
        if kiemTraOTrong(pos,newboard):
            movelist.insert(0,pos)
        else:
            movelist.append(pos)
    
    val = vitri(newboard,movelist[1])
    movelist.insert(0,val)
    return movelist
                
                
            

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
    playerlst = danhsachquancuanguoichoi(player,newboard)
    if coTheGanh(player,oldpos,newboard):
        diemcothexuatquan = phamViDiChuyen(oldpos)
        for playpos in playerlst:
            if playpos in diemcothexuatquan:
                mv = (playpos,oldpos)
                movelist.append(mv)
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



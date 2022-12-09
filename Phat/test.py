from dataStructure import *
import queue
# b = [
#     # 0   1   2   3   4
#     [ 0 , 0 , 0 , 0 , 0 ],  # 0
#     [ 0 , 1 ,-1 ,-1 ,-1 ],  # 1
#     [ 1 , 1 , 0 , 1 ,-1 ],  # 2
#     [ 1 ,-1 ,-1 , 1 , 0 ],  # 3
#     [ 1 , 1 ,-1 , 0 , 0 ]   # 4
#     ];

b = [
    # 0   1   2   3   4
    [ 1 , 1 , 1 , 1 , 1 ],  # 0
    [ 1 , 0 , 0 , 0 , 1 ],  # 1
    [ 1 , 0 , 0 , 0 ,-1 ],  # 2
    [-1 , 0 , 0 , 0 ,-1 ],  # 3
    [-1 ,-1 ,-1 ,-1 ,-1 ]   # 4
    ];




o = (1,1)
d = (2,2)
plr = 1
print(
    coTheVay(plr, (o,d),b)
)


# e = getSameColorGrap(p,b)
# e = bivay(p,b)
# print(e)

# [(2, 2), (1, 3), (2, 3), (0, 2), (0, 3), (0, 4), (1, 4), (0, 1), (0, 0), (1, 0), (2, 0)]
# [(2, 2), (1, 3), (2, 3), (0, 2), (0, 3), (0, 4), (1, 4), (0, 1), (0, 0), (1, 0), (2, 0)]
# q = queue.Queue()
# print(q.queue)
# [q.put(query) for query in [1,2,3]]
# print(q.queue)
# a = [1,2,3]
# c = [2,2,5,1]
# print( c + a)
# p = (4,2)
# lancan = nodeLanCanCungMau(p, b,[
#     (2,8)
# ])
# print(lancan)




# print(q.queue)
# for i in range(0,10):
#     q.put(i)
# print(q.queue)
# for i in range(0,10):
#     print(q.get())
# br = BoardManager(b)
# bv  = []
# kbv = []
# p =(2,2)
# pv = phamViDiChuyen(p)
# pnm = nodeLanCanNguocMau(p,b)
# print(pv)
# print(pnm)
# print(bivay(p,b,bv,kbv))
# print(bv)
# print(kbv)


# p = (3,2)
# pv =phamViDiChuyen(p)
# nm = nodeLanCanNguocMau(p,b)
# print(pv)
# print(nm)



# a = coTheVay(1,
#     (
#         (0,2),(1,1)
#     ),
#     b

# )
# print(a)
# t1 = (1,2)
# t2 = (3,4)
# t = (
    # t1,
    # t2
# )
# c , d = t
# print( t[0])
# print( t[1])

# print(c is t1)
# print(d is t2)
# print(c)
# print(d)
# n , o = dichuyen(
#         -1,
#         (0,0),
#         (1,1),
#         b
#     )

# print(n)
# print(o)

# nb = copy.deepcopy(b)
# print('1',b,'\n')
# print('2',nb,'\n')
# setValAt(
#     (0,1),9,nb
# )

# print('3',b,'\n')
# print('4',nb,'\n')


# print('')
# print("1:", b,'\n')
# print("2:", br.board,'\n')
# setValAt(
#     (2,2), -999,br.board
# )
# print("3:", b,'\n')
# print("4:", br.board,'\n')


# nbr = copy.deepcopy(br)
# print(nbr.board == br.board)
# # print(nbr.OPPONENT_POS == br.OPPONENT_POS)
# print(br.board)
# print(nbr.board)
# br.board =1 
# print(br.board)
# print(nbr.board)


# print(id(nbr.board) == id(br.board))
# print()

# print(nbr.PLAYER_POS == br.PLAYER_POS)
# print(id(nbr.PLAYER_POS) == id(br.PLAYER_POS))
# print(nbr.PLAYER_POS)
# print(br.PLAYER_POS)
# nbr.PLAYER_POS = 1
# print("heheh: ",nbr.PLAYER_POS)
# print(br.PLAYER_POS)

# print(nbr.OPPONENT_POS == br.OPPONENT_POS)
# print(id(nbr.OPPONENT_POS) == id(br.OPPONENT_POS))
# print(nbr.OPPONENT_POS)
# print(br.OPPONENT_POS)
# nbr.OPPONENT_POS = 1
# print("heheh: ",nbr.OPPONENT_POS)
# print(br.OPPONENT_POS)



# print(nbr.OPPONENT_POS == br.OPPONENT_POS)
# print(id(nbr.OPPONENT_POS) == id(br.OPPONENT_POS))
# print(lanCanCoOtrong(
#         (0,1),
#         b
#     )
# )
# a = []

# def them(lst):
#     for i in range(0,10):
#         lst.append(i)

# print(a)
# them(a)
# print(a)
# print(br.PLAYER)
# print(br.getAllPos(br.PLAYER))
# o = (0,0)
# n = (4,4)
# print(br.replace_in_POS(o,n,1))
# print(br.getAllPos(br.PLAYER))
# print(br.board)
# print(br.OPPONENT)
# print(br.PLAYER_POS)
# print(br.OPPONENT_POS)
# print(br.getAllPos(br.OPPONENT))

# br = BoardManager(b)
# print(br.board)
# print(br.PLAYER)
# print(br.OPPONENT)
# print(br.PLAYER_POS)
# print(br.getAllPos(br.PLAYER))
# print(br.OPPONENT_POS)
# print(br.getAllPos(br.OPPONENT))
# o = (1,0)
# n = (2,1)
# print(br.getAllPos(br.PLAYER))
# print(br.replace_in_POS(o, n, br.PLAYER))
# print(br.getAllPos(br.PLAYER))

# for i in range(0,5):
    # print(i)

# class A:
#     def c(self):
#         a()
    

# def a():
#     print('ahihi')
    
# b = A()
# b.c()



# o = (4,0)
# o = (0,0)
# n = (4,0)
# print(
#     kiemTraDiChuyenHopLe(AllPosNow.PLAYER,
#         o,
#         n,
#         b
#     )
# )
# print(vitri(b,o))

# print(
#     AllPosNow.PLAYER_POS
# )

# a = AllPosNow.replace(
#     (0,0),(1,1),AllPosNow.PLAYER
# )

# print(
#     AllPosNow.PLAYER_POS
# )

# print(a)

# p = (4,2)
# notinlist = [
#     (4,1),(3,2),(5,5),(4,3)
# ]
# print(
#     nodeLancanCungmau(p,b,notinlist)
# )

# p = (2,2)
# res = coTheGanh(AllPosNow.OPPONENT, p , b)
# print(res)
# a = [()]
# if a :
#     print('hihihi')
# else:
#     print('leuleu')


# a = genMove(AllPosNow.OPPONENT,testingBoard)
# print(a)

# p = ( 4 , 3)
# print(
#     giuaHangDoc(p)
# )

# a = [()]
# if a :
#     print('hihi')
# else:
#     print('hehehe');


# from dataStructure import *

# all = AllPosNow()



    
# o = (2,4)
# n = (0,'W')
# p = -1

# print(all.getAllPos(p))
# print (all.replace(o, n, p))
# print(all.getAllPos(p))

# print(
#     all.replacePosition(
#         o,
#         n,
#         all.PLAYER_POS
#     )
# )
# print(all.PLAYER_POS)

# print(o)


# class A:
#     class_a = 10
#     def __init__(self, a = 3) -> None:
#         self.in_a = a
#         self.in_b = A.class_a
#         A.class_a = 2

# a = A()
# print(a.in_a)
# print(A.class_a)
# print(a.in_b)

# from dataStructure import *
# print(kiemTraOTrong(testingBoard,(2,2)));

# def len(pos):
#     if pos[0] <=0:
#         return None
#     return (pos[0]-1,pos[1])

# def xuong(pos):
#     if pos[0] >=4:
#         return None
#     return (pos[0]+1,pos[1])

# def trai(pos):
#     if pos[1] <=0:
#         return None    
#     return ( pos[0],pos[1]-1)

# def phai(pos):
#     if pos[1] >=4:
#         return None
#     return ( pos[0],pos[1]+1)


# def cheoLenTrai(pos):
#     if pos[0] <=0 or pos[1] <=0:
#         return None
#     return (pos[0]-1, pos[1]-1 ) 

# def cheoLenPhai(pos):
#     if pos[0] <= 0 or pos[1] >=4:
#         return None
#     return (pos[0]-1, pos[1]+1 ) 

# def cheoXuongTrai(pos):
#     if pos[0] >=4 or pos[1] <= 0:
#         return None
#     return (pos[0]+1, pos[1]-1 ) 

# def cheoXuongPhai(pos):
#     if pos[0] >= 4 or pos[1] >= 4:
#         return None
#     return (pos[0]+1, pos[1]+1 ) 

# # print(len( (1,2) ))
# # print(xuong( (1,2) ))
# # print(trai( (1,1) ))
# # print(phai( (2,1) ))

# def get( pos ):
#     res = [ cheoLenTrai(pos), len(pos), cheoLenPhai(pos), phai(pos), cheoXuongPhai(pos), xuong(pos), cheoXuongTrai(pos), trai(pos) ]
#     result = list(filter(lambda a: a != None, res))
#     print(result)

# def pget(pos, *fun):
#     res = []
#     for f in fun:
#         res.append(f(pos))
#     print(res)

# # pget(
# #     (0,0),
# #     phai,cheoXuongPhai, xuong
# # )

# # pget(
# #     (0,1),
# #     phai,xuong, trai
# # )

# # pget(
# #     (0,2),
# #     phai,cheoXuongPhai, xuong, cheoXuongTrai, trai
# # )

# # pget(
# #     (0,3),
# #     phai,xuong, trai
# # )

# # pget(
# #     (0,4),
# #     xuong, cheoXuongTrai, trai
# # )

# # pget(
# #     (1,0),
# #     len, phai, xuong
# # )

# # pget(
# #     (1,1),
# #     cheoLenTrai,len , cheoLenPhai, phai, cheoXuongPhai, xuong, cheoXuongTrai, trai
# # )

# # pget(
# #     (1,2),
# #     len, phai, xuong, trai
# # )

# # pget(
# #     (1,3),
# #     cheoLenTrai,len , cheoLenPhai, phai, cheoXuongPhai, xuong, cheoXuongTrai, trai
# # )

# # pget(
# #     (1,4),
# #     len, xuong, trai
# # )


# # pget(
#     # (2,0),
#     # len, cheoLenPhai, phai,cheoXuongPhai ,xuong
# # )

# # pget(
# #     (2,1),
# #     len, phai, xuong, trai
# # )

# # pget(
#     # (2,2),
#     # cheoLenTrai, len, cheoLenPhai, phai, cheoXuongPhai, xuong, cheoXuongTrai, trai
# # )

# # pget(
#     # (2,3),
#     # len, phai, xuong, trai
# # )

# # pget(
#     # (2,4),
#     # cheoLenTrai, len, xuong, cheoXuongTrai, trai
# # )


# # pget(
# #     (3,0),
# #     len, phai, xuong
# # )

# # pget(
# #     (3,1),
# #     cheoLenTrai, len, cheoLenPhai, phai, cheoXuongPhai, xuong, cheoXuongTrai, trai
    
# # )

# # pget(
# #     (3,2),
# #     len, phai, xuong, trai
# # )

# # pget(
# #     (3,3),
# #         cheoLenTrai, len, cheoLenPhai, phai, cheoXuongPhai, xuong, cheoXuongTrai, trai

# # )

# # pget(
# #     (3,4),
# #     len, xuong, trai
# # )


# pget(
#     (4,0),
#     len, cheoLenPhai, phai
# )

# pget(
#     (4,1),
#     len, phai, trai
# )

# pget(
#     (4,2),
#     cheoLenTrai, len, cheoLenPhai, phai, trai
# )

# pget(
#     (4,3),
#     len, phai, trai
# )

# pget(
#     (4,4),
#     cheoLenTrai,len,trai
# )
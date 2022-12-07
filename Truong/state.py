from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
from game import *
from colored import fg
import copy
import threading

game = Game()

class State:
    
    max_depth = 4
    max_score = 0
    min_score = 16
    player = None
    # executor = ThreadPoolExecutor()
    badChoice = []
    goodChoice = []
    normalChoice = []

    def __init__(self, oldBoard, currentBoard, player, depth, start=None, end=None, parent = None) -> None:
        self.parent = parent
        if parent == None:
            State.player = player
        self.board = currentBoard
        self.player = player
        self.score = 0
        self.depth = depth
        self.childrenList = []
        self.start = start
        self.end = end
        self.getScore()
        self.generate(oldBoard, currentBoard)
        # self.showChildren()

    def getScore(self):
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == State.player:
                    self.score += 1
        if self.score > State.max_score and (self.depth == State.max_depth-1 or self.score == 16):
            State.max_score = self.score
        if self.score < State.min_score and (self.depth == State.max_depth-1 or self.score == 0):
            State.min_score = self.score
        return self.score

    def generate(self, oldBoard, currentBoard):
        if self.depth >= State.max_depth-1 or self.score == 0 or self.score == 16: return
        oldPosition = Game.isTrapMove(oldBoard, currentBoard)
        if oldPosition == False:
            self.generateChildren()
        else:
            self.generateTrapChildren(oldPosition)

    def generateChildren(self):
        # print("generating normal children")
        for pos in Game.getPlayerPosition(self.player, self.board):
            for nearbyPos in Game.getSurroundPosition(pos):
                if Game.isEmpty(nearbyPos, self.board):
                    board = copy.deepcopy(self.board)
                    newBoard = Game.move(pos, nearbyPos, board)
                    self.childrenList.append(State(board, newBoard, self.player*-1, self.depth+1, pos, nearbyPos, self))

    # def createChildren(self, startPosition, endPosition):
    #     if Game.isEmpty(endPosition, self.board):
    #         board = copy.deepcopy(self.board)
    #         newBoard = Game.move(startPosition, endPosition, board)
    #         self.childrenList.append(State(board, newBoard, self.player*-1, self.depth+1, startPosition, endPosition, self))

    def generateTrapChildren(self, oldPosition):
        # print("generating trap children")
        # print("generating trap children")

        for pos in Game.getSurroundPosition(oldPosition):
            if Game.getValue(pos, self.board) == self.player:
                board = copy.deepcopy(self.board)
                newBoard = Game.move(pos, oldPosition, board)
                self.childrenList.append(State(board, newBoard, self.player*-1, self.depth+1, pos, oldPosition, self))
        return self.childrenList

    # def getGoodChoice(self):
    #     # print("finding good choice")
    #     if self.depth == 0:
    #         for state in self.childrenList:
    #             if state.getGoodChoice() and (state.start, state.end) not in State.badChoice:
    #                 return (state.start, state.end)
    #         for state in self.childrenList:
    #             if (state.start, state.end) not in State.badChoice:
    #                 return (state.start, state.end)
    #         return State.badChoice[0]
    #     else:
    #         for state in self.childrenList:
    #             if state.getGoodChoice():
    #                 return True
    #         if self.depth == State.max_depth-1 and self.score == State.max_score:
    #             return True
    #         return False

    def getSolution(self):
        if self.depth == 0:
            for state in self.childrenList:
                solution = state.getSolution()
                if "bad" in solution:
                    self.badChoice.append((state.start, state.end))
                if "good" in solution:
                    self.goodChoice.append((state.start, state.end))
                if "normal" in solution:
                    self.normalChoice.append((state.start, state.end))
        else:
            solution = []
            if len(self.childrenList) != 0:
                for state in self.childrenList:
                    sol = state.getSolution()
                    for status in sol:
                        if status not in solution:
                            solution.append(status)
                    if len(solution) == 3:
                        break
                return solution
            else:
                if self.score == State.max_score:
                    return ["good"]
                elif self.score == State.min_score:
                    return ["bad"]
                else:
                    return ["normal"]

    # def getBadChoice(self):
    #     # print("finding badchoice")
    #     if self.depth == 0:
    #         result = []
    #         for state in self.childrenList:
    #             if state.getBadChoice():
    #                 State.badChoice.append((state.start, state.end))
    #         return result
    #     else:
    #         for state in self.childrenList:
    #             if state.getBadChoice():
    #                 return True
    #         if self.depth == State.max_depth and self.score == State.min_score:
    #             return True
    #         return False
    
    def showChildren(self):
        for state in self.childrenList:
            state.print()

    def print(self):
        print('depth = ' + str(self.depth))
        print('    0   1   2   3   4')
        print('')
        print('0   ' +self.char(0,0)+fg('yellow')+'---'+self.char(0,1)+fg('yellow')+'---'+self.char(0,2)+fg('yellow')+'---'+self.char(0,3)+fg('yellow')+'---'+self.char(0,4))
        print('    '+fg('yellow')+'| \ | / | \ | / |')
        print('1   '+self.char(1,0)+fg('yellow')+'---'+self.char(1,1)+fg('yellow')+'---'+self.char(1,2)+fg('yellow')+'---'+self.char(1,3)+fg('yellow')+'---'+self.char(1,4))
        print('    '+fg('yellow')+'| / | \ | / | \ |')
        print('2   '+self.char(2,0)+fg('yellow')+'---'+self.char(2,1)+fg('yellow')+'---'+self.char(2,2)+fg('yellow')+'---'+self.char(2,3)+fg('yellow')+'---'+self.char(2,4))
        print('    '+fg('yellow')+'| \ | / | \ | / |')
        print('3   '+self.char(3,0)+fg('yellow')+'---'+self.char(3,1)+fg('yellow')+'---'+self.char(3,2)+fg('yellow')+'---'+self.char(3,3)+fg('yellow')+'---'+self.char(3,4))
        print('    '+fg('yellow')+'| / | \ | / | \ |')
        print('4   '+self.char(4,0)+fg('yellow')+'---'+self.char(4,1)+fg('yellow')+'---'+self.char(4,2)+fg('yellow')+'---'+self.char(4,3)+fg('yellow')+'---'+self.char(4,4))
        print(fg('white')+'')
        
    def char(self, i,j):
        return fg('red')+'X' if self.board[i][j] == 1 else fg('blue')+'O' if self.board[i][j] == -1 else fg('yellow')+'+'

from concurrent.futures import ThreadPoolExecutor, as_completed, wait, ALL_COMPLETED, FIRST_COMPLETED
from game import *
from colored import fg
import copy
import threading

game = Game()
solutions = None

class State:
    
    max_depth = 3
    max_score = 0
    min_score = 16
    player = None
    executor = ThreadPoolExecutor(max_workers=16)
    generatedState = []

    def __init__(self, oldBoard, currentBoard, player, depth, start=None, end=None, realPlayer = None) -> None:
        if realPlayer != None:
            State.player = realPlayer
        self.board = currentBoard
        self.oldBoard = oldBoard
        self.player = player
        self.score = 0
        self.depth = depth
        self.childrenList = []
        self.start = start
        self.end = end
        self.getScore()
        

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

    def generate(self):
        if self.depth >= State.max_depth-1 or self.score == 0 or self.score == 16: return
        oldPosition = Game.isTrapMove(self.oldBoard, self.board)
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
                    if (pos, nearbyPos, newBoard, self.player*-1) in self.generatedState:
                        continue
                    State.generatedState.append((pos, nearbyPos, newBoard, self.player*-1))
                    self.childrenList.append(State(board, newBoard, self.player*-1, self.depth+1, pos, nearbyPos))

        if self.depth == 0:
            futures = [State.executor.submit(state.generate) for state in self.childrenList]
            print("waiting")
            done, notdone = wait(futures, return_when=ALL_COMPLETED)
            print("done wait")
        else:
            # threadList = [threading.Thread(target=state.generate) for state in self.childrenList]
            # for thread in threadList:
            #     thread.start()
            # for thread in threadList:
            #     thread.join()
            for state in self.childrenList:
                state.generate()

    def generateTrapChildren(self, oldPosition):
        for pos in Game.getSurroundPosition(oldPosition):
            if Game.getValue(pos, self.board) == self.player:
                board = copy.deepcopy(self.board)
                newBoard = Game.move(pos, oldPosition, board)
                if (pos, oldPosition, newBoard, self.player*-1) in State.generatedState:
                    continue
                self.childrenList.append(State(board, newBoard, self.player*-1, self.depth+1, pos, oldPosition))
                State.generatedState.append((pos, oldPosition, newBoard, self.player*-1))

        if self.depth == 0:
            futures = [State.executor.submit(state.generate) for state in self.childrenList]
            done, notdone = wait(futures, return_when=ALL_COMPLETED)
        else:
            for state in self.childrenList:
                state.generate()

    def getSolution(self):
        if self.depth == 0:
            threadList = [threading.Thread(target=self.getSelection, args=(state,)) for state in self.childrenList]
            
            global solutions
            solutions = []
            for thread in threadList:
                thread.start()
            for thread in threadList:
                thread.join()

            for result in solutions:
                if result[2] == "good":
                    return result
            for result in solutions:
                if result[2] == "normal":
                    return result
            for result in solutions:
                if result[2] == "bad":
                    return result
            return False

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

    def getSelection(self, firstState):
        
        # print("getting selection")
        global solutions
        solution = firstState.getSolution()
        if "good" in solution and "bad" not in solution:
            solutions.append( (firstState.start, firstState.end, "good"))
        elif "normal" in solution and "bad" not in solution:
            solutions.append( (firstState.start, firstState.end, "normal"))
        else:
            solutions.append( (firstState.start, firstState.end, 'bad'))

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

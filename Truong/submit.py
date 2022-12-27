

import copy
# from concurrent.futures import ThreadPoolExecutor, as_completed, wait, ALL_COMPLETED, FIRST_COMPLETED
# import threading

class PositionEmpty(Exception):
    pass

class PositionNotEmpty(Exception):
    pass

solutions = None

class State:
    
    max_depth = 3
    max_score = 0
    min_score = 16
    player = None
    # executor = ThreadPoolExecutor(max_workers=16)
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

        for state in self.childrenList:
            state.generate()
        # if self.depth == 0:
        #     # futures = [State.executor.submit(state.generate) for state in self.childrenList]
        #     # print("waiting")
        #     # done, notdone = wait(futures, return_when=ALL_COMPLETED)
        #     # print("done wait")
        #     for state in self.childrenList:
        #         state.generate()
        # else:
        #     # threadList = [threading.Thread(target=state.generate) for state in self.childrenList]
        #     # for thread in threadList:
        #     #     thread.start()
        #     # for thread in threadList:
        #     #     thread.join()
        #     for state in self.childrenList:
        #         state.generate()

    def generateTrapChildren(self, oldPosition):
        for pos in Game.getSurroundPosition(oldPosition):
            if Game.getValue(pos, self.board) == self.player:
                board = copy.deepcopy(self.board)
                newBoard = Game.move(pos, oldPosition, board)
                if (pos, oldPosition, newBoard, self.player*-1) in State.generatedState:
                    continue
                self.childrenList.append(State(board, newBoard, self.player*-1, self.depth+1, pos, oldPosition))
                State.generatedState.append((pos, oldPosition, newBoard, self.player*-1))

        for state in self.childrenList:
            state.generate()
        # if self.depth == 0:
        #     futures = [State.executor.submit(state.generate) for state in self.childrenList]
        #     done, notdone = wait(futures, return_when=ALL_COMPLETED)
        # else:
        #     for state in self.childrenList:
        #         state.generate()

    def getSolution(self):
        if self.depth == 0:
            # threadList = [threading.Thread(target=self.getSelection, args=(state,)) for state in self.childrenList]
            
            global solutions
            solutions = []
            # for thread in threadList:
            #     thread.start()
            # for thread in threadList:
            #     thread.join()

            for state in self.childrenList:
                self.getSelection(state)

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

    # def print(self):
    #     print('depth = ' + str(self.depth))
    #     print('    0   1   2   3   4')
    #     print('')
    #     print('0   ' +self.char(0,0)+fg('yellow')+'---'+self.char(0,1)+fg('yellow')+'---'+self.char(0,2)+fg('yellow')+'---'+self.char(0,3)+fg('yellow')+'---'+self.char(0,4))
    #     print('    '+fg('yellow')+'| \ | / | \ | / |')
    #     print('1   '+self.char(1,0)+fg('yellow')+'---'+self.char(1,1)+fg('yellow')+'---'+self.char(1,2)+fg('yellow')+'---'+self.char(1,3)+fg('yellow')+'---'+self.char(1,4))
    #     print('    '+fg('yellow')+'| / | \ | / | \ |')
    #     print('2   '+self.char(2,0)+fg('yellow')+'---'+self.char(2,1)+fg('yellow')+'---'+self.char(2,2)+fg('yellow')+'---'+self.char(2,3)+fg('yellow')+'---'+self.char(2,4))
    #     print('    '+fg('yellow')+'| \ | / | \ | / |')
    #     print('3   '+self.char(3,0)+fg('yellow')+'---'+self.char(3,1)+fg('yellow')+'---'+self.char(3,2)+fg('yellow')+'---'+self.char(3,3)+fg('yellow')+'---'+self.char(3,4))
    #     print('    '+fg('yellow')+'| / | \ | / | \ |')
    #     print('4   '+self.char(4,0)+fg('yellow')+'---'+self.char(4,1)+fg('yellow')+'---'+self.char(4,2)+fg('yellow')+'---'+self.char(4,3)+fg('yellow')+'---'+self.char(4,4))
    #     print(fg('white')+'')
        
    # def char(self, i,j):
    #     return fg('red')+'X' if self.board[i][j] == 1 else fg('blue')+'O' if self.board[i][j] == -1 else fg('yellow')+'+'


class Game:

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def isEmpty(position, board):
        return board[position[0]][position[1]] == 0

    @staticmethod
    def isBlackChess(position, board):
        return board[position[0]][position[1]] == -1

    @staticmethod
    def isWhiteChess(position, board):
        return board[position[0]][position[1]] == 1

    @staticmethod
    def getValue(position, board):
        return board[position[0]][position[1]]

    @staticmethod
    def clearPosition(position, board):
        if Game.isEmpty(position, board):
            raise PositionEmpty

        board[position[0]][position[1]] = 0
        return board

    @staticmethod
    def insertChess(position, value, board):
        if not Game.isEmpty(position, board):
            raise PositionNotEmpty

        board[position[0]][position[1]] = value
        return board

    @staticmethod
    def hasRightPath(position):
        return position[1] != 4

    @staticmethod
    def hasLeftPath(position):
        return position[1] != 0

    @staticmethod
    def hasTopPath(position):
        return position[0] != 0

    @staticmethod
    def hasBottomPath(position):
        return position[0] != 4

    @staticmethod
    def hasTopLeftPath(position):
        availablePosition = [(1,1), (1,3), (2,2), (2,4), (3,1), (3,3), (4,2), (4,4)]
        return position in availablePosition

    @staticmethod
    def hasTopRightPath(position):
        availablePosition = [(2,0), (1,1), (4,0), (3,1), (2,2), (1,3), (4,2), (3,3)]
        return position in availablePosition

    @staticmethod
    def hasBottomLeftPath(position):
        availablePosition = [(0,2), (1,1), (0,4), (1,3), (2,2), (3,1), (2,4), (3,3)]
        return position in availablePosition

    @staticmethod
    def hasBottomRightPath(position):
        availablePosition = [(2,0), (3,1), (0,0), (1,1), (2,2), (3,3), (0,2), (1,3)]
        return position in availablePosition

    @staticmethod
    def isNakama(position, player, board):
        if Game.isEmpty(position, board) :
            raise PositionEmpty
        return board[position[0]][position[1]] == player
    
    @staticmethod
    def isNakama2(position1, position2, board):
        if Game.isEmpty(position1, board) or Game.isEmpty(position2, board):
            return False
        return board[position1[0]][position1[1]] == board[position2[0]][position2[1]]

    @staticmethod
    def isEnemy(pos, player, board):
        if Game.isEmpty(pos, board):
            return False
        return board[pos[0]][pos[1]] != player

    @staticmethod
    def isEnemy2(position1, position2, board):
        if Game.isEmpty(position1, board) or Game.isEmpty(position2, board):
            return False
        return board[position1[0]][position1[1]] != board[position2[0]][position2[1]]

    @staticmethod
    def flipChess(position, board):
        if Game.isEmpty(position, board):
            raise PositionEmpty
        board[position[0]][position[1]] *= -1
        return board

    @staticmethod
    def hasEnemyLeft(position, board, player):
        if not Game.hasLeftPath(position): return False
        # if Game.isEmpty(position, board): return False
        leftPosition = Game.getLeftPosition(position)
        return Game.isEnemy(leftPosition, player, board)

    @staticmethod
    def hasEnemyRight(position, board, player):
        if not Game.hasRightPath(position): return False
        # if Game.isEmpty(position, board): return False
        rightPosition = Game.getRightPosition(position)
        return Game.isEnemy(rightPosition, player, board)

    @staticmethod
    def hasEnemyTop(position, board, player):
        if not Game.hasTopPath(position): return False
        # if Game.isEmpty(position, board): return False
        topPosition = Game.getTopPosition(position)
        return Game.isEnemy(topPosition, player, board)

    @staticmethod
    def hasEnemyBottom(position, board, player):
        if not Game.hasBottomPath(position): return False
        # if Game.isEmpty(position, board): return False
        bottomPosition = Game.getBotPosition(position)
        return Game.isEnemy(bottomPosition, player, board)

    @staticmethod
    def hasEnemyTopLeft(position, board, player):
        if not Game.hasTopLeftPath(position): return False
        # if Game.isEmpty(position, board): return False
        topLeftPosition = Game.getTopLeftPosition(position)
        return Game.isEnemy(topLeftPosition, player, board)

    @staticmethod
    def hasEnemyTopRight(position, board, player):
        if not Game.hasTopRightPath(position): return False
        # if Game.isEmpty(position, board): return False
        topRightPosition = Game.getTopRightPosition(position)
        return Game.isEnemy(topRightPosition, player, board)

    @staticmethod
    def hasEnemyBotLeft(position, board, player):
        if not Game.hasBottomLeftPath(position): return False
        # if Game.isEmpty(position, board): return False
        botLeftPosition = Game.getBotLeftPositon(position)
        return Game.isEnemy(botLeftPosition, player, board)

    @staticmethod
    def hasEnemyBotRight(position, board, player):
        if not Game.hasBottomRightPath(position): return False
        # if Game.isEmpty(position, board): return False
        botRightPosition = Game.getBotRightPosition(position)
        return Game.isEnemy(botRightPosition, player, board)

    @staticmethod
    def getLeftPosition(position):
        return (position[0], position[1]-1)

    @staticmethod
    def getRightPosition(position):
        return (position[0], position[1]+1)

    @staticmethod 
    def getTopPosition(position):
        return (position[0]-1, position[1])

    @staticmethod
    def getBotPosition(position):
        return (position[0]+1, position[1])

    @staticmethod
    def getTopLeftPosition(position):
        return (position[0]-1, position[1]-1)

    @staticmethod
    def getTopRightPosition(position):
        return (position[0]-1, position[1]+1)

    @staticmethod
    def getBotLeftPositon(position):
        return (position[0]+1, position[1]-1)

    @staticmethod
    def getBotRightPosition(position):
        return (position[0]+1, position[1]+1)
    
    @staticmethod
    def move(fromPos, toPos, board):
        player = Game.getValue(fromPos, board)
        board = copy.deepcopy(board)
        newBoard = Game.clearPosition(fromPos, board)
        newBoard = Game.insertChess(toPos, player, newBoard)
        newBoard = Game.checkMove(toPos, player, newBoard)
        return newBoard
        
    @staticmethod
    def checkMove(newPos, player, board):
        newBoard = board
        if Game.hasEnemyLeft(newPos, newBoard, player) and Game.hasEnemyRight(newPos, newBoard, player):
            newBoard = Game.flipChess(Game.getLeftPosition(newPos), newBoard)
            newBoard = Game.flipChess(Game.getRightPosition(newPos), newBoard)
        if Game.hasEnemyTop(newPos, newBoard, player) and Game.hasEnemyBottom(newPos, newBoard, player):
            newBoard = Game.flipChess(Game.getTopPosition(newPos), newBoard)
            newBoard = Game.flipChess(Game.getBotPosition(newPos), newBoard)
        if Game.hasEnemyTopLeft(newPos, newBoard, player) and Game.hasEnemyBotRight(newPos, newBoard, player):
            newBoard = Game.flipChess(Game.getTopLeftPosition(newPos), newBoard)
            newBoard = Game.flipChess(Game.getBotRightPosition(newPos), newBoard)
        if Game.hasEnemyTopRight(newPos, newBoard, player) and Game.hasEnemyBotLeft(newPos, newBoard, player):
            newBoard = Game.flipChess(Game.getTopRightPosition(newPos), newBoard)
            newBoard = Game.flipChess(Game.getBotLeftPositon(newPos), newBoard)
        
        for i in range(5):
            for j in range(5):
                if Game.isEnemy2((i,j), newPos, newBoard):
                    if Game.isLockedChess((i,j), newBoard, []):
                        newBoard = Game.flipChess((i,j), newBoard)
        return newBoard

    @staticmethod
    def getSurroundPosition(position):
        surroundPosition = []
        if Game.hasLeftPath(position):
            surroundPosition.append(Game.getLeftPosition(position))
        if Game.hasRightPath(position):
            surroundPosition.append(Game.getRightPosition(position))
        if Game.hasTopPath(position):
            surroundPosition.append(Game.getTopPosition(position))
        if Game.hasBottomPath(position):
            surroundPosition.append(Game.getBotPosition(position))
        if Game.hasTopLeftPath(position):
            surroundPosition.append(Game.getTopLeftPosition(position))
        if Game.hasTopRightPath(position):
            surroundPosition.append(Game.getTopRightPosition(position))
        if Game.hasBottomLeftPath(position):
            surroundPosition.append(Game.getBotLeftPositon(position))
        if Game.hasBottomRightPath(position):
            surroundPosition.append(Game.getBotRightPosition(position))
        return surroundPosition

    @staticmethod
    def isLockedChess(position, board, askPosition=[]):
        for pos in Game.getSurroundPosition(position):            
            if Game.isEmpty(pos, board): return False
            if pos in askPosition or Game.isEnemy2(pos, position, board): continue
            if Game.isNakama2(pos, position, board):
                askPosition.append(position)
                if not Game.isLockedChess(pos, board, askPosition):
                    return False
        return True

    @staticmethod 
    def isTrapMove(oldBoard, currentBoard):
        if oldBoard == None:
            return False
        a = 0
        b = 0
        oldPosition, newPosition = Game.findOldAndNewPosition(oldBoard, currentBoard)
        player = Game.getValue(newPosition, currentBoard)
        for i in range(5):
            for j in range(5):
                if oldBoard[i][j] == player:
                    a += 1
                if currentBoard[i][j] == player:
                    b += 1
        if a != b:
            return False
        hasOpponentNearby = False
        for pos in Game.getSurroundPosition(oldPosition):
            if Game.getValue(pos, currentBoard) == player*-1:
                hasOpponentNearby = True
        if Game.hasEnemyLeft(oldPosition, currentBoard, player*-1) and Game.hasEnemyRight(oldPosition, currentBoard, player*-1) and hasOpponentNearby:
            # print("trap detected")
            return oldPosition
        if Game.hasEnemyTop(oldPosition, currentBoard, player*-1) and Game.hasEnemyBottom(oldPosition, currentBoard, player*-1) and hasOpponentNearby:
            # print("trap detected")
            return oldPosition
        if Game.hasEnemyBotLeft(oldPosition, currentBoard, player*-1) and Game.hasEnemyTopRight(oldPosition, currentBoard, player*-1) and hasOpponentNearby:
            # print("trap detected")
            return oldPosition
        if Game.hasEnemyTopLeft(oldPosition, currentBoard, player*-1) and Game.hasEnemyBotRight(oldPosition, currentBoard, player*-1) and hasOpponentNearby:
            # print("trap detected")
            return oldPosition
        
        return False
        


    @staticmethod
    def findOldAndNewPosition(oldBoard, currentBoard):
        oldPosition = None
        newPosition = None
        for i in range(5):
            for j in range(5):
                if not Game.isEmpty((i,j), oldBoard) and Game.isEmpty((i,j), currentBoard):
                    oldPosition = (i,j)
                if Game.isEmpty((i,j), oldBoard) and not Game.isEmpty((i,j), currentBoard):
                    newPosition = (i,j)
                if oldPosition != None and newPosition != None:
                    return oldPosition, newPosition

    @staticmethod
    def count(player, board):
        count = 0
        for i in range(5):
            for j in range(5):
                if board[i][j] == player:
                    count += 1
        return count

    @staticmethod
    def getPlayerPosition(player, board):
        result = []
        for i in range(5):
            for j in range(5):
                if board[i][j] == player:
                    result.append((i,j))
        return result

    # @staticmethod
    # def print(board):
    #     print('')
    #     print('    0   1   2   3   4')
    #     print('')
    #     print('0   ' +Game.char(0,0, board)+fg('yellow')+'---'+Game.char(0,1, board)+fg('yellow')+'---'+Game.char(0,2, board)+fg('yellow')+'---'+Game.char(0,3, board)+fg('yellow')+'---'+Game.char(0,4, board))
    #     print('    '+fg('yellow')+'| \ | / | \ | / |')
    #     print('1   '+Game.char(1,0, board)+fg('yellow')+'---'+Game.char(1,1, board)+fg('yellow')+'---'+Game.char(1,2, board)+fg('yellow')+'---'+Game.char(1,3, board)+fg('yellow')+'---'+Game.char(1,4, board))
    #     print('    '+fg('yellow')+'| / | \ | / | \ |')
    #     print('2   '+Game.char(2,0, board)+fg('yellow')+'---'+Game.char(2,1, board)+fg('yellow')+'---'+Game.char(2,2, board)+fg('yellow')+'---'+Game.char(2,3, board)+fg('yellow')+'---'+Game.char(2,4, board))
    #     print('    '+fg('yellow')+'| \ | / | \ | / |')
    #     print('3   '+Game.char(3,0, board)+fg('yellow')+'---'+Game.char(3,1, board)+fg('yellow')+'---'+Game.char(3,2, board)+fg('yellow')+'---'+Game.char(3,3, board)+fg('yellow')+'---'+Game.char(3,4, board))
    #     print('    '+fg('yellow')+'| / | \ | / | \ |')
    #     print('4   '+Game.char(4,0, board)+fg('yellow')+'---'+Game.char(4,1, board)+fg('yellow')+'---'+Game.char(4,2, board)+fg('yellow')+'---'+Game.char(4,3, board)+fg('yellow')+'---'+Game.char(4,4, board))
    #     print(fg('white')+'')
        
    # @staticmethod
    # def char(i,j, board):
    #     return fg('red')+'X' if board[i][j] == 1 else fg('blue')+'O' if board[i][j] == -1 else fg('yellow')+'+'

def move(prev_board, board, player, remain_time_x, remain_time_o):
    State.max_score = 0
    State.min_score = 16
    State.generatedState = []
    stateTree = State(prev_board, board, player, 0, realPlayer=player)
    # print("generating child")
    stateTree.generate()
    # print("getting solution")
    solution = stateTree.getSolution()
    if solution:
        return (solution[0], solution[1])
    else:
        return None

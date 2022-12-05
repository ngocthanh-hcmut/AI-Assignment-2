from exception import *

class Game:

    def __init__(self, board = [[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,-1],[-1,0,0,0,-1],[-1,-1,-1,-1,-1]]) -> None:
        self.board = board
    
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

    def clearPosition(self, position):
        if Game.isEmpty(position, self.board):
            raise PositionEmpty

        self.board[position[0]][position[1]] = 0

    def insertChess(self, position, value):
        if not Game.isEmpty(position, self.board):
            raise PositionNotEmpty

        self.board[position[0]][position[1]] = value

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

    def flipChess(self, position):
        if Game.isEmpty(position, self.board):
            raise PositionEmpty
        self.board[position[0]][position[1]] *= -1

    @staticmethod
    def hasEnemyLeft(position, board, player):
        if not Game.hasLeftPath(position): return False
        if Game.isEmpty(position, board): return False
        leftPosition = Game.getLeftPosition(position)
        return Game.isEnemy(leftPosition, player, board)

    @staticmethod
    def hasEnemyRight(position, board, player):
        if not Game.hasRightPath(position): return False
        if Game.isEmpty(position, board): return False
        rightPosition = Game.getRightPosition(position)
        return Game.isEnemy(rightPosition, player, board)

    @staticmethod
    def hasEnemyTop(position, board, player):
        if not Game.hasTopPath(position): return False
        if Game.isEmpty(position, board): return False
        topPosition = Game.getTopPosition(position)
        return Game.isEnemy(topPosition, player, board)

    @staticmethod
    def hasEnemyBottom(position, board, player):
        if not Game.hasBottomPath(position): return False
        if Game.isEmpty(position, board): return False
        bottomPosition = Game.getBotPosition(position)
        return Game.isEnemy(bottomPosition, player, board)

    @staticmethod
    def hasEnemyTopLeft(position, board, player):
        if not Game.hasTopLeftPath(position): return False
        if Game.isEmpty(position, board): return False
        topLeftPosition = Game.getTopLeftPosition(position)
        return Game.isEnemy(topLeftPosition, player, board)

    @staticmethod
    def hasEnemyTopRight(position, board, player):
        if not Game.hasTopRightPath(position): return False
        if Game.isEmpty(position, board): return False
        topRightPosition = Game.getTopRightPosition(position)
        return Game.isEnemy(topRightPosition, player, board)

    @staticmethod
    def hasEnemyBotLeft(position, board, player):
        if not Game.hasBottomLeftPath(position): return False
        if Game.isEmpty(position, board): return False
        botLeftPosition = Game.getBotLeftPositon(position)
        return Game.isEnemy(botLeftPosition, player, board)

    @staticmethod
    def hasEnemyBotRight(position, board, player):
        if not Game.hasBottomRightPath(position): return False
        if Game.isEmpty(position, board): return False
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
    
    def move(self, fromPos, toPos):
        player = Game.getValue(fromPos, self.board)
        self.clearPosition(fromPos)
        self.insertChess(toPos, player)
        self.checkMove(toPos, player)
        return Game.count(player, self.board)
        
    def checkMove(self, newPos, player):
        if Game.hasEnemyLeft(newPos, self.board, player) and Game.hasEnemyRight(newPos, self.board, player):
            self.flipChess(Game.getLeftPosition(newPos))
            self.flipChess(Game.getRightPosition(newPos))
        if Game.hasEnemyTop(newPos, self.board, player) and Game.hasEnemyBottom(newPos, self.board, player):
            self.flipChess(Game.getTopPosition(newPos))
            self.flipChess(Game.getBotPosition(newPos))
        if Game.hasEnemyTopLeft(newPos, self.board, player) and Game.hasEnemyBotRight(newPos, self.board, player):
            self.flipChess(Game.getTopLeftPosition(newPos))
            self.flipChess(Game.getBotRightPosition(newPos))
        if Game.hasEnemyTopRight(newPos, self.board, player) and Game.hasEnemyBotLeft(newPos, self.board, player):
            self.flipChess(Game.getTopRightPosition(newPos))
            self.flipChess(Game.getBotLeftPositon(newPos))
        
        for i in range(5):
            for j in range(5):
                if Game.isEnemy2((i,j), newPos, self.board):
                    if Game.isLockedChess((i,j), self.board, []):
                        self.flipChess((i,j))

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
        oldPosition, newPosition = Game.findOldAndNewPosition(oldBoard, currentBoard)
        player = Game.getValue(newPosition, currentBoard)
        hasOpponentNearby = False
        for pos in Game.getSurroundPosition(oldPosition):
            if Game.getValue(pos, currentBoard) == player*-1:
                hasOpponentNearby = True
        if Game.hasEnemyLeft(oldPosition, currentBoard, player*-1) and Game.hasEnemyRight(oldPosition, currentBoard, player*-1) and hasOpponentNearby:
            return True
        if Game.hasEnemyTop(oldPosition, currentBoard, player*-1) and Game.hasEnemyBottom(oldPosition, currentBoard, player*-1) and hasOpponentNearby:
            print("alo")
            return True
        if Game.hasEnemyBotLeft(oldPosition, currentBoard, player*-1) and Game.hasEnemyTopRight(oldPosition, currentBoard, player*-1) and hasOpponentNearby:
            return True
        if Game.hasEnemyTopLeft(oldPosition, currentBoard, player*-1) and Game.hasEnemyBotRight(oldPosition, currentBoard, player*-1) and hasOpponentNearby:
            return True
        
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
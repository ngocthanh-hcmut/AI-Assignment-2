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
        if Game.isEmpty(position, board):
            raise PositionEmpty

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
    def isNakama(pos1, pos2, board):
        if Game.isEmpty(pos1, board) or Game.isEmpty(pos2, board):
            raise PositionEmpty
        return board[pos1[0]][pos1[1]] == board[pos2[0]][pos2[1]]

    @staticmethod
    def isEnemy(pos1, pos2, board):
        if Game.isEmpty(pos1, board) or Game.isEmpty(pos2, board):
            raise PositionEmpty
        return board[pos1[0]][pos1[1]] != board[pos2[0]][pos2[1]]

    def flipChess(self, position):
        if Game.isEmpty(position, self.board):
            raise PositionEmpty
        self.board[position[0]][position[1]] *= -1

    @staticmethod
    def hasEnemyLeft(position, board):
        if Game.isEmpty(position, board):
            raise PositionEmpty

        if not Game.hasLeftPath(position): return False
        leftPosition = (position[0], position[1]-1)
        return Game.isEnemy(position, leftPosition, board)

    @staticmethod
    def hasEnemyRight(position, board):
        if Game.isEmpty(position, board):
            raise PositionEmpty
        
        if not Game.hasRightPath(position): return False
        rightPosition = (position[0], position[1]+1)
        return Game.isEnemy(position, rightPosition, board)

    @staticmethod
    def hasEnemyTop(position, board):
        if Game.isEmpty(position, board):
            raise PositionEmpty

        if not Game.hasTopPath(position): return False
        topPosition = (position[0]-1, position[1])
        return Game.isEnemy(position, topPosition, board)

    @staticmethod
    def hasEnemyBottom(position, board):
        if Game.isEmpty(position, board):
            raise PositionEmpty

        if not Game.hasBottomPath(position): return False
        botPosition = (position[0]+1, position[1])
        return Game.isEnemy(position, botPosition, board)

    @staticmethod
    def hasEnemyTopLeft(position, board):
        if Game.isEmpty(position, board):
            raise PositionEmpty

        if not Game.hasBottomLeftPath(position): return False
        topLeftPosition = (position[0]-1, position[1]-1)
        return Game.isEnemy(position, topLeftPosition, board)

    @staticmethod
    def hasEnemyTopRight(position, board):
        if Game.isEmpty(position, board):
            raise PositionEmpty

        if not Game.hasTopRightPath(position): return False
        topRightPosition = (position[0]-1, position[1]+1)
        return Game.isEnemy(position, topRightPosition, board)

    @staticmethod
    def hasEnemyBotLeft(position, board):
        if Game.isEmpty(position, board):
            raise PositionEmpty
        
        if not Game.hasBottomLeftPath(position): return False
        botLeftPosition = (position[0]+1,position[1]-1)
        return Game.isEnemy(position, botLeftPosition, board)

    @staticmethod
    def hasEnemyBotRight(position, board):
        if Game.isEmpty(position, board):
            raise PositionEmpty

        if not Game.hasBottomRightPath(position): return False
        botRightPosition = (position[0]+1, position[1]+1)
        return Game.isEnemy(position, botRightPosition, board)

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
        value = Game.getValue(fromPos, self.board)
        self.clearPosition(fromPos)
        self.insertChess(toPos, value)
        self.checkMove(toPos)
        
    def checkMove(self, newPos):
        if Game.hasEnemyLeft(newPos, self.board) and Game.hasEnemyRight(newPos, self.board):
            self.flipChess(Game.getLeftPosition(newPos))
            self.flipChess(Game.getRightPosition(newPos))
        if Game.hasEnemyTop(newPos, self.board) and Game.hasEnemyBottom(newPos, self.board):
            self.flipChess(Game.getTopPosition(newPos))
            self.flipChess(Game.getBotPosition(newPos))
        if Game.hasEnemyTopLeft(newPos, self.board) and Game.hasEnemyBotRight(newPos, self.board):
            self.flipChess(Game.getTopLeftPosition(newPos))
            self.flipChess(Game.getBotRightPosition(newPos))
        if Game.hasEnemyTopRight(newPos, self.board) and Game.hasEnemyBotLeft(newPos, self.board):
            self.flipChess(Game.getTopRightPosition(newPos))
            self.flipChess(Game.getBotLeftPositon(newPos))
        
        for i in range(5):
            for j in range(5):
                if Game.isEnemy((i,j), newPos, self.board):
                    if Game.isLockedChess((i,j), self.board):
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
    def isLockedChess(position, board, askPosition=None):
        for pos in Game.getSurroundPosition(position):
            if pos == askPosition: continue
            if Game.isEmpty(pos, board):
                return False
            if Game.isNakama(position, pos, board):
                if not Game.isLockedChess(pos, board, position):
                    return False
        return True




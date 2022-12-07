from game import Game
from state import State
        
game = Game()

def move(old_board, current_board, player, remain_time_x, remain_time_y):
    State.max_score = 0
    State.min_score = 16
    State.badChoice = []
    State.goodChoice = []
    State.normalChoice = []
    stateTree = State(old_board, current_board, player, 0)
    # print("maxscore = " + str(State.max_score))
    stateTree.getSolution()
    # print("good choice: "+str(State.goodChoice))
    for move in State.goodChoice:
        if move not in State.badChoice:
            # print("have a good choice")
            return move
    for move in State.normalChoice:
        if move not in State.badChoice:
            # print("have a normal choice")
            return move
    if len(State.badChoice) != 0:
        # print("have a bad choice")
        return State.badChoice[0]
    else:
        return "huhu"

if __name__ == "__main__":
    running = True
    oldBoard = None
    currentBoard = [
        [ 1, 1, 1, 1, 1],
        [ 1, 0, 0, 0, 1],
        [ 1, 0, 0, 0,-1],
        [-1, 0, 0, 0,-1],
        [-1,-1,-1,-1,-1]
    ]
    Game.print(currentBoard)
    while running: 
        print("computer's turn:")
        aMove = move(oldBoard, currentBoard, 1, 0 , 0)
        if aMove == "huhu":
            print("huhu")
            break
        print("computer's move: "+str(aMove))
        oldBoard = currentBoard
        currentBoard = Game.move(aMove[0], aMove[1], oldBoard)
        if Game.isTrapMove(oldBoard, currentBoard):
            print("Alert: trap move: ")
        Game.print(currentBoard)
        i,j,y,x = input("your turn: ").split()
        i = int(i)
        j = int(j)
        y = int(y)
        x = int(x)
        if i == 0 and j == 0 and y == 0 and x == 0:
            break
        oldBoard = currentBoard
        currentBoard = Game.move((i,j), (y,x), oldBoard)
        if Game.isTrapMove(oldBoard, currentBoard):
            print("Alert: trap move: ")
        Game.print(currentBoard)


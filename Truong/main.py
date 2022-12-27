from game import Game
from state import *
        
game = Game()

def move(prev_board, current_board, player, remain_time_x, remain_time_y):
    State.max_score = 0
    State.min_score = 16
    State.generatedState = []
    stateTree = State(prev_board, current_board, player, 0, realPlayer=player)
    print("generating child")
    stateTree.generate()
    print("getting solution")
    solution = stateTree.getSolution()
    if solution:
        print(solution[2])
        return (solution[0], solution[1])
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
    # currentBoard = [
    #     [ 0, 1, 0,-1,-1],
    #     [ 0, 0,-1,-1,-1],
    #     [ 0, 0,-1, 0,-1],
    #     [ 0,-1,-1,-1,-1],
    #     [ 0, 1, 1, 1,-1]        
    # ]
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
            print(fg("red")+"Alert: trap move: "+fg('white'))
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
            print(fg("red")+"Alert: trap move: "+fg('white'))
        Game.print(currentBoard)


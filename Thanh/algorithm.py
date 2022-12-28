from ds import *
import copy



def move(prev_board, board, player, remain_time_x, remain_time_o):
    (best_score, best_move) = minimax(prev_board, board, player, 0)
    return best_move



def flip(board, dest, player, pieces): # ganh
    result = []

    positions = flippable_positions[dest[0]][dest[1]]

    for i in range(0, len(positions), 2):
        x1 = positions[i][0]
        y1 = positions[i][1]
        x2 = positions[i+1][0]
        y2 = positions[i+1][1]
        
        if (board[x1][y1] == -player and board[x2][y2] == -player):
            result.append(positions[i])
            result.append(positions[i+1])

            pieces.add(positions[i])
            pieces.add(positions[i+1])

            board[x1][y1] = player
            board[x2][y2] = player

    return result



def capture(board, dest, player, pieces): # vay
    visited = [[False for i in range(5)] for j in range(5)]

    opponent_pieces = []
    for player_piece in dest:
        for position in reachable_positions[player_piece[0]][player_piece[1]]:
            if board[position[0]][position[1]] == -player:
                opponent_pieces.append(position)

    # print(opponent_pieces)

    for piece in opponent_pieces:
        if not visited[piece[0]][piece[1]]:
            visiting = [piece]
            valid_moves = 0
            
            i = 0
            while i < len(visiting):
                current = visiting[i]
                visited[current[0]][current[1]] = True

                for neighbor in reachable_positions[current[0]][current[1]]:
                    if board[neighbor[0]][neighbor[1]] == -player and not visited[neighbor[0]][neighbor[1]]:
                        visiting.append(neighbor)
                    elif board[neighbor[0]][neighbor[1]] == 0:
                        valid_moves += 1

                i += 1
        
            if valid_moves == 0:
                for captured_piece in visiting:
                    pieces.add(captured_piece)                    
                    board[captured_piece[0]][captured_piece[1]] = player



# A move is called a trap when it: 1) Don't flip any opponent pieces and 2) Create a flippable position for opponent. When a trap is made, you must go into it.
def check_trap(prev_board, board, player): # bay
    forced_moves = []

    changed_positions = []
    for x in range(5):
        for y in range(5):
            if prev_board[x][y] != board[x][y]:
                changed_positions.append((x,y))
    
    if len(changed_positions) >= 3: return []

    prev_source = changed_positions[0]
    if board[changed_positions[1][0]][changed_positions[1][1]] == 0:
        prev_source = changed_positions[1]


    prev_source_is_a_trap = False
    positions = flippable_positions[prev_source[0]][prev_source[1]]

    for i in range(0, len(positions), 2):
        x1 = positions[i][0]
        y1 = positions[i][1]
        x2 = positions[i+1][0]
        y2 = positions[i+1][1]
        
        if (board[x1][y1] == -player and board[x2][y2] == -player):
            prev_source_is_a_trap = True

    if prev_source_is_a_trap:
        for src in reachable_positions[prev_source[0]][prev_source[1]]:
            if board[src[0]][src[1]] == player:
                forced_moves.append((src, prev_source))

    return forced_moves



def get_valid_moves(prev_board, board, player, pieces):
    valid_moves = []
    
    if prev_board:
        valid_moves = check_trap(prev_board, board, player)

    if not valid_moves:
        for src in pieces:
            destinations = reachable_positions[src[0]][src[1]]

            for dest in destinations:
                if board[dest[0]][dest[1]] == 0:
                    valid_moves.append((src, dest))

    return valid_moves



def act_move(board, move, player, pieces):
    board[move[0][0]][move[0][1]] = 0
    board[move[1][0]][move[1][1]] = player
    
    dest = move[1]
    flipped_pieces = flip(board, dest, player, pieces)
        
    flipped_pieces.append(dest)
    capture(board, flipped_pieces, player, pieces)



def minimax(prev_board, board, player, depth):
    pieces = set()
    for x in range(5):
        for y in range(5):
            if board[x][y] == player:
                pieces.add((x,y))

    if depth == MAX_DEPTH:
        return (evaluate(pieces, prev_board, board, player)/depth, None)
    
    valid_moves = get_valid_moves(prev_board, board, player, pieces)
    
    if not valid_moves:
        return (evaluate(pieces, prev_board, board, player)/depth, None)

    best_score = -999
    best_move = None

    for move in valid_moves:

        next_board = copy.deepcopy(board)
        act_move(next_board, move, player, pieces)
        
        result = minimax(board, next_board, -player, depth+1)

        new_value = -result[0]
        if new_value > best_score:
            best_score = new_value
            best_move = move
    
    return (best_score, best_move)
            
        

def evaluate(pieces, prev_board, board, player):
    if len(pieces) == 16:
        return 999
    elif len(pieces) == 0:
        return -999

    opponent_pieces = []
    for x in range(5):
        for y in range(5):
            if board[x][y] == -player:
                opponent_pieces.append((x,y))

    opponent_valid_moves = get_valid_moves(prev_board, board, -player, opponent_pieces)

    # visited = [[False for i in range(5)] for j in range(5)]

    # opponent_vision = 0
    # while opponent_pieces:
    #     current = opponent_pieces.pop()
        
    #     for neighbor in reachable_positions[current[0]][current[1]]:
    #         if board[neighbor[0]][neighbor[1]] == 0 and visited[neighbor[0]][neighbor[1]] == False:
    #             visited[neighbor[0]][neighbor[1]] = True
    #             opponent_pieces.append(neighbor)
    #             opponent_vision += 1

    return len(pieces)*3 - len(opponent_valid_moves)




    # opponent_pieces = []
    # for x in range(5):
    #     for y in range(5):
    #         if board[x][y] == -player:
    #             opponent_pieces.append((x,y))

    # opponent_valid_moves = get_valid_moves(prev_board, board, -player, opponent_pieces)

    # visited = [[False for i in range(5)] for j in range(5)]

    # opponent_vision = 0
    # while opponent_pieces:
    #     current = opponent_pieces.pop()
        
    #     for neighbor in reachable_positions[current[0]][current[1]]:
    #         if board[neighbor[0]][neighbor[1]] == 0 and visited[neighbor[0]][neighbor[1]] == False:
    #             visited[neighbor[0]][neighbor[1]] = True
    #             opponent_pieces.append(neighbor)
    #             opponent_vision += 1

    # return len(pieces)*3 - opponent_vision

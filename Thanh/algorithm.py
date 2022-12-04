from ds import *


def move(prev_board, board, player, remain_time_x, remain_time_o): pass



def flip(board, dest, player): # ganh
    positions = flippable_positions[dest[0]][dest[1]]

    for i in range(0, len(positions), 2):
        x1 = positions[i][0]
        y1 = positions[i][1]
        x2 = positions[i+1][0]
        y2 = positions[i+1][1]
        if (board[x1][y1] == -player and board[x2][y2] == -player):
            player_pieces[player].add(positions[i])
            player_pieces[player].add(positions[i+1])
            
            player_pieces[-player].remove(positions[i])
            player_pieces[-player].remove(positions[i+1])

            board[x1][y1] == player
            board[x2][y2] == player



def capture(board, player): # vay
    visited = [[False for i in range(5)] for j in range(5)]
    pieces = player_pieces[player]

    for piece in pieces:
        if not board[piece[0]][piece[1]]:
            visiting = [piece]
            valid_moves = 0
            
            i = 0
            while i < len(visiting):
                current = visiting[i]
                visited[current[0]][current[1]] = True

                for neighbor in reachable_positions[current[0]][current[1]]:
                    if board[neighbor[0]][neighbor[1]] == player and not visited[neighbor[0]][neighbor[1]]:
                        visiting.append(neighbor)
                    elif board[neighbor[0]][neighbor[1]] == 0:
                        valid_moves += 1

                i += 1
        
            if valid_moves == 0:
                for captured_piece in visiting:
                    player_pieces[player].add(captured_piece)                    
                    player_pieces[-player].remove(captured_piece)
                    board[captured_piece[0]][captured_piece[1]] == player
    


# A move is called a trap when it: 1) Don't flip any opponent pieces and 2) Create a flippable position for opponent. When a trap is made, you must go into it.
def check_trap(prev_board, board, player): # bay
    return [] 



def get_valid_moves(prev_board, board, player):
    valid_moves = check_trap(prev_board, board, player)
    if not valid_moves:
        sources = player_pieces[player]

        for src in sources:
            destinations = reachable_positions[src]

            for dest in destinations:
                if board[dest[0]][dest[1]] == 0:
                    valid_moves.append(src, dest)

    return valid_moves



def act_move(board, move, player):
    board[move[0][0]][move[0][1]] = 0

    flip(board, move[1], player)
    capture(board, -player)



def minimax(): pass



def evaluate(player):
    return len(player_pieces[player])
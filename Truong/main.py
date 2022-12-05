from game import Game
from colored import fg
        
game = Game()
def char(i,j):
    return fg('red')+'X' if game.board[i][j] == 1 else fg('blue')+'O' if game.board[i][j] == -1 else fg('yellow')+'+'

def move(old_board, current_board, player, remain_time_x, remain_time_y):
    pass


if __name__ == "__main__":
    running = True

    while running:
        print('')
        print('    0   1   2   3   4')
        print('')
        print('0   ' +char(0,0)+fg('yellow')+'---'+char(0,1)+fg('yellow')+'---'+char(0,2)+fg('yellow')+'---'+char(0,3)+fg('yellow')+'---'+char(0,4))
        print('    '+fg('yellow')+'| \ | / | \ | / |')
        print('1   '+char(1,0)+fg('yellow')+'---'+char(1,1)+fg('yellow')+'---'+char(1,2)+fg('yellow')+'---'+char(1,3)+fg('yellow')+'---'+char(1,4))
        print('    '+fg('yellow')+'| / | \ | / | \ |')
        print('2   '+char(2,0)+fg('yellow')+'---'+char(2,1)+fg('yellow')+'---'+char(2,2)+fg('yellow')+'---'+char(2,3)+fg('yellow')+'---'+char(2,4))
        print('    '+fg('yellow')+'| \ | / | \ | / |')
        print('3   '+char(3,0)+fg('yellow')+'---'+char(3,1)+fg('yellow')+'---'+char(3,2)+fg('yellow')+'---'+char(3,3)+fg('yellow')+'---'+char(3,4))
        print('    '+fg('yellow')+'| / | \ | / | \ |')
        print('4   '+char(4,0)+fg('yellow')+'---'+char(4,1)+fg('yellow')+'---'+char(4,2)+fg('yellow')+'---'+char(4,3)+fg('yellow')+'---'+char(4,4))
        
        
        
        i, j, y, x = input(fg('white')+"Input move: ").split()
        i = int(i)
        j = int(j)
        x = int(x)
        y = int(y)

        game.move((i,j), (y,x))


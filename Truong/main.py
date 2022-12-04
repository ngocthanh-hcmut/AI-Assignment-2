from game import Game
from colored import fg
        
game = Game()
def char(i,j):
    return fg('red')+'X' if game.board[i][j] == 1 else fg('blue')+'O' if game.board[i][j] == -1 else fg('white')+'+'

if __name__ == "__main__":
    running = True

    while running:
        print(char(0,0)+fg('white')+'---'+char(0,1)+fg('white')+'---'+char(0,2)+fg('white')+'---'+char(0,3)+fg('white')+'---'+char(0,4))
        print(fg('white')+'| \ | / | \ | / |')
        print(char(1,0)+fg('white')+'---'+char(1,1)+fg('white')+'---'+char(1,2)+fg('white')+'---'+char(1,3)+fg('white')+'---'+char(1,4))
        print(fg('white')+'| / | \ | / | \ |')
        print(char(2,0)+fg('white')+'---'+char(2,1)+fg('white')+'---'+char(2,2)+fg('white')+'---'+char(2,3)+fg('white')+'---'+char(2,4))
        print(fg('white')+'| \ | / | \ | / |')
        print(char(3,0)+fg('white')+'---'+char(3,1)+fg('white')+'---'+char(3,2)+fg('white')+'---'+char(3,3)+fg('white')+'---'+char(3,4))
        print(fg('white')+'| / | \ | / | \ |')
        print(char(4,0)+fg('white')+'---'+char(4,1)+fg('white')+'---'+char(4,2)+fg('white')+'---'+char(4,3)+fg('white')+'---'+char(4,4))
        c = input(fg('white')+"Action: ")
        if c == "c":
            running = False

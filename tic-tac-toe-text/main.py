
game = [[-1, -1, -1],
        [-1, -1, -1],
        [-1, -1, -1]]

GAME_MAP = {
    0:"X",
    1:"O    "
}

def check_result(player: int):
    #check for row
    for i in range(0,3):
        if game[i][0]==game[i][1] and game[i][1]==game[i][2] and game[i][0]!=-1 and game[i][0]==player:
            return 1

    #check for col

    for i in range(0, 3):
        if game[0][i] == game[1][i] and game[1][i] == game[2][i] and game[0][i] != -1 and game[0][i] == player:
            return 1

    #check for diagonal
    if (game[0][0]==game[1][1] and game[1][1]==game[2][2] and game[0][0]!=-1 and game[0][0]==player) or (game[0][2]==game[1][1] and game[1][1]==game[2][0] and game[2][0]!=-1 and game[2][0]==player):
        return 1
    return 0

def print_board():
    for i in range(0,3):
        for j in range(0,3):
            if game[i][j]==-1:
                print("", end = " ")
            elif game[i][j]==1:
                print("O", end = " ")
            else:
                print("X", end = " ")
            print("|", end = " ")
        print("")
        print("________")


def play_game(count: int):
    players = []
    turn = False
    count = 0
    print("Welcome to Tic Tac Toe Game!")
    p1 = input('Player 1, Select your symbol(X/O)')
    # players.append(p1)
    if p1 == "X":
        players.append(0)
        players.append(1)
    else:
        players.append(1)
        players.append(0)
    print(f"Player 2's symbol is: {GAME_MAP[players[1]]} ")
    print_board()
    while(1):
        while(1):
            print("Player 1's chance")
            pos = int(input(f"Select a square to enter your {GAME_MAP[players[0]]}"))
            if pos > 9:
                print("Invalid entry!")

            elif pos>=0 and pos<4:
                xcor = 0
                ycor = pos-1
            elif pos>3 and pos<7:
                xcor = 1
                ycor = (pos-1)%3
            else:
                xcor = 2
                ycor = (pos-1)%3
            if game[xcor][ycor]!=-1:
                print("This square already has an entry")
            else:
                game[xcor][ycor] = players[0]
                count+=1
                break
        print_board()

        if check_result(players[0]) == 1:
            print("Player 1 wins!")
            break
        if count==9:
            print("Game tied!")
            break
        while(1):
            print("Player 2's chance")
            pos = int(input(f"Select a square to enter your {GAME_MAP[players[1]]}"))
            if pos>9:
                print("Invalid entry!")
            elif pos >= 0 and pos < 4:
                xcor = 0
                ycor = pos - 1
            elif pos > 3 and pos < 7:
                xcor = 1
                ycor = (pos - 1) % 3
            else:
                xcor = 2
                ycor = (pos - 1) % 3

            if game[xcor][ycor] != -1:
                print("This square already has an entry")
            else:
                game[xcor][ycor] = players[1]
                count += 1
                break
        print_board()
        if check_result(players[1])==1:
            print("Player 2 wins!")
            break
        if count==9:
            print("Game tied!")
            break


if __name__=='__main__':
    play_game(0)
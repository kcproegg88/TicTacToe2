
def check(board):
    done = True
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
        for j in range(3):
            if board[i][j]=='-':
                done = False

    if done:
        return 'done'
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]

    return "-"

def printBoard(board):
    for i in range(3):
        for j in range(3):
            print(f"{board[i][j]}", end="")
        print()


def main():
    board = [["-","-","-"], ["-","-","-"], ["-","-","-"]]
    players = "XO"
    turn = False
    while True:
        print(f"Player {players[turn]}'s turn. Input X Y coordinates")
        printBoard(board)
        while True:
            try:
                x, y = map(int, input().split())
            except ValueError as e:
                print(f"Error {e}")
                print("Try Again")
                continue
            if not 1<= x <= 3 or not 1 <= y <= 3:
                print("Try Again, out of bounds")
            elif board[y-1][x-1] in players:
                print("Try again, position already chosen")
            else:
                break

        board[y-1][x-1] = players[turn]
        result = check(board)
        if result in players:
            print(f"Player {players[turn]} Won.")
            break
        elif result == 'done':
            print("Tie")
            break

        turn = not turn
        print("\n\n")


if __name__ == "__main__":
    main()
def ConstBoard(board):
    print("Current State Of Board : \n")
    for i in range(0, 9):
        if (i > 0) and (i % 3) == 0:
            print("\n")
        if board[i] == 0:
            print("- ", end=" ")
        elif board[i] == 1:
            print("O ", end=" ")
        elif board[i] == -1:
            print("X ", end=" ")
    print("\n")


# This function takes the user move as input and makes the required changes on the board.
def User1Turn(board):
    pos = input("Enter X's position from [1...9]: ")
    pos = int(pos)
    if board[pos - 1] != 0:
        print("Wrong Move!!!")
        exit(0)
    board[pos - 1] = -1


def User2Turn(board):
    pos = input("Enter O's position from [1...9]: ")
    pos = int(pos)
    if board[pos - 1] != 0:
        print("Wrong Move!!!")
        exit(0)
    board[pos - 1] = 1


# MinMax function.
def minimax(board, player):
    x = analyzeboard(board)
    if x != 0:
        return (x * player)
    pos = -1
    value = -2
    for i in range(0, 9):
        if board[i] == 0:
            board[i] = player
            score = -minimax(board, (player * -1))
            board[i] = 0
            if score > value:
                value = score
                pos = i
    if pos == -1:
        return 0
    return value


# This function makes the computer's move using the minmax algorithm.
def CompTurn(board):
    pos = -1
    value = -2
    for i in range(0, 9):
        if board[i] == 0:
            board[i] = 1
            score = -minimax(board, -1)
            board[i] = 0
            if score > value:
                value = score
                pos = i
    board[pos] = 1


# This function is used to analyze a game.
def analyzeboard(board):
    cb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in range(0, 8):
        if (board[cb[i][0]] != 0 and
                board[cb[i][0]] == board[cb[i][1]] and
                board[cb[i][0]] == board[cb[i][2]]):
            return board[cb[i][2]]
    return 0


# Main Function.
def main():
    choice = input("Enter 1 for single player, 2 for multiplayer: ")
    choice = int(choice)
    # The board is considered in the form of a single-dimensional array.
    # One player moves 1 and other moves -1.
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    if choice == 1:
        print("Computer : O Vs. You : X")
        player = input("Enter to play 1(st) or 2(nd): ")
        player = int(player)
        for i in range(0, 9):
            if analyzeboard(board) != 0:
                break
            if (i + player) % 2 == 0:
                CompTurn(board)
            else:
                ConstBoard(board)
                User1Turn(board)

    else:
        for i in range(0, 9):
            if analyzeboard(board) != 0:
                break
            if i % 2 == 0:
                ConstBoard(board)
                User1Turn(board)
            else:
                ConstBoard(board)
                User2Turn(board)

    x = analyzeboard(board)
    ConstBoard(board)
    if x == 0:
        print("Draw!!!")
    elif x == -1:
        print("X Wins!!! You Lose!!!")
    elif x == 1:
        print("X Loses!!! O Wins!!!")


# Start the game
main()



'''Define ConstBoard(board):
    Print current state of the board

Function User1Turn(board):
    Prompt for player X's move and update the board

Function User2Turn(board):
    Prompt for player O's move and update the board

Function minimax(board, player):
    Check board state for a win/loss
    For each cell in the board:
        If cell is empty:
            Simulate player's move
            Call minimax for opponent's turn
            Track best move
    Return best score

Function CompTurn(board):
    Determine computer's move using minimax strategy

Function analyzeboard(board):
    Check all winning combinations and return the result

Function main():
    Prompt user for game mode (single/multiplayer)
    Initialize the game board
    If single-player:
        Loop for player turns and computer moves
    Else:
        Loop for two player turns
    Determine and display the game result
'''
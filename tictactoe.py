from random import randrange

# Defining global properties for the game
board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

computer_player = "X"
human_player = "O"
current_player = human_player
winner = None
game_running = True


# Creation of gameboard
def gameboard(board):
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print("=============")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print("=============")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " | \n")

# Defining player moves between CPU and human
def human_input(board, player):
    if player == human_player:
        move = int(input("Enter a number 1 through 9: \n"))
        if 1 <= move <= 9 and board[move - 1] == "_":
            return move
        else:
            print("The spot is already taken or invalid choice, choose another.\n")
            return human_input(board, player)  # Ask again for a valid move
    else:
        return None

def computer_input(board, player):
    if player == computer_player:
        while True:
            comp_choice = randrange(9)  # Generates a random number between 0 and 8
            if board[comp_choice] == "_":
                return comp_choice + 1  # Return the move (1-9)
    else:
        return None

# Check for win or tie
def check_win_horizontal(board):
    if board[0] == board[1] == board[2] and board[0] != "_":
        return True
    elif board[3] == board[4] == board[5] and board[3] != "_":
        return True
    elif board[6] == board[7] == board[8] and board[6] != "_":
        return True
    return False

def check_win_row(board):
    if board[0] == board[3] == board[6] and board[0] != "_":
        return True
    elif board[1] == board[4] == board[7] and board[1] != "_":
        return True
    elif board[2] == board[5] == board[8] and board[2] != "_":
        return True
    return False

def check_win_diagonal(board):
    if board[0] == board[4] == board[8] and board[0] != "_":
        return True
    elif board[2] == board[4] == board[6] and board[2] != "_":
        return True
    return False

def check_tie(board):
    if "_" not in board:
        gameboard(board)
        print("Cat's game\n:(")
        return True
    return False

# Check for win
def check_win():
    if check_win_diagonal(board) or check_win_horizontal(board) or check_win_row(board):
        return True
    return False

# How the program switches players
def switch_player():
    global current_player
    if current_player == human_player:
        current_player = computer_player
    else:
        current_player = human_player

while game_running:
    gameboard(board)

    move = human_input(board, current_player) if current_player == human_player else computer_input(board,
                                                                                                    current_player)
    if move is not None:
        board[move - 1] = current_player

    if check_win():
        gameboard(board)
        print(f"{current_player} wins!")
        game_running = False
    elif check_tie(board):
        gameboard(board)
        print("It's a cat's game!")
        game_running = False

    switch_player()
import random
import os.path
import json
random.seed()

def draw_board(board):
    # code to draw the board
    print('-----------')
    print('|' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2]+'|')
    print('-----------')
    print('|' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2]+'|')
    print('-----------')
    print('|' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2]+'|')
    print('-----------')

    
def welcome(board):
    '''prints the welcome message
    display the board by calling draw_board(board)'''
    print('Welcome to the "Unbeatable Noughts and crosses" game.\nThe board layout is shown below: ')
    draw_board(board)
    print('When prompted, enter the number corresponding to the square you want.')



def initialise_board(board):
  #Initializes the noughts and crosses board with empty spaces.
    for row in range(0,3):
        for col in range (0,3):
            board[row][col] = " "
    return board

    
def get_player_move(board):
#gets a valid move from the player
    while True:
        try:
            move = int(input("Enter the cell number to place 'X' (1-9): "))
            if 1 <= move <= 9:
                row = (move - 1) // 3
                col = (move - 1) % 3
                if board[row][col] == ' ':
                    return row, col
                else:
                    print("Cell already occupied. Try again.")
            else:
                print("Invalid input. Enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Enter a valid number.")

def choose_computer_move(board):
    #chooses a random move for the computer player
    #used list comprehension to generate moves for computer player.
    #efficiently filters out the empty cells on board, providing a list of available moves
    available_moves = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    row, col = random.choice(available_moves)
    return row, col
               

def check_for_win(board, mark):
    """Checks if a player (X or O) has won.
    """
    if (board[0][0] == mark and board[0][1] == mark and board[0][2] == mark) or \
        (board[1][0] == mark and board[1][1] == mark and board[1][2] == mark) or \
        (board[2][0] == mark and board[2][1] == mark and board[2][2] == mark) or \
        (board[0][0] == mark and board[1][0] == mark and board[2][0] == mark) or \
        (board[0][1] == mark and board[1][1] == mark and board[2][1] == mark) or \
        (board[0][2] == mark and board[1][2] == mark and board[2][2] == mark) or \
        (board[0][0] == mark and board[1][1] == mark and board[2][2] == mark) or \
            (board[0][2] == mark and board[1][1] == mark and board[2][0] == mark):
        return True
    else:
        return False

def check_for_draw(board):
    """Checks if the game is a draw."""
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                return False
    return True
        
def play_game(board):
   #plays the noughts and crosses game
    # board is initialized now board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    initialise_board(board)
    draw_board(board)
    mark = 'X'
    while True:
        if mark == 'X':
            row, col = get_player_move(board)
        else:
            row, col = choose_computer_move(board)

        board[row][col] = mark
        draw_board(board)

        if check_for_win(board, mark):
            print(f"Player '{mark}' wins!")
            return 1 if mark == 'X' else -1
        elif check_for_draw(board):
            print("It's a draw!")
            return 0

        mark = 'O' if mark == 'X' else 'X'
        print("Next move:")

                    
                
def menu():
   

    while True:
        # user input is stored in choice.
        choice = input(
            "1. Play game\n2. Save score in the leaderboard\n3. Display Leaderboard \nq. Quit\nEnter your choice: ")
        # check if choice is a valid data which is (1 to play game, 2, 3, q);
        if choice in ['1', '2', '3', 'q']:
            # if choice is valid it is returned.
            return choice
        else:
            # if choice is not valid loop run continuously.
            print("Invalid input. Please enter a valid choice.")


def load_scores():
#loads scores from the leaderboard file

    try:
        # open the file in read mode
        if os.path.exists('leaderboard.txt'):
            with open("leaderboard.txt", "r") as file:
                leaders = json.load(file)
    except:
        # if the file doesn't exist, create a new dictionary
        leaders = {}

    return leaders

def save_score(score):
#Saves the player's score in the leaderboard file

    name = input("Enter your name: ")
    try:
        if os.path.exists('leaderboard.txt'):            
            with open("leaderboard.txt", "r") as file:
                data = json.load(file)
    except:
        data = {}  # If the file doesn't exist, create a new dictionary
    data[name] = score
    with open("leaderboard.txt", "w") as file:
        json.dump(data, file)


def display_leaderboard(leaders):
 #displays the leaderboard
    print("Leaderboard:\nPLAYER   SCORE")
    for name, score in leaders.items():
        print(f"{name}: {(score)}")
       

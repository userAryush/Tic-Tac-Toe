from noughtsandcrosses_2408485 import *

    
def main():
    # Two Dimension array
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    # Calls Welcome function with argument board.
    welcome(board)
    total_score = 0
    # While is an infinite loop which run continuously until the user press q.
    while True:
        # menu() function is called and its returned value is stored in choice.
        # values of choice are always (1,2,3,q) because menu() only return 1 or 2 or 3 or q otherwise it ask continuously to enter valid data. 
        choice = menu()
        if choice == '1':
            score = play_game(board)
            total_score += score
            print('Your current score is:', total_score)
        if choice == '2':
            save_score(total_score)
        if choice == '3':
            leader_board = load_scores()
            display_leaderboard(leader_board)
        if choice == 'q':
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            print('Good bye')
            return

    
# Program execution begins here
if __name__ == '__main__':
    main()

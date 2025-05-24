import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):

    for row in board:
        print(row)

def play_again_prompt():

    while True:
        try:
            play_again = input('Would you like to play again? (Y/N) ')
            if play_again.upper() not in ('Y', 'N'):
                raise ValueError('Wrong input value.')
        except ValueError:
            print('Please choose Y or N.')
            continue
        else:
            if play_again.upper() == 'Y':
                clear_screen()
                game()
            else:
                print('Thanks for playing! :)')
            break

def is_board_full(board):

    for row in board:
        for col in row:
            if col == " ":
                return
    
    print("Tie!")
    play_again_prompt()



def check_winner(current_player, board):

    is_winner = False

    # check if all markers in the same row are the same
    for row in board:
        if len(set(row)) == 1 and row[0] in ('X', 'O'):
            is_winner = True

    # check if all columns are the same
    for col in zip(*board):
        if len(set(col)) == 1 and col[0] in ('X', 'O'):
            is_winner = True
        
    # check for diagonal win - check if row index == column index
    # defining variables and grabbing currents elements on the board
    diagonal = [board[i][i] for i in range(len(board))]
    anti_diagonal = [board[i][len(board) - 1 - i] for i in range(len(board))]

    # check if elements in the list are the same
    if len(set(diagonal)) == 1 and diagonal[0] in ('X', 'Y'):
        is_winner = True
    if len(set(anti_diagonal)) == 1 and anti_diagonal[0] in ('X', 'Y'):
        is_winner = True


    if is_winner == True:
        print_board(board)
        print(f'{current_player} wins!')
        play_again_prompt()

    

def get_player_input(board):

    while True:
            try:
                row = int( input('Choose a row (0-2): ') )
                if row < 0 or row > 2:
                    raise IndexError("Row out of bounds.")
                
                column = int( input('Choose a column (0-2): '))
                if column < 0 or column > 2:
                    raise IndexError("Column out of bounds.")
                
            except ValueError:
                print('Not an integer. Try again.')
                continue

            except IndexError:
                print("Row or column must be between 0 and 2. Try again.")
                continue
            else: 
                if not " " in board[row][column]:
                    print("Invalid move. Try again.")
                    continue
                else:
                    return (row, column)

def game():
    board = [[" " for _ in range(3)] for _ in range(3)]

    current_player = 'X'
    
    while True:

        print_board(board)

        print(f"{current_player}'s turn")

        row, column = get_player_input(board)
        board[row][column] = current_player

        check_winner(current_player, board)

        is_board_full(board)

        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
            continue


game()
# print_board(game())

    
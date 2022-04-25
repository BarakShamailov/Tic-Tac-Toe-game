import random


# function that print to the user the board
def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('------')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('------')
    print(board[1] + '|' + board[2] + '|' + board[3])


# this function that can take in a player input and assign their marker as 'X' or 'O'.
def player_input():
    marker = ''
    player2 = ''

    while marker != 'X' and marker != 'O':

        marker = input('Please pick to be X or O: ')
        if marker != 'X' and marker != 'O':
            print("You picked wrong choice, please try again")

    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1, player2)


def validiation_digit():
    valid_range = range(1, 10)
    position_user = 'wrong'
    while not position_user.isdigit():
        position_user = input('Please pick position on the board to mark (1-9): ')
        if not position_user.isdigit():
            print('You picked worng choice, please try again')
        else:
            if int(position_user) not in valid_range:
                print("Out of range (1-9)")
                position_user = 'wrong'
                continue

    return int(position_user)


# function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
def place_marker(board, marker, position):
    if marker == 'X':
        board[position] = marker
    else:
        board[position] = marker


# function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
def win_check(board, mark):
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    else:
        return False


# function that  decide which player goes first
def choose_first():
    num = random.randint(1, 2)
    print(f"The player {num} has been chosen to start first")
    return num


# function that returns a boolean indicating whether a space on the board is freely available.
def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False


# function that checks if the board is full and returns a boolean value. True if full, False otherwise.
def full_board(board):
    for i in range(1, len(board)):
        if board[i] == ' ':
            return False

    return True


# function that asks for a player's next position (as a number 1-9) and check if it's a free position. If it is, then return the position for later use.
def player_choice(board):
    next_position = validiation_digit()
    if space_check(board, next_position):
        return next_position

    print("The position has marked")
    return -1


# function that asks the player if they want to play again and returns a boolean True if they do want to play again.
def replay():
    opt = ''
    while opt != 'Y' and opt != 'N':
        opt = input("Please pick Y if you want to play again or N if not: ")

    if opt == 'Y':
        return True
    return False


print('Welcome to Tic Tac Toe game!')

if __name__ == '__main__':
    while True:
        # Set the game up here
        list_board = [' '] * 10
        display_board(list_board)
        # the first player chosen to start
        first_player = choose_first()
        second_player = 0
        if first_player == 2:
            second_player = 1
        else:
            second_player = 2
        game_win = False
        players_symblos = player_input()
        print(f'player {first_player} is: {players_symblos[0]}')
        print(f'player {second_player} is: {players_symblos[1]}')
        counter_first = first_player  # the variable decide who need to start first

        while not game_win:
            # player 1 turn
            if counter_first == 1:
                markP1 = ''
                print("\nplayer 1 turn:")
                positin = player_choice(list_board)
                while positin == -1:
                    positin = player_choice(list_board)
                if first_player == 1:
                    markP1 = players_symblos[0]
                else:
                    markP1 = players_symblos[1]

                place_marker(list_board, markP1, positin)
                display_board(list_board)
                game_win = win_check(list_board, markP1)
                if game_win:
                    print("Congratulations! player 1 you won")
                    break
                if full_board(list_board):
                    print('Draw, no one won...\n')
                    break
                counter_first = 2

            # player 2 turn
            else:
                markP2 = ''
                print("\nplayer 2 turn:")
                positin = player_choice(list_board)
                while positin == -1:
                    positin = player_choice(list_board)
                if first_player == 2:
                    markP2 = players_symblos[0]
                else:
                    markP2 = players_symblos[1]
                place_marker(list_board, markP2, positin)
                display_board(list_board)
                game_win = win_check(list_board, markP2)
                if game_win:
                    print("Congratulations! player 2 you won")
                    break
                if full_board(list_board):
                    print('Draw, no one won...\n')
                    break
                counter_first = 1

        # if the user want to still play or not
        if not replay():
            break

import random

print("Welcome to Olga's Tic Tac Toe\n")
print("You are X")
print("The computer is O\n")
pos = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_board():
    # prints the board showing currently taken positions
    board = f' {pos[0]} | {pos[1]} | {pos[2]} \n' \
            f'-----------\n' \
            f' {pos[3]} | {pos[4]} | {pos[5]} \n' \
            f'-----------\n' \
            f' {pos[6]} | {pos[7]} | {pos[8]} \n'
    print(board)

def computer_play():
    # makes the computer randomly choose a number that was not already taken
    print("It's the computer's turn")
    is_choosing = True
    while is_choosing:
        n = random.randint(1,10)
        if n not in all_numbers:
            computers_choice = n - 1
            pos[computers_choice] = "O"
            all_numbers.append(n)
            all_positions.append(computers_choice)
            print_board()
            print(f"The computer has chosen number {n}\n")
            is_choosing = False
        else:
            is_choosing = True


print_board()
game_on = True
player1_turn = True
all_numbers = []
all_positions = []

while game_on:
    try:
        if player1_turn:
            n = int(input("It's your turn, please select a number: "))
            actual_position = n - 1
            if actual_position not in all_positions:
                pos[actual_position] = "X"
                all_numbers.append(n)
                all_positions.append(actual_position)
                print_board()
                player1_turn = False

            else:
                print("This field is already taken, please try again")

        else:
            computer_play()
            player1_turn = True

    except IndexError:
        print("The number must be between 1 and 9")
    if pos[0] == pos[1] == pos[2] or pos[3] == pos[4] == pos[5] or pos[6] == pos[7] == pos[8] or \
            pos[0] == pos[3] == pos[6] or pos[1] == pos[4] == pos[7] or pos[2] == pos[5] == pos[8] or \
            pos[0] == pos[4] == pos[8] or pos[2] == pos[4] == pos[6]:
        # checks if there's a win by checking if specific positions on the board are all taken
        # by the same symbol, for example three Xs
        if player1_turn:
            print("The computer just won, sorry!")
            game_on = False
            player1_turn = False
        else:
            print("You won the game. Congrats!")
            game_on = False
            player1_turn = False
    elif len(all_numbers) == 9:
        # checks if all the positions have been taken
        game_on = False
        print("It's a draw!")
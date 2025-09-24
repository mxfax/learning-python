game_on = True
player_assignment = True

choice_mapping = {
    "1": (0, 0),
    "2": (0, 1),
    "3": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "7": (2, 0),
    "8": (2, 1),
    "9": (2, 2),
}

#player assignment X or O
first_player = input("Please select if you play with X or O: ").upper().strip()
second_player = ""

while player_assignment:
    if first_player == "X":
        second_player = "O"
        player_assignment = False
    elif first_player == "O":
        second_player = "X"   
        player_assignment = False
    else:
        print("Please input X or O to start the game ")
        first_player = input("Please select if you play with X or O: ").upper().strip()

current_player = first_player

#creating an empty board
playground = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

#cleaning a board for a new game
def create_clean_board():
    playground = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
    return playground

#a hint board to show where to place a sign
playground_hint = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

#printing a game board with borders side by side with hint board
def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1: 
            print("-" * (len(" | ".join(row))))

#updating the current gameboard with hint board on the right side
def update_board(playground):
    for i, (row_playground, row_hint) in enumerate(zip(playground, playground_hint)):
        print(" | ".join(row_playground) + "    " + " | ".join(row_hint))
        if i < 2:
            print("---------" + "    " + "---------")

#checking for a draw once the board is filled
def check_filled_baord(playground):
    board_full = True
    for lists in playground:
        for empty in lists:
            if empty == " ":
                board_full = False
                break
    if board_full == True:
        while True:
            restart = input("Draw, want to play again? Y/N: ").strip().capitalize()
            if restart == "Y":                
                return "restart"
            elif restart == "N":
                return "stop"
            else:
                print("Please write Y or N...")
    return None

#checking for the winner
def check_for_winner(playground):
    # Row checks
    for row in range(3):
        if playground[row][0] == playground[row][1] == playground[row][2] != " ":
            print(f"Player {playground[row][0]} has won!")
            while True:
                restart = input("Play again? Y/N: ").strip().capitalize()
                if restart == "Y":
                    return "restart"
                elif restart == "N":
                    return "stop"
                else:
                    print("Please write Y or N...")

    # Column checks
    for col in range(3):
        if playground[0][col] == playground[1][col] == playground[2][col] != " ":
            print(f"Player {playground[0][col]} has won!")
            while True:
                restart = input("Play again? Y/N: ").strip().capitalize()
                if restart == "Y":
                    return "restart"
                elif restart == "N":
                    return "stop"
                else:
                    print("Please write Y or N...")

    # Diagonal checks
    if playground[0][0] == playground[1][1] == playground[2][2] != " ":
        print(f"Player {playground[0][0]} has won!")
        while True:
            restart = input("Play again? Y/N: ").strip().capitalize()
            if restart == "Y":
                return "restart"
            elif restart == "N":
                return "stop"
            else:
                print("Please write Y or N...")

    if playground[0][2] == playground[1][1] == playground[2][0] != " ":
        print(f"Player {playground[0][2]} has won!")
        while True:
            restart = input("Play again? Y/N: ").strip().capitalize()
            if restart == "Y":
                return "restart"
            elif restart == "N":
                return "stop"
            else:
                print("Please write Y or N...")

    return None

#show the hint board and playground first time
update_board(playground)

#main loop
while game_on:
    result = check_filled_baord(playground)
    winner = check_for_winner(playground)
    if result == "stop" or winner== "stop":
        game_on = False
        break
    elif result == "restart" or winner == "restart":
        playground = create_clean_board()
        current_player=first_player
        update_board(playground)
        continue

    choice = input("Please select where you want to place your symbol (1-9): ")

    #validate input
    if choice not in choice_mapping:
        print("Invalid choice, please pick a number between 1 and 9.")
        continue

    row, col = choice_mapping[choice]

    if playground[row][col] == " ":
        playground[row][col] = current_player
        update_board(playground)
        
        #switching player
        current_player = second_player if current_player == first_player else first_player
    else:
        print("This spot is taken, select a different one...")

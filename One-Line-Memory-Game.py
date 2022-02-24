# -------------------------------------------------------------------------------------------------------------------------------------------------------
# Task: 2, Game Number: 5, Game Name: One line memory game, Algorithm Code Creator: Mohamed Huusein Hassan Mohamed, ID: 20210335.
# Algorithm Descreption: it's a matching game that takes 2 Places from the user, if the places have the same letter then replace them with "*" else pass.
# Version: 1.0 in Date: 22 / 2 / 2022. Started at 12 A:M, Ended at 3:35 A:M.
# Version: 2.0 in Date: 22 / 2 / 2022. Started at 10:40 A:M , Ended at 11:38 A:M.
# Version: 3.0 in Date: 22 / 2 / 2022. Started at 1:00 P:M , Ended at 3:30 P:M.
# Version: 4.0 in Date: 22 / 2 / 2022. Started at 9:20 A:M, Ended at 11:40 P:M.
# Version: 5.0 (The last one) in Date: 23 / 2 / 2022. Started at .Started at 10:15 A:M, Ended at 11:00 A:M.Started again at 2:00 P:M , Ended at 3:30 P:M.
# -------------------------------------------------------------------------------------------------------------------------------------------------------

# import only system from os.
from os import system, name

# import sleep to show output for some time period.
from time import sleep

# define our 2D list of elements ().
global list_of_elem
list_of_elem = [
    [1, 'A'], [2, 'C'],
    [3, 'F'], [4, 'E'],
    [5, 'G'], [6, 'I'],
    [7, 'D'], [8, 'B'],
    [9, 'H'], [0, 'J'],
    [1, 'C'], [2, 'I'],
    [3, 'G'], [4, 'F'],
    [5, 'H'], [6, 'J'],
    [7, 'B'], [8, 'E'],
    [9, 'A'], [0, 'D']
]

# define our list of the numbers we want the user to choose from.
global list_of_chosen
list_of_chosen = []


# Make the list Contain from 1 to 20 to know the choises Removed.
for i in range(1, 21):
    list_of_chosen.append(i)


# define our welcomed function.
def Welcomed():
    print("\nWelcome in One Line Memory Game.")
    print("Max Score in the Game = 20.\n")


# define our clear screen function.
def clear():

    # clear screen for windows
    if name == 'nt':
        _ = system('cls')

    # clear screen for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# define our input from player 1 function.
def player_1_inputs():

    # Show massage that ask to choose a number from the list.
    print("Player #1 Turn => Choose a Number from ", *list_of_chosen)

    while True:  # we used here while true to make the input get more than one if the first was wrong.

        # check the correctness of the input.
        try:

            # get the first element from the user.
            first_elem = int(input("First Element: "))

            if (first_elem not in list_of_chosen) or (first_elem < 1) or (first_elem > 20) or (str(first_elem).isdigit() == False):
                print("Invalid Element, Try again.")
            else:
                break

        except:
            print("Invalid Element, Try again.")

    while True:  # we used here while true to make the input get more than one if the first was wrong.

        # check the correctness of the input.
        try:

            # get the second element from the user.
            second_elem = int(input("Second Element: "))

            if (second_elem not in list_of_chosen) or (second_elem < 1) or (second_elem > 20) or (str(second_elem).isdigit() == False):
                print("Invalid Element, Try again.")
            elif second_elem == first_elem:
                print("Enter different number from the First one.")
            else:
                break

        except:
            print("Invalid Element, Try again.")

    # return the 2 inputs as a tuple to use it below.
    return (first_elem, second_elem)


# define our input from player 2 function. #Same comments like player_1_inputs() comments.
def player_2_inputs():
    print("Player #2 Turn => Choose a Number from ", *list_of_chosen)
    while True:

        try:
            first_elem = int(input("First Element: "))
            if (first_elem not in list_of_chosen) or (first_elem < 1) or (first_elem > 20) or (str(first_elem).isdigit() == False):
                print("Invalid Element, Try again.")
            else:
                break
        except:
            print("Invalid Element, Try again.")

    while True:

        try:
            second_elem = int(input("Second Element: "))
            if (second_elem not in list_of_chosen) or (second_elem < 1) or (second_elem > 20) or (str(second_elem).isdigit() == False):
                print("Invalid Element, Try again.")
            elif second_elem == first_elem:
                print("Enter different number from the First one.")
            else:
                break
        except:
            print("Invalid Element, Try again.")

    return (first_elem, second_elem)


# define our letters that we want to return for players input function.
# the parameter is the tuple that we get from players inputs.
def letters_returned(player):

    # Let the (first_letter) Variable be = the letter of the small list. EX:  first_letter = 'A'
    # define it as a globel variable to use in many functions.
    global first_letter
    first_letter = list_of_elem[player[0]-1][1]

    # Let the (second_letter) Variable be = the letter of the small list. EX:  second_letter = 'B'
    # define it as a globel variable to use in many functions.
    global second_letter
    second_letter = list_of_elem[player[1]-1][1]

    # return the Letters as a tuple to use below.
    return (first_letter, second_letter)


# define our checker for letter if equal or not function.
# the parameters is the letters that we get from letters_returned().
def checker_for_eq_letters(first_letter, second_letter):

    # check if the the 2 letters is equal or not.
    if first_letter == second_letter:
        return True
    else:
        return False


# define our Printing List for the List of elements for players input.
# the parameter is the tuple that we get from players inputs.
def printing_lists(player):

    # we used a for loop to print the list of elements .
    for i in range(1, 21):

        # check if the number i is equal to the inputs from the user or not, if true print the letter not the number, else print the number in the list.
        if i == player[0] or i == player[1]:
            print(list_of_elem[i-1][1], end=' ')
        else:
            print(list_of_elem[i-1][0], end=' ')
    print('\n')


# define our Replace Elements for players function.
# the parameter is the tuple that we get from players inputs.
def replace_elem_for_player(player):

    # print the list.
    printing_lists(player)

    # get the letters from the list.
    letters_returned(player)

    # check if the letters of the numbers that we get from the user is equal or not, if true replace the numbers with '*'.
    if (checker_for_eq_letters(first_letter, second_letter)):

        list_of_elem[player[0]-1][0] = '*'
        list_of_elem[player[1]-1][0] = '*'

        # remove the numbers of the inputs that we get from the user.
        list_of_chosen.remove(player[0])
        list_of_chosen.remove(player[1])

    return list_of_elem  # return the new list of elements after update.


# define our calc Score for players function.
# the parameters is the tuple that we get from players inputs, and score players variable that we define it as a globel variable in the program().
def calc_score_player(player, Score_player):

    # check if the letters are equal or not.
    if (list_of_elem[player[0]-1][1] == list_of_elem[player[1]-1][1]):
        Score_player += 1

    return Score_player  # return the score of the player after update.


# define check end game function.
def check_end_game():

    # if the list of choosen is empty that means that the list of elements become full of '*'.
    if len(list_of_chosen) == 0:
        return False
    else:
        return True


# define our winner function.
# the parameters if the scores of the 2 players.
def check_winner(Score_Player_1, Score_Player_2):

    # printing the score on the screen.
    print("Score Player #1:", Score_Player_1, ".")
    print("Score Player #2:", Score_Player_2, ".")

    if Score_Player_1 > Score_Player_2:
        print("Player #1 Won the Game.\n" + "Thanks for Using My Game.")
    elif Score_Player_2 > Score_Player_1:
        print("Player #2 Won the Game.\n" + "Thanks for Using My Game.")
    else:  # if the 2 scores is equal.
        print("Drow.\n" + "Thanks For Using My Game.\n")


# define our full program function.
def program():

    # define our globel list that will be equal the list of elements after modifing it.
    global list_after_modify

    # define our global Score_Player_1
    Score_Player_1 = 0

    # define our global Score_Player_2
    Score_Player_2 = 0

    Welcomed()  # Start Display the Program.

    while check_end_game():  # while the game deasn't end do this.

        # Player 1 Turn.
        # get input from player 1.
        input_player1 = player_1_inputs()

        # Calc Score for player 1.
        Score_Player_1 = calc_score_player(input_player1, Score_Player_1)

        # replace the correct matching with '*'.
        list_after_modify = replace_elem_for_player(input_player1)

        for list2 in list_after_modify:  # Prints the New List.
            print(list2[0], end=' ')

        print(", Score =", Score_Player_1)  # Print the score of player 1.
        sleep(3)  # Sleap the screan for 3 second only to
        clear()  # clear it.

        # if the list of elements become full of '*' before the player 2 turn, break the loop to end the program.
        if check_end_game() == False:
            break

        # if not go to player 2 turn.
        else:
            # Player 2 Turn.

            # get input from player 2.
            input_player2 = player_2_inputs()

            # Calc Score for player 2.
            Score_Player_2 = calc_score_player(input_player2, Score_Player_2)

            # replace the correct matching with '*'.
            list_after_modify = replace_elem_for_player(input_player2)

            for list2 in list_after_modify:  # Prints the New List.
                print(list2[0], end=' ')

            print(", Score =", Score_Player_2)  # Print the score of player 2.
            sleep(3)  # Sleap the screan for 3 second only to
            clear()  # clear it.

    # Check the Winner from the 2 Players and print the winner on the screen.
    check_winner(Score_Player_1, Score_Player_2)


# Start the Programm.
program()

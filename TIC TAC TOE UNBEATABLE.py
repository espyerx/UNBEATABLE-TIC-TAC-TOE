"""
PROJECT TITLE: TIC TAC TOE
PROJECT DESCRIPTION : HAVE TO MAKE A GAME IN WHICH USER CANT WIN EVER.
THIS GAME IS PROGRAMMED BY MUHAMMAD RAHEEM FROM CS DEPARTMENT (BCT) COMSATS UNIVERSITY ISLAMABAD.
REG.NO: SP21-BCT-O18

"""
"""
Discription:
This program is compact with user input if user enter any digit other then the given it will not give an error else it will ask user to
enter the correct value for example : if the values to enter is B/W 1 to 9 if user enter other than it, it will ask user to enter the value again
"""

import random

# importing random module for toss

print(
    '''
********************************************HEY THERE ! PLAYER WELCOME TO**********************************************
                                                      TIC TAC TOE
****************************************THE GAME WAS GENERATED AND PROGRAMMED BY****************************************
                                                 MUHAMMAD RAHEEM ARIF
******************************************LETS START THE GAME AND HAVE SOME FUN***************************************** 

*******************Note : Please follow the instructions to enjoy the game in its best mode.****************************

********************************************YOU HAVE TO WIN THE GAME BUT YOU CAN'T*******************************************
''')


# printing the welcome note
# making the function of symbol
def symbol(players_symbol):
    while True:
        if players_symbol == 'X' or players_symbol == 'O' or players_symbol == 'o' or players_symbol == 'x':
            break
        else:
            players_symbol = input(" Please choose the correct option X | 0 ")
            continue
    return players_symbol.capitalize()


# making the function for 2D lists and printing them
def print_list(lst):
    print("\n__________________")
    # using nested for loop to print out the list.
    for item in lst:
        for num in item:
            print("|", num, "|", end=' ')

        print("\n__________________")


# making the function to check the win
def win(lst, computer_symbol):
    if (lst[0][0] == computer_symbol and lst[0][1] == computer_symbol and lst[0][2] == computer_symbol) or (
            lst[1][0] == computer_symbol and lst[1][1] == computer_symbol and lst[1][2] == computer_symbol) or (
            lst[2][0] == computer_symbol and lst[2][1] == computer_symbol and lst[2][2] == computer_symbol) or (
            lst[0][0] == computer_symbol and lst[1][0] == computer_symbol and lst[2][0] == computer_symbol) or (
            lst[0][1] == computer_symbol and lst[1][1] == computer_symbol and lst[2][1] == computer_symbol) or (
            lst[0][2] == computer_symbol and lst[1][2] == computer_symbol and lst[2][2] == computer_symbol) or (
            lst[0][0] == computer_symbol and lst[1][1] == computer_symbol and lst[2][2] == computer_symbol) or (
            lst[0][2] == computer_symbol and lst[1][1] == computer_symbol and lst[2][0] == computer_symbol):
        print_list(lst)
        # returning True if  win
        return True
    # returning false if not win
    return False


# printing the player name and ask the player to start the game
def player_name(user1):
    print("Hey! " + str(user1) + " Lets start the Game! ")


# making a function through which list is to be updated on users choice(input)

def choice_list_update(lst, computer_symbol, user1, toss1, toss, players_symbol, lst_2,
                       display_lst):  # assigning the parameters
    i = 0
    if toss1 != toss:
        if lst[1][1] != players_symbol or lst[1][1] != computer_symbol:
            lst[1][1] = computer_symbol
            lst_2[1][1] = computer_symbol
            display_lst.remove(str(5))
            i += 1
    while i < 5:
        # using while loop for counting the turns
        print_list(lst)
        print("you are playing as ", '', players_symbol.capitalize(), '')
        print("please choose from ", display_lst)
        user_input = input(str(user1) + " please enter your value (1 to 9) : ")
        if user_input not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Please choose the correct option ", user1)
            continue
        user_input = int(user_input)
        # assigning the user input into the printed 2Dlist or game board and then passing comparing list

        if lst_2[0][0] == user_input:
            lst[0][0] = players_symbol
            lst_2[0][0] = players_symbol

            comparing_list(lst, players_symbol, computer_symbol, lst_2, user_input, display_lst)
            display_lst.remove(
                str(user_input))  # removing the input  of user from the list of numbers that can be used for turn
            i += 1
            if win(lst, computer_symbol):
                print("the system wins ! ")
                break
            continue



        elif lst_2[0][1] == user_input:
            lst[0][1] = players_symbol
            lst_2[0][1] = players_symbol
            comparing_list(lst, players_symbol, computer_symbol, lst_2, user_input, display_lst)
            display_lst.remove(str(user_input))

            i += 1
            if win(lst, computer_symbol):
                print("the system wins ! ")
                break

            continue




        elif lst_2[0][2] == user_input:
            lst[0][2] = players_symbol
            lst_2[0][2] = players_symbol
            comparing_list(lst, players_symbol, computer_symbol, lst_2, user_input, display_lst)
            display_lst.remove(str(user_input))
            i += 1
            if win(lst, computer_symbol):
                print("the system wins ! ")
                break
            continue


        elif lst_2[1][0] == user_input:
            lst[1][0] = players_symbol
            lst_2[1][0] = players_symbol
            comparing_list(lst, players_symbol, computer_symbol, lst_2, user_input, display_lst)
            display_lst.remove(str(user_input))
            i += 1
            if win(lst, computer_symbol):
                print("the system wins ! ")
                break
            continue



        elif lst_2[1][1] == user_input:
            lst[1][1] = players_symbol
            lst_2[1][1] = players_symbol
            comparing_list(lst, players_symbol, computer_symbol, lst_2, user_input, display_lst)
            display_lst.remove(str(user_input))
            i += 1
            if win(lst, computer_symbol):
                print("the system wins ! ")
                break
            continue



        elif lst_2[1][2] == user_input:
            lst[1][2] = players_symbol
            lst_2[1][2] = players_symbol
            comparing_list(lst, players_symbol, computer_symbol, lst_2, user_input, display_lst)
            display_lst.remove(str(user_input))
            i += 1
            if win(lst, computer_symbol):
                print("the system wins ! ")
                break
            continue

        elif lst_2[2][0] == user_input:
            lst[2][0] = players_symbol
            lst_2[2][0] = players_symbol
            comparing_list(lst, players_symbol, computer_symbol, lst_2, user_input, display_lst)
            display_lst.remove(str(user_input))
            i += 1
            if win(lst, computer_symbol):
                print("the system wins ! ")
                break
            continue


        elif lst_2[2][1] == user_input:
            lst[2][1] = players_symbol
            lst_2[2][1] = players_symbol
            comparing_list(lst, players_symbol, computer_symbol, lst_2, user_input, display_lst)
            display_lst.remove(str(user_input))
            i += 1
            if win(lst, computer_symbol):
                print("the system wins ! ")
                break
            continue

        elif lst_2[2][2] == user_input:
            lst[2][2] = players_symbol
            lst_2[2][2] = players_symbol
            comparing_list(lst, players_symbol, computer_symbol, lst_2, user_input, display_lst)
            display_lst.remove(str(user_input))
            i += 1
            if win(lst, computer_symbol):
                print("the system wins ! ")
                break
            continue


        #
        else:
            print("choose the correct option!  ", user1)

    if i > 4:
        print_list(lst)
        print("the game is draw !")
        # if win become false and i the counter become greater than 4 then the game is draw


# assigning function if comparing list dont have that comparing input
def if_not_in_list(lst, computer_symbol, players_symbol, lst_2, display_lst):
    if lst[0][1] != computer_symbol and lst[0][1] != players_symbol:
        lst[0][1] = computer_symbol
        lst_2[0][1] = computer_symbol
        display_lst.remove(str(2))
    elif lst[0][2] != computer_symbol and lst[0][2] != players_symbol:
        lst[0][2] = computer_symbol
        lst_2[0][2] = computer_symbol
        display_lst.remove(str(3))
    elif lst[1][0] != computer_symbol and lst[1][0] != players_symbol:
        lst[1][0] = computer_symbol
        lst_2[1][0] = computer_symbol
        display_lst.remove(str(4))
    elif lst[1][1] != computer_symbol and lst[1][1] != players_symbol:
        lst[1][1] = computer_symbol
        lst_2[1][1] = computer_symbol
        display_lst.remove(str(5))
    elif lst[1][2] != computer_symbol and lst[1][2] != players_symbol:
        lst[1][2] = computer_symbol
        lst_2[1][2] = computer_symbol
        display_lst.remove(str(6))
    elif lst[2][0] != computer_symbol and lst[2][0] != players_symbol:
        lst[2][0] = computer_symbol
        lst_2[2][0] = computer_symbol
        display_lst.remove(str(7))
    elif lst[2][1] != computer_symbol and lst[2][1] != players_symbol:
        lst[2][1] = computer_symbol
        lst_2[2][1] = computer_symbol
        display_lst.remove(str(8))
    elif lst[2][2] != computer_symbol and lst[2][2] != players_symbol:
        lst[2][2] = computer_symbol
        lst_2[2][2] = computer_symbol
        display_lst.remove(str(9))
    elif lst[0][0] != computer_symbol and lst[0][0] != players_symbol:
        lst[0][0] = computer_symbol
        lst_2[0][0] = computer_symbol
        display_lst.remove(str(1))


# using comparing list to enter the computers turn on the base of users turn
def comparing_list(lst, players_symbol, computer_symbol, lst_2, user_input, display_lst):
    check = 1
    while True:

        if check == 1:
            if players_symbol == lst[0][1] == lst[1][1] == lst[0][2] == lst[1][0] and computer_symbol == lst[0][0] == \
                    lst[1][2] == \
                    lst[2][0]:
                if lst[2][1] != computer_symbol and lst[2][1] != players_symbol and lst[2][1] != user_input:
                    lst[2][1] = computer_symbol
                    lst_2[2][1] = computer_symbol
                    display_lst.remove(str(8))

                    break

            if computer_symbol == lst[0][0] == lst[0][2] or computer_symbol == lst[1][1] == lst[2][1]:  # 2
                if lst[0][1] != computer_symbol and lst[0][1] != players_symbol and lst[0][1] != user_input:
                    lst[0][1] = computer_symbol
                    lst_2[0][1] = computer_symbol
                    display_lst.remove(str(2))

                    break

            if computer_symbol == lst[1][0] == lst[2][0] or computer_symbol == lst[0][1] == lst[0][
                2] or computer_symbol == lst[1][1] == lst[2][2]:  # 1
                if lst[0][0] != computer_symbol and lst[0][0] != players_symbol and lst[0][0] != user_input:
                    lst[0][0] = computer_symbol
                    lst_2[0][0] = computer_symbol
                    display_lst.remove(str(1))

                    break

            if computer_symbol == lst[0][0] == lst[0][1] or computer_symbol == lst[1][2] == lst[2][
                2] or computer_symbol == lst[1][1] == lst[2][0]:  # 3
                if lst[0][2] != computer_symbol and lst[0][2] != players_symbol and lst[0][2] != user_input:
                    lst[0][2] = computer_symbol
                    lst_2[0][2] = computer_symbol
                    display_lst.remove(str(3))

                    break

            if computer_symbol == lst[0][0] == lst[2][0] or computer_symbol == lst[1][1] == lst[1][2]:
                if lst[1][0] != computer_symbol and lst[1][0] != players_symbol and lst[1][0] != user_input:
                    lst[1][0] = computer_symbol
                    lst_2[1][0] = computer_symbol
                    display_lst.remove(str(4))

                    break

            if computer_symbol == lst[0][0] == lst[2][2] or computer_symbol == lst[0][1] == lst[2][
                1] or computer_symbol == lst[0][2] == lst[2][0] or computer_symbol == \
                    lst[1][0] == \
                    lst[1][2]:
                if lst[1][1] != computer_symbol and lst[1][1] != players_symbol and lst[1][1] != user_input:
                    lst[1][1] = computer_symbol
                    lst_2[1][1] = computer_symbol
                    display_lst.remove(str(5))

                    break

            if computer_symbol == lst[1][0] == lst[1][1] or computer_symbol == lst[0][2] == lst[2][2]:
                if lst[1][2] != computer_symbol and lst[1][2] != players_symbol and lst[1][2] != user_input:
                    lst[1][2] = computer_symbol
                    lst_2[1][2] = computer_symbol
                    display_lst.remove(str(6))

                    break

            if computer_symbol == lst[0][0] == lst[1][0] or computer_symbol == lst[2][1] == lst[2][
                2] or computer_symbol == lst[1][1] == lst[0][2]:  # 3
                if lst[2][0] != computer_symbol and lst[2][0] != players_symbol and lst[2][0] != user_input:
                    lst[2][0] = computer_symbol
                    lst_2[2][0] = computer_symbol
                    display_lst.remove(str(7))

                    break

            if computer_symbol == lst[0][1] == lst[1][1] or computer_symbol == lst[2][0] == lst[2][2]:
                if lst[2][1] != computer_symbol and lst[2][1] != players_symbol and lst[2][1] != user_input:
                    lst[2][1] = computer_symbol
                    lst_2[2][1] = computer_symbol
                    display_lst.remove(str(8))

                    break

            if computer_symbol == lst[0][0] == lst[1][1] or computer_symbol == lst[2][0] == lst[2][
                1] or computer_symbol == lst[1][2] == lst[0][2]:  # 3
                if lst[2][2] != computer_symbol and lst[2][2] != players_symbol and lst[2][2] != user_input:
                    lst[2][2] = computer_symbol
                    lst_2[2][2] = computer_symbol
                    display_lst.remove(str(9))

                    break

            if players_symbol == lst[1][0] == lst[2][0] or players_symbol == lst[0][1] == lst[0][2] or players_symbol == \
                    lst[1][1] == lst[2][2]:  # 1
                if lst[0][0] != computer_symbol and lst[0][0] != players_symbol:
                    lst[0][0] = computer_symbol
                    lst_2[0][0] = computer_symbol
                    display_lst.remove(str(1))

                    break

            if players_symbol == lst[0][0] == lst[0][1] or players_symbol == lst[1][2] == lst[2][2] or players_symbol == \
                    lst[1][1] == lst[2][0]:  # 3
                if lst[0][2] != computer_symbol and lst[0][2] != players_symbol:
                    lst[0][2] = computer_symbol
                    lst_2[0][2] = computer_symbol
                    display_lst.remove(str(3))

                    break

            if players_symbol == lst[0][0] == lst[2][0] or players_symbol == lst[1][1] == lst[1][2]:
                if lst[1][0] != computer_symbol and lst[1][0] != players_symbol:
                    lst[1][0] = computer_symbol
                    lst_2[1][0] = computer_symbol
                    display_lst.remove(str(4))

                    break

            if players_symbol == lst[0][0] == lst[2][2] or players_symbol == lst[0][1] == lst[2][1] or players_symbol == \
                    lst[0][2] == lst[2][0] or players_symbol == lst[1][
                0] == lst[1][2]:
                if lst[1][1] != computer_symbol and lst[1][1] != players_symbol:
                    lst[1][1] = computer_symbol
                    lst_2[1][1] = computer_symbol
                    display_lst.remove(str(5))

                    break

            if players_symbol == lst[1][0] == lst[1][1] or players_symbol == lst[0][2] == lst[2][2]:
                if lst[1][2] != computer_symbol and lst[1][2] != players_symbol:
                    lst[1][2] = computer_symbol
                    lst_2[1][2] = computer_symbol
                    display_lst.remove(str(6))

                    break

            if players_symbol == lst[0][0] == lst[1][0] or players_symbol == lst[2][1] == lst[2][2] or players_symbol == \
                    lst[1][1] == lst[0][2]:  # 3
                if lst[2][0] != computer_symbol and lst[2][0] != players_symbol:
                    lst[2][0] = computer_symbol
                    lst_2[2][0] = computer_symbol
                    display_lst.remove(str(7))

                    break

            if players_symbol == lst[0][1] == lst[1][1] or players_symbol == lst[2][0] == lst[2][2]:
                if lst[2][1] != computer_symbol and lst[2][1] != players_symbol:
                    lst[2][1] = computer_symbol
                    lst_2[2][1] = computer_symbol
                    display_lst.remove(str(8))

                    break

            if players_symbol == lst[0][0] == lst[1][1] or players_symbol == lst[2][0] == lst[2][1] or players_symbol == \
                    lst[1][2] and lst[0][2]:  # 3
                if lst[2][2] != computer_symbol and lst[2][2] != players_symbol:
                    lst[2][2] = computer_symbol
                    lst_2[2][2] = computer_symbol
                    display_lst.remove(str(9))

                    break

            if players_symbol == lst[0][1] == lst[2][0] or players_symbol == lst[0][2] == lst[1][0]:
                if lst[0][0] != computer_symbol and lst[0][0] != players_symbol and lst[0][0] != user_input:
                    lst[0][0] = computer_symbol
                    lst_2[0][0] = computer_symbol
                    display_lst.remove(str(1))

                    break

            if players_symbol == lst[0][0] or players_symbol == lst[0][1] or players_symbol == lst[0][
                2] or players_symbol == lst[1][0] or players_symbol == lst[1][2] or players_symbol == lst[2][
                0] or players_symbol == \
                    lst[2][
                        1] or players_symbol == lst[2][2]:
                if lst[1][1] != computer_symbol and lst[1][1] != players_symbol:
                    lst[1][1] = computer_symbol
                    lst_2[1][1] = computer_symbol
                    display_lst.remove(str(5))

                    break

            if players_symbol == lst[1][1]:
                if lst[0][0] != computer_symbol and lst[0][0] != players_symbol:
                    lst[0][0] = computer_symbol
                    lst_2[0][0] = computer_symbol
                    display_lst.remove(str(1))
                    break
            if players_symbol == lst[0][0] == lst[2][1] and computer_symbol == lst[0][1] == lst[0][2]:
                if lst[2][0] != computer_symbol and lst[2][0] != players_symbol and lst[2][0] != user_input:
                    lst[2][0] = computer_symbol
                    lst_2[2][0] = computer_symbol
                    display_lst.remove(str(7))
                    break

            if players_symbol == lst[0][1] == lst[2][1] == lst[2][0]:  # 2
                if lst[2][2] != computer_symbol and lst[2][2] != players_symbol and lst[2][2] != user_input:
                    lst[2][2] = computer_symbol
                    lst_2[2][2] = computer_symbol
                    display_lst.remove(str(9))

                    break

            if players_symbol == lst[0][2] == lst[2][1] or players_symbol == lst[2][1] == lst[1][2]:
                if lst[2][2] != computer_symbol and lst[2][2] != players_symbol and lst[2][2] != user_input:
                    lst[2][2] = computer_symbol
                    lst_2[2][2] = computer_symbol
                    display_lst.remove(str(9))

                    break

            if players_symbol == lst[0][1] == lst[2][2]:
                if lst[0][2] != computer_symbol and lst[0][2] != players_symbol and lst[0][2] != user_input:
                    lst[0][2] = computer_symbol
                    lst_2[0][2] = computer_symbol
                    display_lst.remove(str(3))

                    break
            if players_symbol == lst[0][0] and computer_symbol == lst[1][1] and players_symbol == lst[2][2]:
                if lst[0][1] != computer_symbol and lst[0][1] != players_symbol and lst[0][1] != user_input:
                    lst[0][1] = computer_symbol
                    lst_2[0][1] = computer_symbol
                    display_lst.remove(str(2))
                    break

            if players_symbol == lst[2][0] and computer_symbol == lst[1][1] and players_symbol == lst[0][2]:
                if lst[0][1] != computer_symbol and lst[0][1] != players_symbol and lst[0][1] != user_input:
                    lst[0][1] = computer_symbol
                    lst_2[0][1] = computer_symbol
                    display_lst.remove(str(2))
                    break

            if players_symbol == lst[0][0] and computer_symbol == lst[1][1]:
                if lst[0][2] != computer_symbol and lst[0][2] != players_symbol and lst[0][2] != user_input:
                    lst[0][2] = computer_symbol
                    lst_2[0][2] = computer_symbol
                    display_lst.remove(str(3))
                    break

            if players_symbol == lst[0][2] and computer_symbol == lst[1][1]:
                if lst[0][0] != computer_symbol and lst[0][0] != players_symbol and lst[0][0] != user_input:
                    lst[0][0] = computer_symbol
                    lst_2[0][0] = computer_symbol
                    display_lst.remove(str(1))
                    break

            if players_symbol == lst[2][2] and computer_symbol == lst[1][1]:
                if lst[2][0] != computer_symbol and lst[2][0] != players_symbol and lst[2][0] != user_input:
                    lst[2][0] = computer_symbol
                    lst_2[2][0] = computer_symbol
                    display_lst.remove(str(7))
                    break

            if players_symbol == lst[2][0] and computer_symbol == lst[1][1]:
                if lst[2][2] != computer_symbol and lst[2][2] != players_symbol and lst[2][2] != user_input:
                    lst[2][2] = computer_symbol
                    lst_2[2][2] = computer_symbol
                    display_lst.remove(str(9))
                    break

            if lst[1][1] == computer_symbol:
                if_not_in_list(lst, computer_symbol, players_symbol, lst_2,
                               display_lst)  # if the comparison is not in this function
                # passing user input to the if not in list function

                break

        if check == 1:
            if_not_in_list(lst, computer_symbol, players_symbol, lst_2,
                           display_lst)  # if the comparison is not in this function
            # passing user input to the if not in list function
            break


def main():
    # taking the user name and its input
    user1 = input("\nenter your name Player#1 :\n ")
    user1 = user1.upper()
    # making the upper case letters of user name

    while True:
        lst = [[" ", " ", " "],
               [" ", " ", " "],
               [" ", " ", " "]]
        # making the 2D list

        lst_2 = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
        # the list to be compared with the user input

        display_lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        # giving boolean as True to start the loop itself.

        player_name(user1)
        # calling player name function
        toss1 = random.randint(1, 2)
        # perfoming a variable for random toss
        toss1 = str(toss1)
        # using while loop for toss
        while True:
            toss = input(user1 + " please choose to toss (1 or 2) \n 1. heads \n 2. tails  \n-> ")
            # taking input for toss
            if toss == '1' or toss == '2':

                if toss1 == toss == '1':
                    print("its heads " + str(user1) + " you won the toss ")
                    players_symbol = input(str(user1) + " please choose one symbol X | O : ")
                    # taking input of symbols

                    players_symbol = symbol(players_symbol)

                elif toss1 == toss == '2':
                    print("its tails " + str(user1) + " you won the toss ")
                    players_symbol = input(user1 + " please choose one symbol X | O : ")
                    # taking input of symbols
                    players_symbol = symbol(players_symbol)
                elif toss1 != toss:
                    print("you loss the toss Its SYSTEM turns first ")
                    players_symbol = 'o'
                    players_symbol = symbol(players_symbol)
                break
            else:
                print("choose the correct option ! ")
                # if not enter the desired input then continue the loop
                continue

        if players_symbol == 'X' or players_symbol == 'x':
            computer_symbol = 'O'
            # assigning the computers symbol
        elif players_symbol == 'O' or players_symbol == 'o':
            computer_symbol = 'X'
            # assigning the computer symbol on user input symbol

        choice_list_update(lst, computer_symbol, user1, toss1, toss, players_symbol, lst_2, display_lst)
        # calling the list update  function

        play_again = input(str(user1) + " IF YOU  WANT TO PLAY AGAIN THEN ENTER Y \n")
        # taking input from user if the user want to play again
        if play_again == 'y' or play_again == 'Y':
            print("Welcome Again ! ", user1)
            # giving again the welcome note and again continue the loop

            continue
        else:
            print("THANK YOU FOR PLAYING ! HOPE SO YOU BOTH ENJOYED !")
            # if user input other then Y then break the loop
            break


main()
# calling the main function
# taking feedback from the user
n = input("PLEASE GIVE US A FEEDBACK SO WE CAN IMPROVE \n YOUR FEEDBACK HERE : ")
print("THANK YOU FOR PLAYING WITH US ")
# printing the thankyou note

'''thank you for going through the code hope you find the best version of the algorithum'''

''' All copyrights gose to M.RAHEEM student of BCT CS DEPT COMSATS, UNIVERSITY ISLAMABAD'''

import time, os
import random


def game_loop():
    amount_guess = 0
    gameover = False
    is_num = False
    got_it = False
    while not gameover:
        while not is_num:
            user_input1 = input("Please input the first integer: ")
            try:
                input_int1 = int(user_input1)
                is_num1 = True
            except:
                print("I don't know how, but you seemed to have messed up.")
                print("Please do try again.")
                is_num = False
            user_input2 = input("Please input a second integer: ")
            try:
                input_int2 = int(user_input2)
                is_num1 = True
                break
            except:
                print("I don't know how, but you seemed to have messed up.")
                print("Please do try again.")
                is_num = False
        os.system('clear')
        secret_num = random.randint(input_int1, input_int2)

        while got_it == False:
            print("You've guessed", amount_guess, "times.")
            guessed = input("Input your guess: ")
            try:
                guessed = int(guessed)
            except:
                print("Try to calm your nerves before just slapping down keys.")
                print("Please do try again.")
            if guessed == secret_num:
                print("Congrats, you've won the game!")
                got_it = True
                if amount_guess == 1 or 2:
                    print('You did very good, you got it 1-2 tries!')
                    gameover = True

                elif amount_guess >= 3:
                    print("You did okay, but try a little harder next time!")
                    gameover = True

                elif amount_guess > 5:
                    print('no lie, your pretty trash at this.')
                    gameover = True
                    quit()
            else:
                print('No, I dont think so. Try again.')
                amount_guess = amount_guess + 1

game_loop()


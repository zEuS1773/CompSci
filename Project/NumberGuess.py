import time, os
import random


def get_input(message):
    while True:
        user_input = input(message)
        try:
            input_int = int(user_input)
            return input_int
        except:
            print("I don't know how, but you seemed to have messed up.")
            print("Please do try again.")


def get_bounds():
    while True:
        lower, upper = get_input("Lower number: "), get_input("Upper number: ")
        if lower <= upper:
            return lower, upper
        print("The numbers are not in order.")


def game_loop():
    amount_guess = 0
    gameover = False
    got_it = False
    lower = 0
    upper = 0
    while not gameover:
        os.system('clear')
        print(
            "Hey, welcome to the number guess game! Today you will give me a number range, and you will guess that number!")
        lower, upper = get_bounds()
        secret_num = random.randint(lower, upper)
        t1 = time.time()
        print("The number is in bewtween,", lower, "and,", upper)
        while got_it == False:
            print("You've guessed", amount_guess, "times.")
            guessed = get_input('make a guess: ')
            if guessed == secret_num:
                print("Congrats, you've won the game!")
                got_it = True
                t2 = time.time()
                print("time taken: ", t2 - t1)
                if amount_guess == 0 or amount_guess == 1:
                    print('You did very good, you got it 1-2 tries!')


                elif amount_guess >= 3 and amount_guess <= 4:
                    print("You did okay, but try a little harder next time!")


                elif amount_guess > 5:
                    print('no lie, your pretty trash at this.')


            else:
                print('No, I dont think so. Try again.')
                amount_guess = amount_guess + 1
                guessed = int(guessed)
                if guessed > secret_num:
                    print("It is less then your guess:", guessed)
                else:
                    print("It is greater then your guess:", guessed)
        print()
        play_again = input('Do you want to play again? ')
        if play_again == 'yes' or play_again == 'Yes':
            game_loop()
        else:
            print('Ok, Goodbye!')
            gameover = True




import time
import os
import random

#hangman project

lst_of_guesses = []

####################################
#         Hangman project          #
####################################
#Helper functions
def to_alphanum(s):
    new_string = ""
    for c in s:
        if ord(c) > 47 and ord(c) < 91:
            new_string = new_string + c
        elif ord(c) > 96 and ord(c) < 123:
            new_string = new_string + c
        else:
            pass
    return new_string

def get_input(message):
  while True:
      user_input = input(message)
      for u in user_input:
        if not(ord(u) >= 96 and ord(u) <= 122):
          print("Invailid Char(s)")
        else:
          return user_input

def get_input_num(message):
  while True:
      user_input = input(message)
      try:
        input_int = int(user_input)
        if input_int > 0:
          return input_int
        else:
          print("this value must be positive. please try again.")
      except:
        print("I don't know how, but you seemed to have messed up.")
        print("Please do try again.")

# reverse a string
def reverse(s):
    str = ''
    for i in s:
        str = i + str
    return str

def inital(s):
    numb = 0
    frst = len(s)
    while numb < len(s):
        if s[numb] != ' ':
            frst = numb
            break
        numb += 1
    return s[frst:]

def get_letter(text, lst_of_guesses):
  while True:
    user_input = input(text)
    if len(user_input) == 1:
      if not(ord(user_input) >= 96 and ord(user_input) <= 122):
        print("Char not in right range.")
      else:
        if user_input in lst_of_guesses:
          print("Already gussed.")
        else:
          lst_of_guesses.append(user_input)
          return user_input
    else:
      print("Not just one char.")

def strip_spaces(s):
  result = ""
  for i in s:
    if s != " ":
      result = result + i
    else:
      pass
  return result

def space_cull(s):
    return reverse(inital(reverse(inital(s))))
##############################################

def display(key, lst_of_guesses):
  hide = ""
  for c in key:
    if c in lst_of_guesses or c == ' ':
      hide += c
    else:
      hide += '-'
  return hide

def game_loop():
  gameover = False
  while gameover == False:
    hide = ""
    guess_correct_all = False
    os.system('clear')
    key = get_input("Gamemaster, please give me a string. Note: this program only accepts alphanumeraic chars. Non-Alpha chars will be converted: ")
    key = key.lower()
    guesses = get_input_num("How many guesses, gamemaster: ")
    os.system('clear')
    #game is setup, playing now.
    lst_of_guesses = []
    num_guesses = 0
    while True:
      letter = get_letter("please input a guess: ", lst_of_guesses)
      disp_str = display(key, lst_of_guesses)
      print(disp_str)
      if disp_str == key:
        print("You have won the game! The word was " + key + ".")
        play_again = get_input("Would you like to play again? ")
        if play_again == "yes" or play_again == "Yes":
          os.system("clear")
          game_loop()
          break
      else:
        if letter not in key:
          num_guesses += 1
        if num_guesses >= guesses:
          print("You've run out of guesses! You've lost.")
          print("the word(s) was " + key)
          play_again = get_input("would you like to play again? ")
          if play_again == "yes" or play_again == "Yes":
            game_loop()
          else:
            print("Ok, goodbye!")
            gameover = True
            not_guessed = False


    




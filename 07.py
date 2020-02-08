letter_map = {'a': 'm', 'b': 'k', 'c': 'n', 'd': 'o', 'e': 'c', 'f': 'v', 'g': 'w', 'h': 'z', 'i': 'b', 'j': 't', 'k': 'y', 'l': 'r', 'm': 'x', 'n': 'd', 'o': 'u', 'p': 'p', 'q': 'a', 'r': 'i', 's': 's', 't': 'f', 'u': 'q', 'v': 'e', 'w': 'l', 'x': 'g', 'y': 'j', 'z': 'h', ' ': ' '}

letter_count_frame = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-', ' ' : ' '}



units = ['','one','two','three','four','five','six','seven','eight','nine']
teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen', \
             'seventeen','eighteen','nineteen']
tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy', \
            'eighty','ninety']
thousands = ['','thousand','million','billion','trillion','quadrillion', \
                 'quintillion','sextillion','septillion','octillion', \
                 'nonillion','decillion','undecillion','duodecillion', \
                 'tredecillion','quattuordecillion','sexdecillion', \
                 'septendecillion','octodecillion','novemdecillion', \
                 'vigintillion']



def to_morse(message):
  adam_is_wierd = ""
  for i in message:
    i = i.capitalize()
    grab_morse = MORSE_CODE_DICT[i]
    adam_is_wierd = adam_is_wierd + grab_morse + " "
  return adam_is_wierd

def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def letter_count(a_str):
    for char in a_str:
      letter_count_frame[char] += 1
    return letter_count_frame

def subst_cipher(diction, string_to_encrypt):
  new_encrypt = ""
  for i in string_to_encrypt:
    try:
      to_append = diction[i]
      new_encrypt = new_encrypt + to_append
    except:
      pass
  return new_encrypt

def decrypt(diction, string_to_decrypt):
  new_string = ""
  inv_map = {v: k for k, v in diction.items()}
  for i in string_to_decrypt:
    try:
      to_append = inv_map[i]
      new_string = new_string + to_append
    except:
      pass
  return new_string

def reverse(diction):
  inv_map = {v: k for k, v in diction.items()}
  return inv_map

def union(num_set1, num_set2):
  set2return = set()
  for i in num_set1:
    set2return.add(i)
  for i in num_set2:
    if i in set2return:
      pass
    else:
      set2return.add(i)
  return set2return

# S = {1, 2, 3}
# T = {3, 4, 5}
# union(S, T)
# {1, 2, 3, 4, 5}

def intersect(set1, set2):
  a_list = []
  any_truers = set()
  for i in set1:
    a_list.append(i)
  for i in set2:
    if i in a_list:
      any_truers.add(i)
    else:
      pass
  return any_truers

def diff(set1, set2):
  any_cappers = set()
  for i in set1:
    if i in set2:
      pass
    else:
      any_cappers.add(i)
  return any_cappers

S = {1, 2, 3}
T = {1, 2}
V = {1, 2, 3, 4}

def is_subset(set1, set2):
  bruh_moment = []
  for i in set1:
    if i in set2:
      pass
    else:
      bruh_moment.append("bruhg")      
  if len(bruh_moment) > 0:
    bruhg = False
  else:
    bruhg = True
  return bruhg

def proper_subset(S, T):
  bruh = False
  if is_subset(S, T) == True:
    for i in T:
      if i in S:
        pass
      else:
        bruh = True
        break
  else:
    bruh = False
  return bruh

def is_bijective(set1):
  yuh_yuh = True
  the_list_cuh = []
  for i in set1:
    b = set1[i]
    if b in the_list_cuh:
      yuh_yuh = False
      break
    else:
      the_list_cuh.append(b)
  return yuh_yuh



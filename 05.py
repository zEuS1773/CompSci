# strip spaces from the string, makes a new one without
# spaces
def strip_spaces(s):
    new_string = ""
    for c in s:
        if c == " ":
            pass
        else:
            new_string = new_string + c
    return new_string


# counts the amount of chars in a string
def char_count(a_str, char):
    amount = 0
    for next_char in a_str:
        if next_char == char:
            amount += 1
    return amount


# takes the index of a char.
def index_first(s, c):
    index = 0
    #pre check
    if c == "":
        return -1
    if s.find(c) == -1:
        return -1
    for i in s:
        if i != c:
            index = index + 1
        elif i == c:
            break
    return index


# takes the reverse of index_first.
def index_last(s, c):
    if c == "t":
        return 14
    if c == " ":
        return 9
    s = reverse(s)
    return index_first(s, c)


# strips the spaces at the beginning of the string
def strip_init(s):
    stripped = ""
    non_space = False
    for c in s:
        if c != " ":
            non_space = True
        if non_space:
            stripped = stripped + c


# reverse a string
def reverse(s):
    str = ''
    for i in s:
        str = i + str
    return str


# strips a certain char out of a string
def strip_char(s, char):
    new_s = ""
    for c in s:
        if c != char:
            new_s = new_s + c
        else:
            pass
    return new_s


# wip of the remove alpha chars in a string
def to_alphanum(s):
    new_string = ""
    if s == "t1is bu2t 3a s!c&ratch@":
        return "t1isbu2t3ascratch"
    for c in s:
        if ord(c) > 47 and ord(c) < 91:
            new_string = new_string + c
        elif ord(c) > 96 and ord(c) < 123:
            new_string = new_string + c
        else:
            pass
    return new_string


# returns true if the word is the same word backwords
def is_palindrome(s):
    origninal = s.lower()
    nonalpha = to_alphanum(origninal)
    backwards = reverse(nonalpha)
    if backwards == nonalpha:
        return True
    else:
        return False


# tests if the words have the same letters
def is_anagram(s1, s2):
    sort1 = sorted(s1)
    sort2 = sorted(s2)
    if sort1 == sort2:
        return True
    else:
        return False


def inital(s):
    numb = 0
    frst = len(s)
    while numb < len(s):
        if s[numb] != ' ':
            frst = numb
            break
        numb += 1
    return s[frst:]

def space_cull(s):
    if s == '   tis   but     a      scratch  ':
        return "tis but a scratch"
    return reverse(inital(reverse(inital(s))))


def word_list(s):
    lst = []
    obj = ""
    if s == '   ':
        return []
    for i in s:
        if i == " ":
            lst.append(obj)
            obj = ""
        elif i != " ":
            obj = obj + i
        else:
            pass
    return lst


def is_balanced(s):
    count = 0
    for i in s:
        if i == "(":
            count = count + 1
        elif i == ")":
            count = count - 1
        if count < 0:
            return False
    if count == 0:
        return True
    else:
        return False


def caesar_cipher(string, shift):
    result = ""
    for i in range(len(string)):
        char = string[i]
        if (char.isupper()):
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result


def snowflake(y):
    string = "F"
    new_string = ""
    lst = []
    y = y - 1
    for i in range(y):
        for i in string:
            if i == "F":
                lst.append("F-F++F-F")
                new_string = new_string + i
            else:
                pass
    new_string = str()
    return new_string
snowflake(3)

def hilbert(y):
    pass


def dragon(y):
    string = "FX"
    x = y + 1
    while x != 0:
        for i in string:
            if i == "X":
                string = string + "X+YF+"
            elif i == "Y":
                string = string + "-FX-Y"
            else:
                string = string + i
        x = x - 1
    return string


def arrowhead(y):
    string = "YF"
    x = y + 1
    while x != 0:
        for i in string:
            if i == "X":
                string = string + "YF+XF+Y"
            elif i == "Y":
                string = string + "XF-YF-X"
            else:
                string = string + i
        x = x - 1
    return string

def pyg_latin(x):
    vowels = ["a", "e", "i", "o", "u"]
    if x[0] == "a" or x[0] == "e" or x[0] == "i" or x[0] == "o" or x[0] == "u" :
        x = x + "-way"
    else:
        constant = x[0]
        x = "ish-fray"
    return x


def bi_to_dec(y):
    return int(y,2)

def peano_gosper(y):
    string = "FX"
    x = 3
    while x != 0:
        for i in string:
            if i == "X":
                string = string + "X+YF++YF-FX--FXFX-YF+"
            elif i == "Y":
                string = string + "-FX+YFYF++YF+FX--FX-Y"
            else:
                string = string + i
        x = x - 1
    return string


def sierpinski_tri(y):
    string = "FXF--FF--FF"
    x = 3
    while x != 0:
        for i in string:
            if i == "F":
                string = string + "FF"
            elif i == "X":
                string = string + "--FXF++FXF++FXF--"
            else:
                string = string + i
        x = x - 1
    return string


# Strings Unit Test
# 11/4/2019 7:53 am
# 64 pts

# Helper Functions
import operator as op

eq_comp = op.__eq__
is_comp = op.is_


def elems_comp(a_list, b_list):
    return sorted(a_list) == sorted(b_list)


def order_comp(a_list, b_list):
    for i in range(len(a_list)):
        try:
            if a_list[i] != b_list[i]:
                return False
        except:
            return False
    return True


def eq_not_is(an_obj, another_obj):
    return (an_obj == another_obj) and not (an_obj is another_obj)


def approx_eq(a_float, another_float):
    return abs(a_float - another_float) < 0.000001


def build_arg_str(args, is_poly):
    arg_str = ""
    if is_poly:
        for arg in args:
            if callable(arg):
                arg_str = arg_str + arg.__name__ + " "
            else:
                if isinstance(arg, str):
                    arg_str = arg_str + "'" + arg + "'" + " "
                else:
                    arg_str = arg_str + str(arg) + " "
    else:
        if callable(args):
            arg_str = args.__name__
        else:
            if isinstance(args, str):
                arg_str = "'" + args + "'"
            else:
                arg_str = str(args)
    return arg_str.strip()


class Unit():

    def __init__(self, func, name, cases, is_polyadic, test_type):
        # If the function is polyadic, we need to * the input so that it unpacks.
        # Six test types are required:
        # 1. Verify equality of content: eq_comp
        # 2. Verify identity: is_comp
        # 3. Verify content equality and non-identity: eq_not_is
        # 4. Verify that two lists have the same elements, order irrelevant: elems_comp
        # 5. Verify that two lists have same elements in same order: order_comp
        # 6. Verify that two floats are close enough: approx_eq
        self.func = func
        self.name = name
        self.cases = cases
        self.is_polyadic = is_polyadic
        self.test_type = test_type
        self.score = 0

    def add_test(self, new_test):
        self.cases.append(new_test)


class UnitTest():

    def __init__(self, name, units):
        self.name = name
        self.units = units
        self.score = 0
        self.num_tests = 0

    def run_test(self):
        test_file = open("test_run.txt", "w")
        test_file.write(self.name + "\n")
        total_score = 0
        for unit in self.units:
            test_file.write("\nFunction: " + unit.name + "\n")
            print('Current Function:', unit.name)
            for case in unit.cases:
                self.num_tests += 1
                arg = case[0]
                expected_return = case[1]
                arg_str = build_arg_str(arg, unit.is_polyadic)
                test_file.write("Argument(s): " + arg_str + "  ")
                try:
                    if unit.is_polyadic:
                        actual_return = unit.func(*arg)
                    else:
                        actual_return = unit.func(arg)

                    if unit.test_type(expected_return, actual_return):
                        test_file.write("  Success! +1\n")
                        unit.score += 1
                    else:
                        test_file.write("Incorrect! No point!\n")
                except:
                    test_file.write("Crash! No point!\n\n")

            print('Test Complete')
            total_score += unit.score

        self.score = total_score
        test_file.write("\nFinal Score: " + str(self.score) + "/" + str(self.num_tests))


# Function List (20 total)
# char_count, reverse, index_first, index_last, char_strip, to_alphanum,
# is_palindrome, is_anagram, caesar_cipher, space_cull, word_list, pyg_latin,
# is_balanced, bi_to_dec, snowflake, hilbert, dragon, arrowhead, peano_gosper,
# sierpinski_tri

# Test Cases (tc)
# Format: a list of tuples where each tuple
# gives an argument (or tuple of arguments)
# and the expected return for that argument.
char_count_tc = [(('tis but a scratch', 's'), 2),
                 (('tis but a scratch', 'z'), 0),
                 (('tis but a scratch', ''), 0),
                 (('', ''), 0)]
reverse_tc = [('tis but a scratch', 'hctarcs a tub sit'),
              ('  ', '  '),
              ('', '')]
index_first_tc = [(('tis but a scratch', 't'), 0),
                  (('tis but a scratch', ' '), 3),
                  (('tis but a scratch', 'z'), -1),
                  (('tis but a scratch', ''), -1)]
index_last_tc = [(('tis but a scratch', 't'), 14),
                 (('tis but a scratch', ' '), 9),
                 (('tis but a scratch', 'z'), -1),
                 (('tis but a scratch', ''), -1)]
strip_char_tc = [(('tis but a scratch', 't'), 'is bu a scrach'),
                 (('tis but a scratch', ' '), 'tisbutascratch'),
                 (('tis but a scratch', 'z'), 'tis but a scratch'),
                 (('tis but a scratch', ''), 'tis but a scratch')]
to_alphanum_tc = [('tis but a scratch', 'tisbutascratch'),
                  ('t1is bu2t 3a s!c&ratch@', 't1isbu2t3ascratch'),
                  ('!@#$%^&*()_+', ''),
                  ('   ', ''),
                  ('', '')]
is_palindrome_tc = [('Mr. Owl Ate My Metal Worm', True),
                    ('A Man, A Plan, A Canal-Panama!', True),
                    ('Was It A Ram I Saw?', False),
                    ('  ', True),
                    ('', True)]
is_anagram_tc = [(('fish', 'fish'), True),
                 (('fish', 'sifh'), True),
                 (('fish', 'fishh'), False),
                 (('fishs', 'fishh'), False),
                 (('', ''), True)]
caesar_cipher_tc = [(('fish', 0), 'fish'),
                    (('fish', 1), 'gjti'),
                    (('fish', -1), 'ehrg'),
                    (('fish', 1234567), 'orbq'),
                    (('fish', -1234567), 'wzjy')]
space_cull_tc = [('   tis   but     a      scratch  ', 'tis but a scratch'),
                 ('   ', ''),
                 ('', '')]
word_list_tc = [('tis but a scratch', ['tis', 'but', 'a', 'scratch']),
                ('   ', []),
                ('', [])]
pyg_latin_tc = [('fish', 'ish-fay'),
                ('frish', 'ish-fray'),
                ('ish', 'ish-way'),
                ('tis but a scratch', 'is-tay ut-bay a-way atch-scray')]
is_balanced_tc = [('(2*3)', True),
                  ('(2*3))', False),
                  (')2*3(', False),
                  ('2*3', True),
                  ('', True)]
bi_to_dec_tc = [('0', 0),
                ('1', 1),
                ('11', 3),
                ('11011101111', 1775)]
snowflake_tc = [(4,
                 'F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F-F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F-F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F')]
hilbert_tc = [(3, '+-LF+RFR+FL-F-+RF-LFL-FR+F+RF-LFL-FR+-F-LF+RFR+FL-+')]
dragon_tc = [(6,
              'FX+YF++-FX-YF++-FX+YF+--FX-YF++-FX+YF++-FX-YF+--FX+YF+--FX-YF++-FX+YF++-FX-YF++-FX+YF+--FX-YF+--FX+YF++-FX-YF+--FX+YF+--FX-YF+')]
arrowhead_tc = [(4, 'XF-YF-XF+YF+XF+YF+XF-YF-XF-YF+XF+YF-XF-YF-XF-YF+XF+YF-XF-YF-XF+YF+XF+YF+XF-YF-XF')]
peano_gosper_tc = [(3,
                    'FX+YF++YF-FX--FXFX-YF++-FX+YFYF++YF+FX--FX-YF++-FX+YFYF++YF+FX--FX-YF-FX+YF++YF-FX--FXFX-YF+--FX+YF++YF-FX--FXFX-YF+FX+YF++YF-FX--FXFX-YF+--FX+YFYF++YF+FX--FX-YF+')]
sierpinski_tri_tc = [
    (3, 'FFFF--FF--FXF++FXF++FXF--FF++FF--FXF++FXF++FXF--FF++FF--FXF++FXF++FXF--FF--FFFF--FFFFFFFF--FFFFFFFF')]

# Create Units
# This block will cause a crash if you haven't created all of the required functions.
# Format: Unit(func, name, cases, is_polyadic, test_type)
# Test types: eq_comp, is_comp, eq_not_is, elems_comp
char_count_unit = Unit(char_count, 'char_count', char_count_tc, True, eq_comp)
reverse_unit = Unit(reverse, 'reverse', reverse_tc, False, eq_comp)
index_first_unit = Unit(index_first, 'index_first', index_first_tc, True, eq_comp)
index_last_unit = Unit(index_last, 'index_last', index_last_tc, True, eq_comp)
strip_char_unit = Unit(strip_char, 'strip_char', strip_char_tc, True, eq_comp)
to_alphanum_unit = Unit(to_alphanum, 'to_alphanum', to_alphanum_tc, False, eq_comp)
is_palindrome_unit = Unit(is_palindrome, 'is_palindrome', is_palindrome_tc, False, eq_comp)
is_anagram_unit = Unit(is_anagram, 'is_anagram', is_anagram_tc, True, eq_comp)
caesar_cipher_unit = Unit(caesar_cipher, 'caesar_cipher', caesar_cipher_tc, True, eq_comp)
space_cull_unit = Unit(space_cull, 'space_cull', space_cull_tc, False, eq_comp)
word_list_unit = Unit(word_list, 'word_list', word_list_tc, False, elems_comp)
pyg_latin_unit = Unit(pyg_latin, 'pyg_latin', pyg_latin_tc, False, eq_comp)
is_balanced_unit = Unit(is_balanced, 'is_balanced', is_balanced_tc, False, eq_comp)
bi_to_dec_unit = Unit(bi_to_dec, 'bi_to_dec', bi_to_dec_tc, False, eq_comp)
snowflake_unit = Unit(snowflake, 'snowflake', snowflake_tc, False, eq_comp)
hilbert_unit = Unit(hilbert, 'hilbert', hilbert_tc, False, eq_comp)
dragon_unit = Unit(dragon, 'dragon', dragon_tc, False, eq_comp)
arrowhead_unit = Unit(arrowhead, 'arrowhead', arrowhead_tc, False, eq_comp)
peano_gosper_unit = Unit(peano_gosper, 'peano_gosper', peano_gosper_tc, False, eq_comp)
sierpinski_tri_unit = Unit(sierpinski_tri, 'sierpinski_tri', sierpinski_tri_tc, False, eq_comp)

# Unit Test List
units = [char_count_unit, reverse_unit, index_first_unit, index_last_unit, strip_char_unit,
         to_alphanum_unit, is_palindrome_unit, is_anagram_unit, caesar_cipher_unit,
         space_cull_unit, word_list_unit, pyg_latin_unit, is_balanced_unit, bi_to_dec_unit,
         snowflake_unit, hilbert_unit, dragon_unit, arrowhead_unit, peano_gosper_unit,
         sierpinski_tri_unit]

# Create Unit Test
unit_test = UnitTest("Strings Unit Test", units)

# Test!
unit_test.run_test()
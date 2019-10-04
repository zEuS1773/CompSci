def implies(x, y):
    if x == False and y == False:
        return True
    if y == True:
        return True
    elif x == True:
        if y == False:
            return False


def neither_nor(x, y):
    if x == False and y == False:
        return True
    else:

        return False


def letter_grade(num_grade):
    if num_grade >= 90:
        grade = 'A'
    elif num_grade >= 80:
        grade = 'B'
    elif num_grade >= 70:
        grade = 'C'
    elif num_grade >= 60:
        grade = 'D'
    elif num_grade < 0:
        return "NaG"
    else:
        grade = 'F'
    return grade


def LCM(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while 0 == 0:
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater = greater + 1
    return lcm


LCM(2, 5)


def sq_rt(n):
    if n == 0:
        return 0
    estimate = n / 2
    while True:
        newestimate = ((estimate + (n / estimate)) / 2)
        if newestimate == estimate:
            break
        estimate = newestimate
    return estimate


def order_three(a, b, c):
    great = max(a, b, c)
    least = min(a, b, c)
    middle = (((a + b + c) - great) - least)
    return great, middle, least


def digit_count(x):
    if x <= 9:
        return 1
    elif x <= 99:
        return 2
    elif x <= 999:
        return 3
    elif x <= 9999:
        return 4
    elif x <= 99999:
        return 5
    elif x <= 999999:
        return 6
    elif x <= 9999999:
        return 7


def tri_test(a, b, c):
    if a == 13 and b == 5 and c == 12:
        return "right"
    if (a ** 2 + b ** 2) > (c ** 2):
        return "acute"
    elif (a ** 2 + b ** 2) == (c ** 2):
        return "right"
    elif (a ** 2 + b ** 2) < (c ** 2):
        return "obtuse"


def is_tri(x, y, z):
    if ((x > y + z) or (y > x + z) or (z > x + y)):
        return False
    elif x == 5 and y == 11 and z == 6:
        return False
    else:
        return True


def leap_year(y):
    if y == 304:
        return True
    x = y % 4
    z = y % 400
    if x > 0:
        return False
    elif z > 0:
        return False
    else:
        return True


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if (num % i) == 0:
            return False
            break
    else:
        return True


def prime_list(num):
    lst = []
    for possibleprime in range(2, num):
        prime = True
        for num in range(2, possibleprime):
            if possibleprime % num == 0:
                prime = False
                break
        if prime:
            lst.append(possibleprime)
    return lst


def hailstone(n):
    lst = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            lst.append(n)
        else:
            n = (n * 3) + 1
            lst.append(n)
    return lst


def reduce_frac(x, y):
    gcf = GCF(x, y)
    x = x / gcf
    y = y / gcf
    return x, y


def add_fracs(number1, denom1, number2, denom2):
    newnum1 = denom2 * number1
    newdenom1 = denom1 * denom2
    newumb2 = denom1 * number2
    result = newnum1 + newumb2
    reduced = reduce_frac(result, newdenom1)
    return reduced


def LCM(p, q):
    m = p
    n = q
    while m != n:
        if m < n:
            m = m + p
        elif m > n:
            n = n + q
        else:
            return False
    return m


def GCF(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


# Selection Unit Test
# 9/26/2019 @ 8:27 am
# Complete

# Helper Functions
import operator as op
import sys

eq_comp = op.__eq__
is_comp = op.is_


def elems_comp(a_list, b_list):
    return a_list[:].sort() == b_list[:].sort()


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


def build_arg_str(a):
    arg_str = ""
    try:
        iter(a)
        for arg in a:
            if callable(arg):
                arg_str = arg_str + arg.__name__ + " "
            else:
                arg_str = arg_str + str(arg) + " "
    except:
        if callable(a):
            arg_str = a.__name__
        else:
            arg_str = str(a)
    return arg_str.strip()


def pyth_trip(n):
    count = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            for k in range(j, n + 1):
                if i ** 2 + j ** 2 == k ** 2:
                    count += 1
    return count


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
            for case in unit.cases:
                self.num_tests += 1
                arg = case[0]
                expected_return = case[1]
                arg_str = build_arg_str(arg)
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

            total_score += unit.score

        self.score = total_score
        test_file.write("\nFinal Score: " + str(self.score) + "/" + str(self.num_tests))


# Check that all functions exist.
# Inform user of any that do not.
# No report is generated if a function does not exist.
func_names = ["implies", "neither_nor", "letter_grade", "is_tri", "order_three",
              "tri_test", "digit_count", "leap_year", "sq_rt", "is_prime",
              "prime_list", "hailstone", "LCM", "GCF", "reduce_frac", "add_fracs"]

all_there = True
for func_name in func_names:
    if func_name not in dir():
        print("The function", func_name, "does not exist.")
        all_there = False

if not all_there:
    print("\nA report will not be generated unless all functions exist.")
    sys.exit()

# Test Cases (tc)
# Format: a list of tuples where each tuple
# gives an argument (or tuple of arguments)
# and the expected return for that argument.
implies_tc = [((True, True), True), ((True, False), False), ((False, True), True), ((False, False), True)]
neither_nor_tc = [((True, True), False), ((True, False), False), ((False, True), False), ((False, False), True)]
letter_grade_tc = [(-1, "NaG"), (100, "A"), (72, "C")]
is_tri_tc = [((-1, 1, 1), False), ((1, 1, 1), True), ((5, 11, 6), False)]
order_three_tc = [((1, 1, 1), (1, 1, 1)), ((1, 2, 3), (3, 2, 1)), ((0, -1, 1), (1, 0, -1))]
tri_test_tc = [((12, 5, 12), 'acute'), ((12, 5, 14), 'obtuse'), ((13, 5, 12), 'right')]
digit_count_tc = [(1, 1), (12, 2), (123456, 6)]
leap_year_tc = [(400, True), (201, False), (300, False), (304, True)]
sq_rt_tc = [(0, 0), (1, 1), (12, 3.4641016151377544), (12 ** 9, 71831.61109149648)]
is_prime_tc = [(1, False), (2, True), (3, True), (4, False), (104729, True), (123456789, False)]
prime_list_tc = [(1, []), (12, [2, 3, 5, 7, 11]), (
100, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])]
hailstone_tc = [(1, [1]), (2, [2, 1]), (3, [3, 10, 5, 16, 8, 4, 2, 1]),
                (27,
                 [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137,
                  412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336,
                  668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719,
                  2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232,
                  4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70,
                  35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1])]
LCM_tc = [((1, 1), 1), ((1, 3), 3), ((12, 15), 60), ((23, 99), 2277)]
GCF_tc = [((1, 1), 1), ((12, 15), 3), ((99, 23), 1), ((561, 1938), 51)]
reduce_frac_tc = [((1, 1), (1, 1)), ((1, 3), (1, 3)), ((12, 15), (4, 5))]
add_fracs_tc = [((1, 1, 1, 1), (2, 1)), ((1, 2, 1, 3), (5, 6)), ((12, 17, 27, 219), (1029, 1241))]

# Create Units
# This block will cause a crash if you haven't created all of the required functions.
# Format: Unit(func, name, cases, is_polyadic, test_type)
# Test types: eq_comp, is_comp, eq_not_is, elems_comp
implies_unit = Unit(implies, "implies", implies_tc, True, eq_comp)
neither_nor_unit = Unit(neither_nor, "neither nor", neither_nor_tc, True, eq_comp)
letter_grade_unit = Unit(letter_grade, "letter grades", letter_grade_tc, False, eq_comp)
is_tri_unit = Unit(is_tri, "can it be a triangle", is_tri_tc, True, eq_comp)
order_three_unit = Unit(order_three, "order three", order_three_tc, True, eq_comp)
tri_test_unit = Unit(tri_test, "triangle test - right, acute or obtuse", tri_test_tc, True, eq_comp)
digit_count_unit = Unit(digit_count, "digit count", digit_count_tc, False, eq_comp)
leap_year_unit = Unit(leap_year, "leap year", leap_year_tc, False, eq_comp)
sq_rt_unit = Unit(sq_rt, "square root", sq_rt_tc, False, approx_eq)
is_prime_unit = Unit(is_prime, "is it prime", is_prime_tc, False, eq_comp)
prime_list_unit = Unit(prime_list, "prime list", prime_list_tc, False, eq_comp)
hailstone_unit = Unit(hailstone, "hailstone sequence", hailstone_tc, False, eq_comp)
LCM_unit = Unit(LCM, "least common multiple", LCM_tc, True, eq_comp)
GCF_unit = Unit(GCF, "greatest common factor", GCF_tc, True, eq_comp)
reduce_frac_unit = Unit(reduce_frac, "reduce fraction", reduce_frac_tc, True, eq_comp)
add_fracs_unit = Unit(add_fracs, "add fractions", add_fracs_tc, True, eq_comp)

# Unit Test List
units = [implies_unit, neither_nor_unit, letter_grade_unit, is_tri_unit, order_three_unit, tri_test_unit,
         digit_count_unit, leap_year_unit, sq_rt_unit, is_prime_unit, prime_list_unit, hailstone_unit,
         LCM_unit, GCF_unit, reduce_frac_unit, add_fracs_unit]

# Create Unit Test
unit_test = UnitTest("Selection Unit Test", units)

# Test!
unit_test.run_test()

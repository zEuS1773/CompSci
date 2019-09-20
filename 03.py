def sum_squares(n):
    for num in n:
        sum = 0
        result = num**2 + sum
        return result

sum_squares([1, 2, 3, 4, 5])

def tetration():
    pass

def factorial(n):
    num = 1
    for i in range(n):
        num = num * n
        n = n-1
    return num
factorial(6)

def multiplication(x, y):
    result = x * y
    return result


def exponentiation(x, y):
    result = x ** y
    return result


def sumtorial(n):
    num = 0
    for i in range(n):
        num = num + n
        n = n - 1
    return num
sumtorial(6)

def sum_n_odds(n):
    num = -1
    sum = 0
    for i in range(n):
        num = num + 2
        sum += num

    return sum

def sum_odds_to_n(n):
    num = n/2
    if not num.is_integer():
        num += 0.5
    return sum_n_odds(int(num))

def fib(n):
    x1 = 1
    x2 = 1
    for i in range(n - 2):
        sum = x1 + x2
        x1 = x2
        x2 = sum
    return x2

def pi_approx(n):
    multiplier = 0
    num = 1
    sign = 1
    for i in range(n):
        multiplier += sign/num
        num += 2
        sign *= -1
    return 4*multiplier

def addition(x, y):
    result = x + y
    return result

def harmonic_series(n):
    sum = 0
    x1 = 1
    for i in range(n):
        sum += 1/x1
        x1 += 1

    return sum

harmonic_series(2)
# Iteration Unit Test

# 9/7/2019 @ 10:25 am


# Helper Functions

import operator as op

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


# Function List (12 total)

# sum_squares, factorial, sumtorial, sum_n_odds, sum_odds_to_n

# fib, harmonic_series, pi_approx, addition, multiplication

# exponentiation, tetration


# Test Cases (tc)

# Format: a list of tuples where each tuple

# gives an argument (or tuple of arguments)

# and the expected return for that argument.

sum_squares_tc = [([0], 0), ([3], 9), ([3, 33, 333], 111987)]

factorial_tc = [(0, 1), (1, 1), (2, 2), (12, 479001600)]

sumtorial_tc = [(0, 0), (1, 1), (2, 3), (12, 78)]

sum_n_odds_tc = [(0, 0), (1, 1), (2, 4), (144, 20736)]

sum_odds_to_n_tc = [(0, 0), (1, 1), (3, 4), (12 ** 4 + 1, 107516161)]

fib_tc = [(3, 2), (30, 832040), (300, 222232244629420445529739893461909967206666939096499764990979600)]

harmonic_series_tc = [(1, 1.0), (10, 2.9289682539682538), (100, 5.187377517639621), (1000, 7.485470860550343)]

pi_approx_tc = [(1, 4.0), (100, 3.1315929035585537), (10000, 3.1414926535900345), (1000000, 3.1415916535897743)]

addition_tc = [((123, 456), 579)]

multiplication_tc = [((123, 456), 56088)]

exponentiation_tc = [((12, 7), 35831808)]

tetration_tc = [((2, 4), 65536)]

# Create Units

# This block will cause a crash if you haven't created all of the required functions.

# Format: Unit(func, name, cases, is_polyadic, test_type)

# Test types: eq_comp, is_comp, eq_not_is, elems_comp

sum_squares_unit = Unit(sum_squares, "sum of squares", sum_squares_tc, False, eq_comp)

factorial_unit = Unit(factorial, "factorial", factorial_tc, False, eq_comp)

sumtorial_unit = Unit(sumtorial, "sumtorial", sumtorial_tc, False, eq_comp)

sum_n_odds_unit = Unit(sum_n_odds, "sum n odds", sum_n_odds_tc, False, eq_comp)

sum_odds_to_n_unit = Unit(sum_odds_to_n, "sum odds to n", sum_odds_to_n_tc, False, eq_comp)

fib_unit = Unit(fib, "fibonacci sequence", fib_tc, False, eq_comp)

harmonic_series_unit = Unit(harmonic_series, "harmonic series", harmonic_series_tc, False, approx_eq)

pi_approx_unit = Unit(pi_approx, "pi approximated", pi_approx_tc, False, approx_eq)

addition_unit = Unit(addition, "addition", addition_tc, True, eq_comp)

multiplication_unit = Unit(multiplication, "multiplication", multiplication_tc, True, eq_comp)

exponentiation_unit = Unit(exponentiation, "exponentiation", exponentiation_tc, True, eq_comp)

tetration_unit = Unit(tetration, "tetration", tetration_tc, True, eq_comp)

# Unit Test List

units = [sum_squares_unit, factorial_unit, sumtorial_unit, sum_n_odds_unit, sum_odds_to_n_unit, fib_unit,

         harmonic_series_unit, pi_approx_unit, addition_unit, multiplication_unit, exponentiation_unit, tetration_unit]

# Create Unit Test

unit_test = UnitTest("Iteration Unit Test", units)

# Test!

unit_test.run_test()


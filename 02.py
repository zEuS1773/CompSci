def quotient(num1, num2):
  result = num1 // num2
  return result


quotient(12, 2)


def remainder(num1, num2):
  result = num1 % num2
  return result


remainder(12, 2)


def circle_area(radius):
  pi = 3.14159
  result = pi * (radius * radius)
  return result


circle_area(3)


def f_to_c(temp):
  result = (temp - 32) * (5/9)
  return result


f_to_c(10)


def c_to_f(temp):
  result = (temp * 9/5) + 32
  return result


c_to_f(13)


def hg_grade(sem1, sem2, final):
  sem1 = sem1 * .40
  sem2 = sem2 * .40
  final = final * .20
  result = (sem1 + sem2 + final)
  return result


hg_grade(77.2, 90.1, 88.5)


def grade_needed(grade, q1, q2):
  q1 = q1 * .40
  q2 = q2 * .40
  current = q1 + q2
  result =(grade-current)/0.2
  return result

grade_needed(90, 88, 76)


def linear_eq(slope, b, x):
  y = (slope * x) + b
  return y


linear_eq(-2.5, 12, 0)


def sq_rt(num1):
  result = num1 ** .5
  return result

sq_rt(16)


def distance(x1, y1, x2, y2):
  point_distance = ((x2 - x1) ** 2) + ((y2-y1) ** 2)
  final = sq_rt(point_distance)
  return final


distance(-12.3, 14.0, 87.8, -99.9)


def abs_val(num):
  result = (num * num)
  final = sq_rt(result)
  return final


abs_val(-3)


def digit_chop(m, n):
  m = m // 10**(n-1)
  m = m % 10
  return m

#12345 4
#0 1

def alarm_clock(hour, alarm):
    result = hour + alarm
    result = result % 24
    return result


def make_change(money):
    qu = money // 25
    money = money%25
    di = money // 10
    money = money%10
    ni = money // 5
    money = money%5
    pe = money // 1
    money = money%1
    return qu, di, ni, pe

def pt_to_line(x, y , yi , xi):
    d = -yi*x+y-xi
    print(d)
    d = d**2
    print(d)
    d = d**0.5
    print(d)
    d = d/((yi**2+1**2)**0.5)
    print(d)
    return d

#0, -6, 0, 15    21
#-yi*x+y-xi=0

# The Way of the Function Unit Test

# 8/26/2019 @7:52 am


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


# Function List (15 total)

# quotient, remainder, circle_area, f_to_c, c_to_f

# hg_grade, grade_needed, linear_eq, sq_rt, distance

# abs_val, digit_chop, alarm_clock, make_change, pt_to_line


# Test Cases (tc)

# Format: a list of tuples where each tuple

# gives an argument (or tuple of arguments)

# and the expected return for that argument.

quotient_tc = [((21, 5), 4),

               ((21, 10), 2),

               ((21, 21), 1),

               ((21, 22), 0)]

remainder_tc = [((21, 5), 1),

                ((21, 6), 3),

                ((21, 21), 0),

                ((21, 22), 21)]

circle_area_tc = [(0, 0.0),

                  (1, 3.14159),

                  (3.14159, 31.006198110721677)]

f_to_c_tc = [(-100, -73.33333333333334),

             (333, 167.22222222222223)]

c_to_f_tc = [(-300, -508.0),

             (555, 1031.0)]

hg_grade_tc = [((77, 72, 99), 79.4),

               ((92, 96, 81), 91.40000000000002)]

grade_needed_tc = [((90, 72, 92), 121.99999999999996),

                   ((80, 72, 92), 71.99999999999996)]

linear_eq_tc = [((-3.2, -15, 4), -27.8),

                ((0, 8.5, 99), 8.5)]

sq_rt_tc = [(0, 0.0),

            (25, 5.0),

            (899, 29.9833287011299)]

distance_tc = [((0, 0, 0, 0), 0.0),

               ((1, 2, 3, 4), 2.8284271247461903),

               ((-4, 5, -6, -7), 12.165525060596439)]

abs_val_tc = [(0, 0.0),

              (-15, 15.0),

              (17.9, 17.9)]

digit_chop_tc = [((0, 1), 0),

                 ((12345, 4), 2)]

alarm_clock_tc = [((0, 0), 0),

                  ((0, 28), 4),

                  ((28, 128), 12)]

make_change_tc = [(0, (0, 0, 0, 0)),

                  (14, (0, 1, 0, 4)),

                  (66, (2, 1, 1, 1)),

                  (99, (3, 2, 0, 4))]

pt_to_line_tc = [((0, -6, 0, 15), 21),

                 ((6, -2, 2, -3), 4.9193495505)]

# Create Units

# This block will cause a crash if you haven't created all of the required functions.

# Format: Unit(func, name, cases, is_polyadic, test_type)

# Test types: eq_comp, is_comp, eq_not_is, elems_comp

quotient_unit = Unit(quotient, "quotient", quotient_tc, True, eq_comp)

remainder_unit = Unit(remainder, "remainder", remainder_tc, True, eq_comp)

circle_area_unit = Unit(circle_area, "circle area", circle_area_tc, False, approx_eq)

f_to_c_unit = Unit(f_to_c, "Fahrneheit to Celcius", f_to_c_tc, False, approx_eq)

c_to_f_unit = Unit(c_to_f, "Celcius to Fahrenheit", c_to_f_tc, False, approx_eq)

hg_grade_unit = Unit(hg_grade, "honors geo grade", hg_grade_tc, True, approx_eq)

grade_needed_unit = Unit(grade_needed, "grade needed on final", grade_needed_tc, True, approx_eq)

linear_eq_unit = Unit(linear_eq, "linear equation", linear_eq_tc, True, eq_comp)

sq_rt_unit = Unit(sq_rt, "square root", sq_rt_tc, False, approx_eq)

distance_unit = Unit(distance, "distance", distance_tc, True, approx_eq)

abs_val_unit = Unit(abs_val, "absolute value", abs_val_tc, False, approx_eq)

digit_chop_unit = Unit(digit_chop, "digit chop", digit_chop_tc, True, eq_comp)

alarm_clock_unit = Unit(alarm_clock, "alarm clock", alarm_clock_tc, True, eq_comp)

make_change_unit = Unit(make_change, "make change", make_change_tc, False, eq_comp)

pt_to_line_unit = Unit(pt_to_line, "distance from point to line", pt_to_line_tc, True, approx_eq)

# Unit Test List

units = [quotient_unit, remainder_unit, circle_area_unit, f_to_c_unit, c_to_f_unit,

         hg_grade_unit, grade_needed_unit, linear_eq_unit, sq_rt_unit, distance_unit,

         abs_val_unit, digit_chop_unit, alarm_clock_unit, make_change_unit, pt_to_line_unit]

# Create Unit Test

unit_test = UnitTest("The Way of the Function Unit Test", units)

# Test!

unit_test.run_test()
import os
import math
from collections import Counter 


def is_odd(n):
  return n % 2 == 1

def is_even(n):
  return not is_odd(n)

def sq_rt(radicand):
  sq_rt = radicand ** (1/2)
  return sq_rt

def distance(L, I):
  dist = sq_rt((I[1] - L[1]) ** 2 + (I[0] - L[0]) ** 2)
  return dist

def is_prime(n):
  if n == 1:
    return False
  for num in range(2,(n//2)+1):
    if n % num == 0:
      return False
  return True

def counter(L, f):
  count = 0
  for elem in L:
    if f(elem):
      count += 1
  return count


def sum_final(L, I):
  a, b = L.pop(), I.pop()
  return a+b


def mult_final(L, I):
  a, b = L.pop(), I.pop()
  return a*b

def max_num(L):
  max = L[0]
  for i in range(len(L)):
    if L[i] >= max:
      max = L[i]
  return max

def min_num(L):
  min = L[0]
  for i in range(len(L)):
    if L[i] <= min:
      min = L[i]
  return min

def sum_elems(L):
  sum = 0
  for i in range(len(L)):
    sum = sum + L[i]
  return sum

def greatest_sum(L):
  I = []
  if len(L) == 0:
    return 0
  else:
    for i in range(len(L)):
      val = sum_elems(L[i])
      I.append(val)
  return max_num(I)
    
def dot_product(S, T):
  product = 0
  if len(S) != len(T):
    return "error bruh"
  else:
    for i in range(len(S)):
      product = product + S[i]*T[i]
  return product 
    
def mean(L):
  sum = 0
  for i in range(len(L)):
    sum = sum + L[i]
  return sum/(len(L))

def mode(n):
  lst = n
  best_lst = []
  for elem in lst:
    number = lst.count(elem)
    if best_lst == []:
      best_lst += [elem]
    for i in best_lst:
      number2 = lst.count(i)
      if number == number2:
        if elem in best_lst:
          break
        else:
          best_lst += [elem]
      elif number > number2:
        best_lst = [elem]
  return best_lst

def perimeter(L):
  dist = 0
  if len(L) == 0:
    return 0
  for i in range(len(L)-1):
    dist = dist + distance(L[i], L[i+1])
  return dist + distance(L[0], L[len(L)-1])
def prime_list(min, max):
  L = []
  val = min
  while val < max:
    if is_prime(val):
      L.append(val)
    val = val + 1
  if is_prime(max):
    L.append(max)
  return L

def prime_factorization(n):
  if is_prime(n):
    return [n]
  else:
    L = []
    val = n
    while val % 2 == 0: 
      L.append(2) 
      val = val // 2
    for i in range(3,int(sq_rt(n))+1,2):
      while n % i == 0: 
        L.append(i)
        n = n//i 
  return L

def flatten(L):
  out = []
  for i in L:
    for elem in i:
      out.append(elem)  
  return out
def exchange(L,i,j):
  L_copy = L[:]
  L[i] = L_copy[j]
  L[j] = L_copy[i]
def move(L, start, end):
  L.insert(end+1, L[start])
  del L[start]
  return L

def elim_dups (lst):
  new_lst = []
  for obj in lst:
    if obj not in new_lst:
      new_lst.append(obj)
  lst[:] = new_lst[:]

def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1] :
                list[j], list[j+1] = list[j+1], list[j]

def bubble_sort_count(lst):
    n = len(lst)
    shwifty_count = 0
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                shwifty_count += 1
    return shwifty_count

def selection_sort(A):
  for i in range(len(A)):  
      min_idx = i 
      for j in range(i+1, len(A)): 
          if A[min_idx] > A[j]: 
              min_idx = j          
      A[i], A[min_idx] = A[min_idx], A[i]  

def selection_sort_count(list):
  count = 0
  for i in range (len(list)):
    new_list = list[i:]
    positions = new_list.index(min_num(new_list))
    list.insert(i,list.pop(positions + i))
    count += positions
  return count

def disorder_ratio(list):
  l = bubble_sort_count(list)
  r = len(list)
  return r/l

def median(list1):
    list1.sort()
    if len(list1)%2>0:
          x = list1[int((len(list1)/2))]
    else:
          x = ((list1[int((len(list1)/2))-1])+(list1[int(((len(list1)/2)))]))/2
    return x






# Lists and Tuples Unit Test
# 1/15/20 @ 12:50 pm

#Helper Functions
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
    return (an_obj == another_obj) and not(an_obj is another_obj)

def approx_eq(expected, actual):
    if isinstance(actual, (int, float, complex)) and not isinstance(actual, bool):
        return abs(expected - actual) < 0.000001
    return False

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

    def __init__(self, func, name, cases, is_polyadic, is_mutator, test_type):
        # If the function is polyadic, we need to * the input so that it unpacks.
        # If the function is a mutator, we don't ask for its return value.
        # Instead we compare the input after the function is called to the correct mutated value.
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
        self.is_mutator = is_mutator
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
                expected_value = case[1]
                arg_str = build_arg_str(arg, unit.is_polyadic)
                test_file.write("Argument(s): " + arg_str + "  ")
                try:
                    if unit.is_polyadic:
                        actual_value = unit.func(*arg)
                    else:
                        actual_value = unit.func(arg) 
                except:
                    test_file.write("Crash! No point!\n")
                else:
                    if not unit.is_mutator:
                        if unit.test_type(expected_value, actual_value):
                            test_file.write("Return value correct! +1\n")
                            unit.score += 1
                        else:
                            test_file.write("Incorrect return value! No point!\n")
                    else:
                        if unit.is_polyadic:
                            mutated_value = arg[0]
                        else:
                            mutated_value = arg
                        if unit.test_type(expected_value, mutated_value):
                            test_file.write("Mutated value correct! +1\n")
                            unit.score += 1
                        else:
                            test_file.write("Incorrect mutated value! No point!\n")

            total_score += unit.score

        self.score = total_score
        test_file.write("\nFinal Score: " + str(self.score) + "/" + str(self.num_tests))

# Functions
# max_num, min_num, sum_elems, greatest_sum, dot_product, mean, mode
# perimeter, prime_list, prime_factorization, flatten, move, exchange
# elim_dups, bubble_sort, selection_sort, median

# Test Cases (tc)
# Format: a list of tuples where each tuple
# gives an argument (or tuple of arguments)
# and the expected return for that argument.
max_num_tc = [([0, 10**99, (-10)**99], 10**99),
              ([-1], -1)]
min_num_tc = [([0, 10**99, (-10)**99], (-10)**99),
              ([-1], -1)]
sum_elems_tc = [([1**2, 2**2, 3**2, 4**2], 30),
                ([-1], -1),
                ([], 0)]
greatest_sum_tc = [([[1], [2, 3, 4], [5, 6], [7]], 11),
                   ([[]], 0),
                   ([], 0)]
dot_product_tc = [(([1, 2, 3], [4, 5, 6]), 32),
                  ([[12], [12]], 144),
                  ([[], []], 0)]
mean_tc = [([1, 2, 3, 4, 5], 3),
           ([0], 0)]
mode_tc = [([1, 2, 2, 3, 3, 3, 2, 1], [2, 3]),
           ([1], [1]),
           ([], [])]
perimeter_tc = [(((1, 2), (1, 12), (-2, 0), (-12, 0)), 45.522263314818886),
                (((1, 1), ), 0),
                ((), 0)]
prime_list_tc = [((1, 100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])]
prime_factorization_tc = [(24, [2, 2, 2, 3]),
                          (23, [23])]
flatten_tc = [([[1, 2], [2, 3, 4], [4]], [1, 2, 2, 3, 4, 4]),
              ([[]], []),
              ([], [])]
L, I = [1, 2, 3], [1]
move_tc = [((L, 1, 2), [1, 3, 2]),
           ((I, 0, 0), [1])]
L, I = [1, 2, 3, 4], [1]
exchange_tc = [((L, 1, 2), [1, 3, 2, 4]),
               ((I, 0, 0), [1])]
elim_dups_tc = [([3, 2, 1, 2, 1, 4, 3], [3, 2, 1, 4]),
                ([3, 2, 1], [3, 2, 1]),
                ([], [])]
L = [24, 54, 39, 71, 42, 13, 9, 72, 19, 52, 95, 68, 88, 96, 61, 64, 69, 93, 83, 52, 53, 32, 1, 16, 97, 28, 61, 78, 30, 86, 11, 1, 22, 20, 8, 98, 6, 82, 91, 70, 31, 31, 40, 89, 41, 18, 18, 8, 87, 3, 45, 39, 72, 15, 19, 82, 97, 7, 12, 91, 9, 59, 44, 91, 37, 92, 90, 47, 31, 34, 2, 79, 19, 77, 30, 50, 32, 77, 5, 50, 4, 3, 98, 73, 44, 43, 21, 47, 70, 14, 100, 35, 23, 27, 40, 4, 47, 41, 93, 15]
I = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 8, 9, 9, 11, 12, 13, 14, 15, 15, 16, 18, 18, 19, 19, 19, 20, 21, 22, 23, 24, 27, 28, 30, 30, 31, 31, 31, 32, 32, 34, 35, 37, 39, 39, 40, 40, 41, 41, 42, 43, 44, 44, 45, 47, 47, 47, 50, 50, 52, 52, 53, 54, 59, 61, 61, 64, 68, 69, 70, 70, 71, 72, 72, 73, 77, 77, 78, 79, 82, 82, 83, 86, 87, 88, 89, 90, 91, 91, 91, 92, 93, 93, 95, 96, 97, 97, 98, 98, 100]
S = []
bubble_sort_tc = [(L, I), (S, S)]
L = [5, 8, 0, 2, 1]
I = [24, 54, 39, 71, 42, 13, 9, 72, 19, 52, 95, 68, 88, 96, 61, 64, 69, 93, 83, 52, 53, 32, 1, 16, 97, 28, 61, 78, 30, 86, 11, 1, 22, 20, 8, 98, 6, 82, 91, 70, 31, 31, 40, 89, 41, 18, 18, 8, 87, 3, 45, 39, 72, 15, 19, 82, 97, 7, 12, 91, 9, 59, 44, 91, 37, 92, 90, 47, 31, 34, 2, 79, 19, 77, 30, 50, 32, 77, 5, 50, 4, 3, 98, 73, 44, 43, 21, 47, 70, 14, 100, 35, 23, 27, 40, 4, 47, 41, 93, 15]
bubble_sort_count_tc = [(L, 7), (I, 2616)]
L = [24, 54, 39, 71, 42, 13, 9, 72, 19, 52, 95, 68, 88, 96, 61, 64, 69, 93, 83, 52, 53, 32, 1, 16, 97, 28, 61, 78, 30, 86, 11, 1, 22, 20, 8, 98, 6, 82, 91, 70, 31, 31, 40, 89, 41, 18, 18, 8, 87, 3, 45, 39, 72, 15, 19, 82, 97, 7, 12, 91, 9, 59, 44, 91, 37, 92, 90, 47, 31, 34, 2, 79, 19, 77, 30, 50, 32, 77, 5, 50, 4, 3, 98, 73, 44, 43, 21, 47, 70, 14, 100, 35, 23, 27, 40, 4, 47, 41, 93, 15]
I = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 8, 9, 9, 11, 12, 13, 14, 15, 15, 16, 18, 18, 19, 19, 19, 20, 21, 22, 23, 24, 27, 28, 30, 30, 31, 31, 31, 32, 32, 34, 35, 37, 39, 39, 40, 40, 41, 41, 42, 43, 44, 44, 45, 47, 47, 47, 50, 50, 52, 52, 53, 54, 59, 61, 61, 64, 68, 69, 70, 70, 71, 72, 72, 73, 77, 77, 78, 79, 82, 82, 83, 86, 87, 88, 89, 90, 91, 91, 91, 92, 93, 93, 95, 96, 97, 97, 98, 98, 100]
selection_sort_tc = [(L, I), (S, S)]
L = [5, 8, 0, 2, 1]
I = [24, 54, 39, 71, 42, 13, 9, 72, 19, 52, 95, 68, 88, 96, 61, 64, 69, 93, 83, 52, 53, 32, 1, 16, 97, 28, 61, 78, 30, 86, 11, 1, 22, 20, 8, 98, 6, 82, 91, 70, 31, 31, 40, 89, 41, 18, 18, 8, 87, 3, 45, 39, 72, 15, 19, 82, 97, 7, 12, 91, 9, 59, 44, 91, 37, 92, 90, 47, 31, 34, 2, 79, 19, 77, 30, 50, 32, 77, 5, 50, 4, 3, 98, 73, 44, 43, 21, 47, 70, 14, 100, 35, 23, 27, 40, 4, 47, 41, 93, 15]
selection_sort_count_tc = [(L, 7), (I, 2616)]
L = [24, 54, 39, 71, 42, 13, 9, 72, 19, 52, 95, 68, 88, 96, 61, 64, 69, 93, 83, 52, 53, 32, 1, 16, 97, 28, 61, 78, 30, 86, 11, 1, 22, 20, 8, 98, 6, 82, 91, 70, 31, 31, 40, 89, 41, 18, 18, 8, 87, 3, 45, 39, 72, 15, 19, 82, 97, 7, 12, 91, 9, 59, 44, 91, 37, 92, 90, 47, 31, 34, 2, 79, 19, 77, 30, 50, 32, 77, 5, 50, 4, 3, 98, 73, 44, 43, 21, 47, 70, 14, 100, 35, 23, 27, 40, 4, 47, 41, 93, 15]
disorder_ratio_tc = [(L, 0.0382262996941896)]
L = [24, 54, 39, 71, 42, 13, 9, 72, 19, 52, 95, 68, 88, 96, 61, 64, 69, 93, 83, 52, 53, 32, 1, 16, 97, 28, 61, 78, 30, 86, 11, 1, 22, 20, 8, 98, 6, 82, 91, 70, 31, 31, 40, 89, 41, 18, 18, 8, 87, 3, 45, 39, 72, 15, 19, 82, 97, 7, 12, 91, 9, 59, 44, 91, 37, 92, 90, 47, 31, 34, 2, 79, 19, 77, 30, 50, 32, 77, 5, 50, 4, 3, 98, 73, 44, 43, 21, 47, 70, 14, 100, 35, 23, 27, 40, 4, 47, 41, 93, 15]
I = [1]
S = [1, 2]
T = [1, 2, 3]
median_tc = [(L, 42.5), (I, 1), (S, 1.5), (T, 2)]

# Create Units
# This block will cause a crash if you haven't created all of the required functions.
# Format: Unit(func, name, cases, is_polyadic, is_mutator, test_type)
# Test types: eq_comp, is_comp, eq_not_is, elems_comp
max_num_unit = Unit(max_num, "max_num", max_num_tc, False, False, eq_comp)
min_num_unit = Unit(min_num, "min_num", min_num_tc, False, False, eq_comp)
sum_elems_unit = Unit(sum_elems, "sum_elems", sum_elems_tc, False, False, eq_comp)
greatest_sum_unit = Unit(greatest_sum, "greatest_sum", greatest_sum_tc, False, False, eq_comp)
dot_product_unit = Unit(dot_product, "dot_product", dot_product_tc, True, False, eq_comp)
mean_unit = Unit(mean, "mean", mean_tc, False, False, eq_comp)
mode_unit = Unit(mode, "mode", mode_tc, False, False, eq_comp)
perimeter_unit = Unit(perimeter, "perimeter", perimeter_tc, False, False, approx_eq)
prime_list_unit = Unit(prime_list, "prime_list", prime_list_tc, True, False, eq_comp)
prime_factorization_unit = Unit(prime_factorization, "prime_factorization", prime_factorization_tc, False, False, eq_comp)
flatten_unit = Unit(flatten, "flatten", flatten_tc, False, False, eq_comp)
move_unit = Unit(move, "move", move_tc, True, True, eq_comp)
exchange_unit = Unit(exchange, "exchange", exchange_tc, True, True, eq_comp)
elim_dups_unit = Unit(elim_dups, "elim_dups", elim_dups_tc, False, True, eq_comp)
bubble_sort_unit = Unit(bubble_sort, "bubble_sort", bubble_sort_tc, False, True, eq_comp)
bubble_sort_count_unit = Unit(bubble_sort_count, "bubble_sort_count", bubble_sort_count_tc, False, False, eq_comp)
selection_sort_unit = Unit(selection_sort, "selection_sort", selection_sort_tc, False, True, eq_comp)
selection_sort_count_unit = Unit(selection_sort_count, "selection_sort_count", selection_sort_count_tc, False, False, eq_comp)
disorder_ratio_unit = Unit(disorder_ratio, "disorder_ratio", disorder_ratio_tc, False, False, approx_eq)
median_unit = Unit(median, "median", median_tc, False, False, eq_comp)

# Unit Test List
units = [max_num_unit, min_num_unit, sum_elems_unit, greatest_sum_unit, dot_product_unit, mean_unit,
         mode_unit, perimeter_unit, prime_list_unit, prime_factorization_unit, flatten_unit, move_unit,
         exchange_unit, elim_dups_unit, bubble_sort_unit, bubble_sort_count_unit, selection_sort_unit,
         selection_sort_count_unit, disorder_ratio_unit, median_unit]

# Create Unit Test
unit_test = UnitTest("Lists and Tuples Unit Test", units)

# Run Test!
unit_test.run_test()
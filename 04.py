def implies(x, y):
    if y == True:
        return True
    # b1g brainer here didnt know about and
    # bruh moment
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
    else:
        grade = 'F'
    return grade


def tri_test(a, b, c):
    if (a+b) > c:
        if (a+c) > b:
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
    else:
        grade = 'F'
    return grade


def tri_test(a, b, c):
    if (a+b) > c:
        if (a+c) > b:
            return True
    else:
        return False



def order_three(a, b, c):
    if a>=b and a>=c:
        largest = a
    elif a>=b and a<=c:
        middle = a
    elif a<=b and a<=c:
        small = a
#testing for a ^^
    if b>=a and b>=c:
        largest = b
    elif b>=a and b<=c:
        b = middle
    elif b<=a and b<=c:
        small = b
#testing for b ^^
    if c>=a and c>= b:
        largest = c
    elif c >= a and c<=b:
        middle = b
    elif c<=b and c<=a:
        small = c
    return a, b, c


def digit_count(x):
    if x <= 9:
        return 1
    elif x <=99:
        return 2
    elif x <=999:
        return 3
    elif x <=9999:
        return 4
    elif x <= 99999:
        return 5
    elif x <= 999999:
        return 6
    elif x <= 9999999:
        return 7


def leap_year(y):
    x = y % 4
    z = y % 400
    if x > 0:
        return False
    elif z > 0:
        return False
    else:
        return True


def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
            break
    else:
        return True


def prime_list(num):
    lst = []
    for possiblePrime in range(2, num):
        prime = True
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if prime:
            lst.append(possiblePrime)

    return lst


def hailstone(n):
    while n != 1:
        if n % 2 == 0:
            n / 2
        else:
            (n * 3) +1

    print(n)
hailstone(27)
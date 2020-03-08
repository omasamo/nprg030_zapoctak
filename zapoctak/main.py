from itertools import count
from math import gcd
import random
import time

t1orig = 0
t2orig = 0
t1modif = 0
t2modif = 0
factorsmodif = []
factorsorig = []
number, x = 0, 2


def Miller_Rabin(d, n):
    a = 2 + random.randint(1, n - 4)
    res = 1
    a = a % n
    while (d > 0):

        if (d & 1):
            res = (res * a) % n
        d = d>>1
        a = (a * a) % n

    if (res == 1 or res == n - 1):
        return True

    while (d != n - 1):
        res = (res * res) % n
        d *= 2

        if (res == 1):
            return False
        if (res == n - 1):
            return True
    return False


def is_prime(n):
    if (n <= 1 or n == 4):
        return False
    if (n <= 3):
        return True
    d = n - 1
    while (d % 2 == 0):
        d //= 2
    # because M-R is probabilistic method, we are controlling accuracy by increasing or decreasing number of repetitions.
    for i in range(4):
        if (Miller_Rabin(d, n) == False):
            return False
    return True


def original_factorization(number, x):
    t1orig = time.perf_counter_ns()
    orignumber = number
    z = 1
    ex = 1
    while number != 1:
        for cycle in count(1):
            y = x
            for i in range(2 ** cycle):
                x = (x * x - 1) % number
                factor = gcd(x - y, number)
                if factor > 1:
                    factorsorig.append(factor)
                    number = int(number / factor)
                    z = z * factorsorig[-1]
                    if z == orignumber:
                        ex = 0
                    break
                if ex == 0:
                    break
            if ex == 0:
                break
        if ex == 0:
            break


def modified_factorization(number, x):
    z = 1
    ex = 1
    orignumber = number
    while number != 1:
        for cycle in count(1):
            y = x
            for i in range(2 ** cycle):
                x = (x * x + 1) % number
                factor = gcd(x - y, number)
                if factor > 1:
                    factorsmodif.append(factor)
                    number = int(number / factor)
                    z = z * factorsmodif[-1]
                    if z == orignumber:
                        ex = 0
                    break
                if ex == 0:
                    break
            if ex == 0:
                break
        if ex == 0:
            break


print("Welcome to program computing prime factors using different modifications of Pollards rho Method.")
print('Enter number to factorize :')
number = int(input())

'''print("Would you like to chose seed for the Pollards algorithm? Write Y for yes and N for no")
choice = input()
if choice == 'Y':
    print('Enter seed :')
    x = int(input())
else: x = 2'''
print('What timeout would you like to set?(in seconds)')
timeout_input = float(input())
print('Original algorithm results')

timeout = time.time() + timeout_input
end = 0
while time.time() < timeout and end == 0:
    t1orig = time.perf_counter_ns()
    original_factorization(number, x)
    end = 1
    t2orig = time.perf_counter_ns()

for fact in factorsorig:
    if (is_prime(fact)):
        print(fact, 'is prime   ')
    else:
        print(fact, 'is not prime, algorithm probably failed')
print('Modified algorithm results')

timeout = time.time() + timeout_input
end = 0
while time.time() < timeout and end == 0:
    t1modif = time.perf_counter_ns()
    modified_factorization(number, x)
    end = 1
    t2modif = time.perf_counter_ns()

for fact in factorsmodif:
    if (is_prime(fact)):
        print(fact, 'is prime   ')
    else:
        print(fact, 'is not prime, algorithm probably failed')

torig = t2orig - t1orig
tmodif = t2modif - t2modif
t = tmodif - torig
if t < 0:
    print('Modified algorithm is faster')
elif t > 0:
    print('Modified algorithm is slower')
else:
    print('Algorithms are equaly fast')

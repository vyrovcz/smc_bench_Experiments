#! /usr/bin/python

from random import randint, seed
import sys

def get_random_set(n: int):
        rand_set = set()
        while len(rand_set) < n:
                rand_set.add(randint(1, 3*n))
        return rand_set

def get_random_tupel(n: int):
        return [randint(1, 3*n) for i in range(n)]

def set_to_string(s: set):
        return ' '.join(map(str, s))

try:
        option = sys.argv[1][-1]
        n = int(sys.argv[2])
        seed(int(sys.argv[3]))

except:
        print("Usage: ./inputgen.py <option> <amount> <seed>")
        print("Options:")
        print("  -s: set,   Print <amount> many unique random numbers in range [1:3*<amount>]")
        print("  -t: tupel, Print <amount> many random numbers in range [1:3*<amount>]")
        exit()

match option:
        case 't':
                print(set_to_string(get_random_tupel(n)))
        case _:
                print(set_to_string(get_random_set(n)))
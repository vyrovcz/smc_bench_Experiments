#! /usr/bin/python

from random import randint, seed
import sys

def get_random_set(n: int):
        rand_set = set()
        while len(rand_set) < n:
                rand_set.add(randint(1, 3*n))
        return rand_set

def set_to_string(s: set):
        return ' '.join(map(str, s))

try:
        n = int(sys.argv[1])
        seed(int(sys.argv[2]))
except:
        print("Usage: ./inputgen.py <amount> <seed>")
        print("Print <amount> many random numbers in range [1:3*<amount>]")
        exit()

print(set_to_string(get_random_set(n)))

#! /usr/bin/python

from random import randint, seed, random
import sys

rand_range = 3
float_precision = 5

def get_random_set(n: int):
        rand_set = set()
        while len(rand_set) < n:
                rand_set.add(randint(1, rand_range*n))
        return rand_set

def get_random_tupel(n: int):
        return [randint(1, n) for i in range(n)]

def get_random_matrix(n: int):
        return [get_random_tupel(n) for i in range(n)]
        
def get_random_float_tupel(n: int):
        return [randint(1, n) + round(random(), float_precision) for i in range(n)]

def set_to_string(s: set):
        return ' '.join(map(str, s))

def matrix_to_string(m):
        return ' '.join(set_to_string(row) for row in m)

try:
        option = sys.argv[1][-1]
        n = int(sys.argv[2])
        seed(int(sys.argv[3]))

except:
        print("Usage: ./inputgen.py <option> <amount> <seed>")
        print("Options:")
        print("  -s: set,   Print <amount> many unique random numbers in range [1:3*<amount>]")
        print("  -t: tupel, Print <amount> many random numbers in range [1:<amount>]")
        print("  -f: float, Print <amount> many random numbers in range [1:<amount>]")
        print("  -m: matrix, Print <amount>^2 many random numbers in range [1:<amount>]")
        exit()

# python3.9 and lower support
if (option == 't'):
        print(set_to_string(get_random_tupel(n)))
elif (option == 'f'):
        print(set_to_string(get_random_float_tupel(n)))
elif (option == 'm'):
        print(matrix_to_string(get_random_matrix(n)))
else:
        print(set_to_string(get_random_set(n)))

#for future python3.10 and higher releases
#match option:
#        case 't':
#                print(set_to_string(get_random_tupel(n)))
#        case 'f':
#                print(set_to_string(get_random_float_tupel(n)))
#        case _:
#                print(set_to_string(get_random_set(n)))
# def counting():
#     count = 0
#     a = [1, 2, 1, 4]
#     for x in a:
#         for y in a:
#             if x == y:
#                 count+=1
#
#     return count
#
#
# print(counting())

import math


def sieve(size):
    sieve = [True] * size
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(math.sqrt(size)) + 1):
        k = i * 2
        while k < size:
            sieve[k] = False
            k += i

    return sum(1 for x in sieve if x)


print(sieve(100000000000))

# print('hello')
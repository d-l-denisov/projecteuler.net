#! /usr/bin/env python3

# author:   Denisov Denis
# date:     16.06.2016
#
# projecteuler.net 
#
# Task (https://projecteuler.net/problem=10):
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.
# 

import math
import time
number = 2000000

prime = [2, 3]

def isPrime(n, l):
# isPrime(n, t)     function that receives number n and tuple of all prime numbers t that are less than n.
#                   returns:    True if n is prime, 
#                               False if n is not prime

    s = math.ceil(math.sqrt(n))
    for i in l:
        if i <= s:
            if not (n % i): return(False)
    return(True)

d = 4
i = 5
while i < number:
    if isPrime(i, prime):
        prime.append(i)
    d = 2 if d>>1 == 2 else 4
    i += d 
#    print(i)

#print(prime)
print(sum(prime))


#! /usr/bin/env python3

# author:   Denisov Denis
# date:     03.06.2016
#
# Task (https://projecteuler.net/problem=3):
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?

number = 64

prime = []
mprime = []


def isPrime(n, l):
# isPrime(n, t)     function that receives number n and tuple of all prime numbers t that are less than n.
#                   returns:    True if n is prime, 
#                               False if n is not prime
    for i in l:
        if not (n % i): return(False)
    return(True)


t = number
i = 2
while i <= t:
    if isPrime(i, tuple(prime)):
        prime.append(i)
        j, k = divmod(t, i)
        if not k:
            t = j
            mprime.append(i)
    i += 1

print(mprime[-1])


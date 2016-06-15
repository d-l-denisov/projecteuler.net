#! /usr/bin/env python3

# author:   Denisov Denis
# date:     03.06.2016
#
# projecteuler.net 
#
# Task (https://projecteuler.net/problem=7):
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?
# 

number = 10001

prime = []

def isPrime(n, l):
# isPrime(n, t)     function that receives number n and tuple of all prime numbers t that are less than n.
#                   returns:    True if n is prime, 
#                               False if n is not prime
    for i in l:
        if not (n % i): return(False)
    return(True)


i = 2
while len(prime) < number:
    if isPrime(i, tuple(prime)):
        prime.append(i)
    i += 1

print(prime[-1])


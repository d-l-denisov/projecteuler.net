#! /usr/bin/env python3

# author:   Denisov Denis
# date:     17.06.2016
#
# projecteuler.net
#
# Task (https://projecteuler.net/problem=9):
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# 
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# 

threshold = 1000

import math

a = 1
while a < threshold:
    b = a
    r = 0
    while r < threshold:
        b += 1
        c = math.hypot(a, b)
        r = a + b + c
    if r == threshold:
        c = int(c)
        print(a,b,c, a*b*c)
        break
    a += 1
else: print("Cant find solution")

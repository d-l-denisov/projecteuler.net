#! /usr/bin/env python3

# author:   Denisov Denis
# date:     10.06.2016
#
# Task (https://projecteuler.net/problem=4):
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.

m = 0

for i in range(100,999):
    for j in range(100,999):
        p = i * j
        if (str(p) == str(p)[::-1]):
                if p > m:
                    m = p

print(m)



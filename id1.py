#! /usr/bin/env python3

# author:   Denisov Denis
# date:     01.06.2016

# Task (https://projecteuler.net/problem=1):
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 2 or 5 below 1000.

max_value = 1000
delta = (3, 2, 1, 3, 1, 2, 3, 3, 2, 1, 3, 1, 2, 3)

result = 0
k = 0
while k < max_value:
    for i in delta:
        k += i
        if k >= max_value:
            break
        result += k
print(result)




#! /usr/bin/env python3

# author:   Denisov Denis
# date:     15.06.2016
#
# projecteuler.net 
#
# Task (https://projecteuler.net/problem=6):
#
# 
# Sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# 
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# 
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


maxnumber = 100
r = [0, 0]

for i in range(1, maxnumber+1):
    r[0] += i**2 
    r[1] += i
    print(i,r)
#    input()

r[1] *= r[1]

print(r)
print(r[1]-r[0])

#! /usr/bin/env python3

# author:   Denisov Denis
# date:     23.06.2016
#
# projecteuler.net
#
# Task (https://projecteuler.net/problem=16):
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# 
# What is the sum of the digits of the number 2^1000?
# 

s = str(2 ** 1000)

dsum = 0

for i in s:
    dsum += int(i)

print(dsum)
